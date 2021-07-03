import tkinter as tk
import configuration
import event

class SimpleUI:
    def __init__(self, master, cs, kb):
        self.master = master
        self.master.minsize(900, 500)
        self.cs = cs
        self.kb = kb
        self.master.title('Planer')
        self.inter = Interactions(self.kb, self)
        self.master = self.inter.ini_keybindings(self.master)
        self.buttons = []

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                       'August', 'Semptember', 'October', 'November', 'December']
        self.month_id = 0

        self.xv = 15
        self.yv = 30
        self.scale = 1
        self.font_params = ('Helvetica', 20)
        self.stickyness = 'NSEW'
        self.orientation = 'center'

        self.ini_nav()
        self.ini_cal_grid()
        self.ini_comp()

    def ini_comp(self):
        entry = tk.Entry(self.master, width = 5)
        entry.grid(column = 0, row = 6, ipadx = self.xv, 
                ipady = self.yv, sticky = self.stickyness)
        """confirm_add = tk.Button(self.master, text = 'confirm', anchor = self.orientation, 
                                command=self.test1)
        confirm_add.grid(column = 1, row = 6, sticky = self.stickyness)
        confirm_add['font'] = self.font_params"""
    
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

class Interactions:
    text = ''
    def __init__(self, kb, ui):
        self.ui = ui
        self.function_names = {'add': self.add, 'go_forward' : lambda dummy : self.update_label_forw(1, self.ui), 
                'go_backward' : lambda dummy : self.update_label_forw(-1, self.ui), 'calculate' : self.calculate}
        self.kb = kb

    def ini_keybindings(self, window):
        for ki, vi in self.kb.conf_dict.items():
            window.bind(f'<{ki}>', self.function_names[vi])
        return window

    #def update_label_forw(self, x, ui, dummy=None):
    def update_label_forw(self, x, dummy=None):
        self.ui.month_id = (self.ui.month_id + x) % 12
        self.ui.label['text'] = self.ui.months[self.ui.month_id]
        if not self.ui.has_31_days():
            self.ui.buttons[-1].grid_remove()
            if self.ui.label['text'] == 'February':
                self.ui.buttons[-2].grid_remove()
        else:
            self.ui.buttons[-1].grid(column = 2, row = 5, ipadx = self.ui.xv, 
                        ipady = self.ui.yv, sticky = self.ui.stickyness)
            self.ui.buttons[-2].grid(column = 1, row = 5, ipadx = self.ui.xv, 
                        ipady = self.ui.yv, sticky = self.ui.stickyness)

    def add(self, id, dummy=None):
        if self.ui.buttons[id]['bg'] == self.ui.cs.conf_dict['main_colour']:
            self.ui.buttons[id]['bg'] = 'blue'
        else:
            self.ui.buttons[id]['bg'] = self.ui.cs.conf_dict['main_colour']

    def calculate(self, dummy=None):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    cs = configuration.Colourscheme('example_colours.txt')
    kb = configuration.Keybindings('example_keys.txt')
    test = SimpleUI(root, cs, kb)
    root.mainloop()
