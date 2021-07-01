import tkinter as tk
import tkinter.font
import configuration
import event

class SimpleUI:
    def __init__(self, master, cs, kb):
        self.master = master
        self.master.minsize(900, 500)
        self.cs = cs
        self.kb = kb
        self.master.title('Planer')

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                       'August', 'Semptember', 'October', 'November', 'December']
        self.month_id = 0
        self.function_names = {'add': Interactions.add, 'go_forward' : lambda dummy : self.update_label_forw(1), 
                'go_backward' : lambda dummy : self.update_label_forw(-1), 'calculate' : Interactions.calculate}

        self.xv = 15
        self.yv = 30
        self.scale = 1
        self.font_params = ('Helvetica', 20)
        self.stickyness = 'NSEW'
        self.orientation = 'center'

        self.ini_nav()
        self.ini_cal_grid()
        self.ini_keybindings()
        self.ini_comp()

    def ini_keybindings(self):
        for ki, vi in self.kb.conf_dict.items():
            self.master.bind(f'<{ki}>', self.function_names[vi])

    def ini_comp(self):
        # to jest dla dodania
        """entry = tk.Text(self.master, height = 5, width = 5) 
        entry.grid(column = 0, row = 6, sticky = self.stickyness)"""
        # this width is important
        entry = tk.Entry(self.master, width = 5)
        entry.grid(column = 0, row = 6, ipadx = self.xv, 
                ipady = self.yv, sticky = self.stickyness)
        confirm_add = tk.Button(self.master, text = 'confirm', anchor = self.orientation)
        confirm_add.grid(column = 1, row = 6, sticky = self.stickyness)
        confirm_add['font'] = ('Helvetica', 15)

    def ini_cal_grid(self):
        self.buttons = []
        for i in range(1, 32):
            self.buttons.append(tk.Button(self.master, text=f'{i}', anchor = self.orientation))

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
        
        for i in range(7):
            tk.Grid.rowconfigure(self.master, i, weight=self.scale)

    def ini_nav(self):
        self.label = tk.Label(self.master, text=self.months[0], anchor = self.orientation)
        self.label.grid(column = 2, row = 0, columnspan = 3, sticky = self.stickyness)
        self.label['font'] = self.font_params
        self.label['bg'] = self.cs.conf_dict['label_colour']

        button_side1 = tk.Button(self.master, text='previous', anchor = self.orientation, command=lambda : update_label_forw(-1))
        button_side2 = tk.Button(self.master, text='next', anchor= self.orientation, command=lambda : update_label_back(1))
        button_side1.grid(column = 0, row = 0, columnspan = 2, sticky = self.stickyness)
        button_side2.grid(column = 5, row = 0, columnspan = 2, sticky = self.stickyness)
        button_side1['bg'] = self.cs.conf_dict['nav_button_left_colour']
        button_side2['bg'] = self.cs.conf_dict['nav_button_right_colour']
        button_side1['font'] = self.font_params
        button_side2['font'] = self.font_params

    def update_label_forw(self, x, dummy=None):
        self.month_id = (self.month_id + x) % len(self.months)
        self.label['text'] = self.months[self.month_id]
        if not self.__has_31_days__():
            self.buttons[-1].grid_remove()
            if self.label['text'] == 'February':
                self.buttons[-2].grid_remove()
        else:
            self.buttons[-1].grid(column = 2, row = 5, ipadx = self.xv, 
                        ipady = self.yv, sticky = self.stickyness)
            self.buttons[-2].grid(column = 1, row = 5, ipadx = self.xv, 
                        ipady = self.yv, sticky = self.stickyness)

    def __has_31_days__(self):
        return self.label['text'] in ['January', 'March', 'May', 'July', 'August', 'October', 'December']

class Interactions:
    text = ''
    def __init__():
        self.function_names = {'add': self.add, 'go_forward' : lambda dummy : self.update_label_forw(1), 
                'go_backward' : lambda dummy : self.update_label_forw(-1), 'calculate' : self.calculate}

    def update_label_forw(self, x, dummy=None):
        self.month_id = (self.month_id + x) % 12
        self.label['text'] = self.months[self.month_id]
        if not self.__has_31_days__():
            self.buttons[-1].grid_remove()
            if self.label['text'] == 'February':
                self.buttons[-2].grid_remove()
        else:
            self.buttons[-1].grid(column = 2, row = 5, ipadx = self.xv, 
                        ipady = self.yv, sticky = self.stickyness)
            self.buttons[-2].grid(column = 1, row = 5, ipadx = self.xv, 
                        ipady = self.yv, sticky = self.stickyness)

    def add(self, dummy=None):
        # tu bedzie stworzenie eventa z dniem, godzina
        pass

    def calculate(self, dummy=None):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    cs = configuration.Colourscheme('example_colours.txt')
    kb = configuration.Keybindings('example_keys.txt')
    test = SimpleUI(root, cs, kb)
    root.mainloop()

