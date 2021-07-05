import tkinter as tk
import configuration
import event
from datetime import datetime
import fileop

class SimpleUI:
    def __init__(self, master, cs, kb):
        self.xv = 15
        self.yv = 30
        self.scale = 1
        self.font_params = ('Helvetica', 20)
        self.stickyness = 'NSEW'
        self.orientation = 'center'
        self.master = master
        self.master.minsize(900, 500)
        self.cs = cs
        self.kb = kb
        self.master.title('Planer')
        self.inter = Interactions(self.kb, self)
        self.master = self.inter.ini_keybindings(self.master)
        self.buttons = []
        self.event_list = []
        self.textvar = tk.StringVar()
        self.save = fileop.FileOperations(open('testfile', 'wb'))

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                       'August', 'September', 'October', 'November', 'December']
        self.month_id = 0


        self.ini_nav()
        self.ini_cal_grid()
        self.ini_comp()

    def ini_comp(self):
        info_label = tk.Label(self.master, text='Add another event:', 
        anchor=self.orientation)
        info_label.grid(column=0, row=6) 
        entry = tk.Entry(self.master, width = 5, textvariable=self.textvar)
        entry.grid(column = 1, row = 6, ipadx = self.xv, 
                ipady = self.yv, sticky = self.stickyness)

        frame = tk.Frame(self.master)
        frame.grid(column=3, row=5, columnspan=3)
        removal_info = tk.Label(frame, text='To remove event provide its day and hours:', 
        anchor=self.orientation)
        removal_info.grid(column=0, row=0, sticky=self.stickyness) 
        self.rem_str = tk.StringVar()
        input_str = tk.Entry(frame, textvariable=self.rem_str, width=5)
        input_str.grid(column=0, row=1, sticky=self.stickyness)
        removal_button = tk.Button(self.master, text='Confirm', command=self.inter.remove)
        removal_button.grid(column=6, row=5)
 
    
    def ini_cal_grid(self):
        for special in range(1, 32):
            self.buttons.append(tk.Button(self.master, text=str(special), anchor = self.orientation, 
            command=lambda id=special : self.inter.add(id - 1)))

        for i in range(28):
            self.buttons[i].grid(column = i % 7, row = i // 7 + 1, ipadx = self.xv, 
                    ipady = self.yv, sticky = self.stickyness)
            self.buttons[i]['font'] = self.font_params
            self.buttons[i]['bg'] = self.cs.conf_dict['main_colour']

        for i in range(28, 31):
            self.buttons[i].grid(column = i % 7, row = 5, ipadx = self.xv, 
                        ipady = self.yv, sticky = self.stickyness)
            self.buttons[i]['font'] = self.font_params
            self.buttons[i]['bg'] = self.cs.conf_dict['main_colour']

        for i in range(7):
            tk.Grid.columnconfigure(self.master, i, weight=self.scale)
            tk.Grid.rowconfigure(self.master, i, weight=self.scale)

    def ini_nav(self):
        self.label = tk.Label(self.master, text=self.months[0], anchor = self.orientation)
        self.label.grid(column = 2, row = 0, columnspan = 3, sticky = self.stickyness)
        self.label['font'] = self.font_params
        self.label['bg'] = self.cs.conf_dict['label_colour']

        button_side1 = tk.Button(self.master, text='previous', anchor = self.orientation, command=lambda : self.inter.update_label_forw(-1))
        button_side2 = tk.Button(self.master, text='next', anchor= self.orientation, command=lambda : self.inter.update_label_forw(1))
        button_side1.grid(column = 0, row = 0, columnspan = 2, sticky = self.stickyness)
        button_side2.grid(column = 5, row = 0, columnspan = 2, sticky = self.stickyness)
        button_side1['bg'] = self.cs.conf_dict['nav_button_left_colour']
        button_side2['bg'] = self.cs.conf_dict['nav_button_right_colour']
        button_side1['font'] = self.font_params
        button_side2['font'] = self.font_params

    def has_31_days(self):
        return self.label['text'] in ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    
    def is_leap_year(self):
        year = datetime.today().year
        if year % 4:
            return False
        elif year % 100:
            return True
        elif year % 400:
            return False
        return True

class Interactions:
    text = ''
    def __init__(self, kb, ui):
        self.ui = ui
        self.function_names = {'add': self.add, 'go_forward' : lambda dummy : self.update_label_forw(1), 
                'go_backward' : lambda dummy : self.update_label_forw(-1)}
        self.kb = kb
        self.ids = {
            'January' : 31,
            'February' : 28 + self.ui.is_leap_year(),
            'March' : 31,
            'April' : 30,
            'May' : 31,
            'June' : 30,
            'July' : 31,
            'August' : 31,
            'September' : 30,
            'October' : 31,
            'November' : 30,
            'December' : 31
        }
    
    def remove(self):
        event_params = self.ui.rem_str.get().split('-')
        event_params[0] = int(self.get_day_id(int(event_params[0]) - 1))
        event_params[1] = tuple([int(h) for h in event_params[1].split(':')])
        event_params[2] = tuple([int(h) for h in event_params[2].split(':')])
        cnt = 0
        for e in self.ui.event_list:
            if e.get_id() == event_params[0]:
                if e.get_start() == event_params[1] and e.get_end() == event_params[2]:
                    self.ui.event_list.remove(e)
                    self.ui.save.remove()
                cnt += 1
        if cnt <= 1:
            self.ui.buttons[event_params[0]]['bg'] = self.ui.cs.conf_dict['main_colour']
        self.ui.rem_str.set('')

    def ini_keybindings(self, window):
        for ki, vi in self.kb.conf_dict.items():
            window.bind(f'<{ki}>', self.function_names[vi])
        return window
    
    def get_day_id(self, button_id):
        res = 0
        for m, v in self.ids.items():
            if m == self.ui.label['text']:
                break
            res += v
        return str(res + button_id)

    def reverse_id(self, day_id):
        months = list(self.ids.keys())
        it = 0
        while day_id > 31:
            day_id -= self.ids[months[it]]
            it += 1
        return (months[it], day_id)

    def update_label_forw(self, x, dummy=None):
        self.ui.month_id = (self.ui.month_id + x) % 12
        self.ui.label['text'] = self.ui.months[self.ui.month_id]
        if not self.ui.has_31_days():
            self.ui.buttons[-1].grid_remove()
            if self.ui.label['text'] == 'February':
                self.ui.buttons[-2].grid_remove()
                if not self.ui.is_leap_year():
                    self.ui.buttons[-3].grid_remove()
        else:
            self.ui.buttons[-1].grid(column = 2, row = 5, ipadx = self.ui.xv, 
                        ipady = self.ui.yv, sticky = self.ui.stickyness)
            self.ui.buttons[-2].grid(column = 1, row = 5, ipadx = self.ui.xv, 
                        ipady = self.ui.yv, sticky = self.ui.stickyness)
            self.ui.buttons[-3].grid(column = 0, row = 5, ipadx = self.ui.xv, 
                        ipady = self.ui.yv, sticky = self.ui.stickyness)
        for e in self.ui.event_list:
            md = self.reverse_id(e.get_id())
            if self.ui.label['text'] == md[0]:
                self.ui.buttons[md[1]]['bg'] = self.ui.cs.conf_dict['event_colour'] #'blue'
            else:
                self.ui.buttons[md[1]]['bg'] = self.ui.cs.conf_dict['main_colour']

    def add(self, id, dummy=None):
        self.ui.buttons[id]['bg'] = self.ui.cs.conf_dict['event_colour']
        e = event.Event(self.ui.textvar.get(), self.get_day_id(id))
        self.ui.event_list.append(e)
        self.ui.save.save(e)
        self.ui.textvar.set('') 

if __name__ == '__main__':
    root = tk.Tk()
    cs = configuration.Colourscheme('example_colours.txt')
    kb = configuration.Keybindings('example_keys.txt')
    test = SimpleUI(root, cs, kb)
    root.mainloop()
