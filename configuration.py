from xdg import xdg_config_home
from os import path

class Configuration:
    key_list_colours = ['main_colour', 'nav_button_left_colour',
                'nav_button_right_colour', 'label_colour', 'font_colour']
    key_list_keybindings = ['go_forward', 'go_backward', 'calculate', 'add']

    def parse(self, f, choice):
        res = {}
        with open(f) as conf_file:
            content = conf_file.readlines()
            for content_pair in content:
                key, value = content_pair.split()
                if choice == 1:
                    if self.__check_colours__(key, value):
                        res[key] = value
                    else:
                        print('Parse Error')
                        break
                if choice == 2:
                    if self.__check_bindings__(value):
                        res[key] = value
        return res

class Colourscheme(Configuration):
    def __init__(self, conf_file):
        if conf_file != None:
            self.choice = 1
            self.conf_dict = self.parse(conf_file, self.choice)
        else:
            self.conf_dict = self.parse(path.join(xdg_config_home(), 'planer', 'planer_colours.txt', self.choice))

    def __check_colours__(self, key, val):
        alnum = val.isalnum()
        try:
            int(val, 16)
            return key in self.key_list_colours
        except ValueError:
            return alnum and (key in self.key_list_colours)

class Keybindings(Configuration):
    def __init__(self, conf_file):
        if conf_file != None:
            self.choice = 2
            self.conf_dict = self.parse(conf_file, self.choice)
        else:
            self.conf_dict = self.parse(path.join(xdg_config_home(), 'planer', 'planer_colours.txt', self.choice))

    def __check_bindings__(self, val):
        return val in self.key_list_keybindings

if __name__ == '__main__':
    c = Colourscheme('example_colours.txt')
    k = Keybindings('example_keys.txt')
    #print(c.conf_dict)
    print(k.conf_dict)
    for ki, vi in k.conf_dict.items():
        print(k.function_names[vi])

