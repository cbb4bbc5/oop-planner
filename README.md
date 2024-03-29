# OOP course project

# Table of contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
	* [Navigation](#navigation)
	* [Adding an event](#adding-an-event)
	* [Editing configuration files](#editing-configuration-files)
	* [Temporary configuration change](#temporary-configuration-change)

## Overview
This repository contains the source code for a simple planner. Main functions of this program are:
* displaying the calendar view of __current__ year
* adding reminders
* customisation using two configuration files named (txt extension is required for simplicity reasons):
  * keybindings.txt
  * colourscheme.txt
* one time customisation using custom files
* respecting XDG BASE DIRECTORY (mixed results)

## Installation
The project was made using Python 3.9.4. It was primarily tested on
Windows 10 and briefly on Arch Linux. The only non-standard required
module is [this one](https://pypi.org/project/xdg/).

To run the demonstration program just run file called simple.py

## Usage
### Navigation
To move one month forward press the button with text 'next' on it. By
default right arrow key can be used as well. Similarly to go back press 
button label 'previous' or left arrow key.
### Adding an event
Write the text and starting hour and ending hour of the event in the 
specified format HH:MM-HH:MM-event text can contain white characters.
Other delimiters are important and cannot be changed without editing
the source code.

Then just click on a button representing date on which your event takes 
place. Program will highlight it (by default it is colour blue). The 
input field will be then automatically cleared.
### Editing configuration files
They should be located in the ```$XDG_CONFIG_HOME/planer``` if the
corresponding environmental variable is set. Otherwise they cannot
be used. In this case refer to [Temporary configuration change](#temporary-configuration-change)

Accepted keys and their values for colourscheme are the following:
* main_colour
* nav_button_left_colour
* nav_button_right_colour
* label_colour
* font_colour

For the list of values refer to 
[this page](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter).

And for keybidnings:
* go_forward
* go_backward
* add

### Temporary configuration change
Just initialise the instance of class Colourscheme or Keybindings with the
absolute path to your configuration files to change looks or interactions
respectively.
