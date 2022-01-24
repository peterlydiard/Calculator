'''
Created on 22 Jan 2022

@author: peter
'''
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    '''
    classdocs
    '''
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '=']

    def __init__(self, controller):
        '''
        Constructor
        '''
        super().__init__()
        
        self.controller = controller
        
        self.value_var = tk.StringVar()
        
        self.title("PyCalc 1.0")
        
        self.config(bg="black")
        
        self._configure_button_styles()
        
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        self._centre_window()
        
    def _configure_button_styles(self):
        style = ttk.Style()
        #print(style.theme_names())
        #print(style.theme_use())
        style.theme_use('alt')
        
        # style for number buttons
        style.configure('N.TButton', foreground='white', background='grey')
        # style for operator buttons
        style.configure('O.TButton', foreground='white', background='orange')
        # style for miscellaneous buttons
        style.configure('M.TButton', background='white')
        
        
    def main(self):
        # print("In main of view")
        self.mainloop() # infinite loop!
    
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
               
        
    def _make_label(self):
        lbl = tk.Label(self.main_frm, anchor='e', textvariable=self.value_var, 
                       bg='black', fg='white', font=('Arial', 30))
        lbl.pack(fill='x') # fill along x axis
        
        
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack() 
        
        is_first_row = True
        buttons_in_row = 0
        
        for caption in self.button_captions:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False
                buttons_in_row = 0
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x') # packs vertically by default
                
            if isinstance(caption, int):
                style_prefix = 'N'
            elif caption in ['/', '*', '+', '-', '=']:
                style_prefix = 'O'
            else:
                style_prefix = 'M'
                
            style_name =f'{style_prefix}.TButton'
            
            btn = ttk.Button(
                frm, text=caption, command=
                    (lambda button=caption: self.controller.on_button_click(button)
                     ),
                style=style_name
                )
            
            if caption == 0: # Let 0 button expand to fill bottom row
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0
                
            btn.pack(fill=fill, expand=expand, side='left') # pack buttons horizontally
            buttons_in_row += 1
            
    def _centre_window(self):
        self.update()                # update winfo data after creating widgets
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
            
            