# Brant Buckley
# Class: Intro to Python
# File: FinalMusicGUI.py
# Date: 5/01/22
# Description: This is the final project music GUI. The GUI consists of text boxes
# to display the scale data in a list box. There is also a clear button and exit button as well
# as radio buttons to change the displayed text. All 12 musical keys are avaialble. The major scale entry box
# will display the major scale input and the major scale chords. The minor scale entry box will display the relative minor scale
# input and the relative minor scale chords.

import tkinter
import tkinter.messagebox
import tkinter.font
from ScaleTheory import ScaleTheory
import tkinter.filedialog

class MusicGUI:
    
    # Class Level Variables for Font.
    TIMES_FONT = 'Times New Roman'
    AR = 'Arial'
    
    def __init__(self):
        # Empty list to hold the displayed Scales.
        self.__scaleList = []
        # Creating the main window.
        self.main_window = tkinter.Tk()
        # Displaying the title.
        self.main_window.title('Music GUI')
        # Enter the screen dimensions.
        self.main_window.geometry("1500x500+10+20")
        
        # Creating a scrollbar.
        self.scrollbar = tkinter.Scrollbar(self.main_window, orient = tkinter.HORIZONTAL)
        self.scrollbar.pack(side=tkinter.BOTTOM, fill="x") 
        
        # Create two frames for to input musical major and minor scales.
        # A third fram for buttons.
        self.scale1_frame = tkinter.Frame(self.main_window)
        self.scale2_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        # Creating/Packing Widgets for the Major Scale.
        self.scale1_label = tkinter.Label(self.scale1_frame,
                                          text='Enter a Major Scale:')
        self.scale1_entry = tkinter.Entry(self.scale1_frame,
                                          width=30)
        self.scale1_label.pack(side='left')
        self.scale1_entry.pack(side='left')
        
        # Creating/Packing Widgets for the Minor Scale.
        self.scale2_label = tkinter.Label(self.scale2_frame,
                                          text='Enter a Relative Minor Scale:')
        self.scale2_entry = tkinter.Entry(self.scale2_frame,
                                          width=30)
        self.scale2_label.pack(side='left')
        self.scale2_entry.pack(side='left')
        
        # Create and pack the button widgets.
        self.display_button = tkinter.Button(self.button_frame,
                                             text='Display',
                                             command=self.display)
        self.clear_button = tkinter.Button(self.button_frame,
                                             text='Clear',
                                           command=self.clear)
        
        self.exit_button = tkinter.Button(self.button_frame,
                                             text='Exit',
                                          command=self.main_window.destroy)
        self.display_button.pack(side='left')
        self.clear_button.pack(side='left')
        self.exit_button.pack(side='left')
        
        # Packing the frames.
        self.scale1_frame.pack()
        self.scale2_frame.pack()
        self.button_frame.pack()
        
        # Create two Radiobuttons for font of display.
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create an StringVar Object to use on Radiobuttons and
        # Set the StringVar object to
        self.font_fam = tkinter.StringVar()
        self.font_fam.set(MusicGUI.AR)
        
        # Create Radiobutton widgets in the bottom_frame.
        self.rb1 = tkinter.Radiobutton(self.bottom_frame,
                                       text ='Times New Roman',
                                       variable = self.font_fam,
                                       value = MusicGUI.TIMES_FONT)
        self.rb2 = tkinter.Radiobutton(self.bottom_frame,
                                       text ='Arial',
                                       variable = self.font_fam,
                                       value = MusicGUI.AR)
        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        
        # Pack the frames.
        self.bottom_frame.pack()
        
        # Creating a Listbox.
        # Create a listbox widget.
        self.listbox = tkinter.Listbox(self.main_window, width = 170, height = 30)
        self.listbox.pack(padx=50, pady=10)
        
        # Populate the Listbox with the data.
        self.listbox.insert(0)
        
        # Configuring the scroll bar to scroll.
        self.scrollbar.config(command=self.listbox.xview)
        
        # Creating a menu bar.
        self.menubar = tkinter.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        # Adding file menu options.
        self.file_menu = tkinter.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'Save Scales...',
                                   command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Exit',
                                   command = self.main_window.destroy)
        
        # Start the main loop.
        tkinter.mainloop()
        
    # Function to display the users scale input in the GUI.
    def display(self):
        # Creating Key Objects from MusicTheory(majorScale, majorChords, relativeMinorscale, relativeMinorchords).
        C_Major = ScaleTheory(('C','D','E','F','G','A','B','C'), {'C Major': 'CEG','D Minor': 'DFA','E Minor': 'EGB',
                  'F Major': 'FAC','G Major': 'GBD','A Minor': 'ACE','B Diminished': 'BDF'}, ('A','B','C','D','E','F','G','A'),
                  {'A Minor': 'ACE','B Diminished': 'BDF','C Major': 'CEG','D Minor': 'DFA','E Minor': 'EGB','F Major': 'FAC',
                  'G Major': 'GBD'})
 
        G_Major = ScaleTheory(('G','A','B','C','D','E','F#','G'), {'G Major': 'GBD','A Minor': 'ACE','B Minor': 'BDF#',
                  'C Major': 'CEG','D Major': 'DF#A','E Minor': 'EGB','F# Diminished': 'F#AC'}, ('E','F#','G','A','B','C','D','E'),
                  {'E Minor': 'EGB','F# Diminished': 'F#AC','G Major': 'GBD','A Minor': 'ACE','B Minor': 'BDF#','C Major': 'CEG',
                  'D Major': 'DF#A'})
    
        D_Major = ScaleTheory(('D','E','F#','G','A','B','C#','D'), {'D Major': 'DF#A','E Minor': 'EGB','F# Minor': 'F#AC#',
                  'G Major': 'GBD','A Major': 'AC#E','B Minor': 'BDF#','C# Diminished': 'C#EG'}, ('B','C#','D','E','F#','G','A','B'),
                  {'B Minor': 'BDF#','C# Diminished': 'C#EG','D Major': 'DF#A','E Minor': 'EGB','F# Minor': 'F#AC','G Major': 'GBD',
                  'A Major': 'AC#E'})
    
        A_Major = ScaleTheory(('A','B','C#','D','E','F#','G#','A'), {'A Major': 'AC#E','B Minor': 'BDF#','C# Minor': 'C#EG',
                  'D Major': 'DF#A','E Major': 'EG#B','F# Minor': 'F#AC#','G# Diminished': 'G#BD'}, ('F#','G#','A','B','C#','D','E','F#'),
                  {'F# Minor': 'F#AC#','G# Diminished': 'G#BD','A Major': 'AC#E','B Minor': 'BDF#','C# Minor': 'C#EG','D Major': 'DF#A',
                  'E Major': 'EG#B'})
    
        E_Major = ScaleTheory(('E','F#','G#','A','B','C#','D#','E'), {'E Major': 'EG#B','F# Minor': 'F#AC#','G# Minor': 'G#BD#',
                  'A Major': 'AC#E','B Major': 'BD#F#','C# Minor': 'C#EG#','D# Diminished': 'D#F#A'}, ('C#','D#','E','F#','G#','A','B','C#'),
                  {'C# Minor': 'C#EG#','D# Diminished': 'D#F#A','E Major': 'EG#B','F# Minor': 'F#AC#','G# Minor': 'G#BD#','A Major': 'AC#E',
                  'B Major': 'BD#F#'})
    
        B_Major = ScaleTheory(('B','C#','D#','E','F#','G#','A#','B'), {'B Major': 'BD#F#','C# Minor': 'C#EG#','D# Minor': 'D#F#A#',
                  'E Major': 'EG#B','F# Major': 'F#A#C#','G# Minor': 'G#BD#','A# Diminished': 'A#C#E'}, ('G#','A#','B','C#','D#','E','F#','G#'),
                  {'G# Minor': 'G#BD#','A# Diminished': 'A#C#E','B Major': 'BD#F#','C# Minor': 'C#EG#','D# Minor': 'D#F#A','E Major': 'EG#B',
                  'F# Major': 'F#A#C#'})
    
        Fsharp_Major = ScaleTheory(('F#','G#','A#','B','C#','D#','E#','F#'), {'F# Major': 'F#A#C#','G# Minor': 'G#BD#','A #Minor': 'A#C#E#',
                   'B Major': 'BD#F#','C# Major': 'C#E#G#','D# Minor': 'D#F#A#','E# Diminished': 'E#G#B'}, ('D#','E#','F#','G#','A#','B','C#','D#'),
                   {'D# Minor': 'D#F#A#','E# Diminished': 'E#G#B','F# Major': 'F#A#C#','G# Minor': 'G#BD#','A# Minor': 'A#C#E','B Major': 'BD#F#',
                   'C# Major': 'C#E#G#'})
    
        C_Sharp_Major = ScaleTheory(('C#','D#','E#','F#','G#','A#','B#','C#'), {'C# Major': 'C#E#G#','D# Minor': 'D#F#A#','E# Minor': 'E#G#B#',
                   'F# Major': 'F#A#C#','G# Major': 'G#B#D#','A# Minor': 'A#C#E#','B# Diminished': 'B#D#F#'}, ('A#','B#','C#','D#','E#','F#','G#','A#'),
                   {'A# Minor': 'A#C#E#','B# Diminished': 'B#D#F#','C# Major': 'C#E#G#','D# Minor': 'D#F#A#','E# Minor': 'E#G#B#','F# Major': 'F#A#C#',
                   'G# Major': 'G#B#D#'})
    
        F_Major = ScaleTheory(('F','G','A','Bb','C','D','E','F'), {'F Major': 'FAC','G Minor': 'GBbD','A Minor': 'ACE','Bb Major': 'BbDF',
                   'C Major': 'CEG','D Minor': 'DFA','E Diminished': 'EGBb'}, ('D','E','F','G','A','Bb','C','D'), {'D Minor': 'DFA','E Diminished': 'EGBb',
                   'F Major': 'FAC','G minor': 'GBbD','A Minor': 'ACE','Bb Major': 'BbDF',
                   'C Major': 'CEG'})
    
        Bflat_Major = ScaleTheory(('Bb','C','D','Eb','F','G','A','Bb'), {'C Major': 'CEG','D Minor': 'DFA','E Minor': 'EGB','F Major': 'FAC',
                   'G Major': 'GBD','A Minor': 'ACE','B Diminished': 'BDF','C Major': 'CEG'}, ('G','A','Bb','C','D','Eb','F','G'), {'G Minor': 'GBbD',
                   'A Diminished': 'ACEb','Bb Major': 'BbDF','C minor': 'CEbG','D Minor': 'DFA','Eb Major': 'EbGBb',
                   'F Major': 'FAC'})
    
        Eflat_Major = ScaleTheory(('Eb','F','G','Ab','Bb', 'C', 'D', 'Eb'), {'Eb Major': 'EbGBb','F Minor': 'FAbC','G Minor': 'GbBD',
                   'Ab Major': 'AbCEb','Bb Major': 'BbDF','C Minor': 'CEbG','D Diminished': 'DFAb'}, ('C', 'D', 'Eb','F','G','Ab','Bb', 'C'), {'C Minor': 'CEbG',
                   'D Diminished': 'DFAb','Eb Major': 'EbGBb','F minor': 'FAbC','G Minor': 'GBbD','Ab Major': 'AbCEb',
                   'Bb Major': 'BbDF'})
    
        Aflat_Major = ScaleTheory(('Ab','Bb', 'C', 'Db', 'Eb','F','G','Ab'), {'Ab Major': 'AbCEb','Bb Minor': 'BbDbF','C Minor': 'CEbG',
                   'Db Major': 'DbFAb','Eb Major': 'EbGBb','F Minor': 'FAbC','G Diminished': 'GBbDb'}, ('F','G','Ab','Bb','C','Db','Eb','F'), {'F Minor': 'FAbC',
                   'G Diminished': 'GBbDb','Ab Major': 'AbCEb','Bb minor': 'BbDbF','C Minor': 'CEbG','Db Major': 'DbFAb',
                   'Eb Major': 'EbGBb'})
        
        # Getting the user input data and storing it into a variable.
        entryMajor = self.scale1_entry.get()
        entryMinor = self.scale2_entry.get()
        
        # Displaying Font options.
        fontToUse = tkinter.font.Font(family = self.font_fam.get(),
                                      weight = 'normal')
        self.listbox.config(font = fontToUse)
        
        # Try/except if major scale is input incorrectly.
        try:
            # If and elif statements to determine the correct key for Major Scales and Major Chords.
            if entryMajor == 'C':
                self.__scaleList.append(C_Major.Majors())
                self.listbox.insert(0, C_Major.Majors())
            elif entryMajor == 'G':
                self.__scaleList.append(G_Major.Majors())
                self.listbox.insert(0, G_Major.Majors())
            elif entryMajor == 'D':
                self.__scaleList.append(D_Major.Majors())
                self.listbox.insert(0, D_Major.Majors())
            elif entryMajor == 'A':
                self.__scaleList.append(A_Major.Majors())
                self.listbox.insert(0, A_Major.Majors())
            elif entryMajor == 'E':
                self.__scaleList.append(E_Major.Majors())
                self.listbox.insert(0, E_Major.Majors())
            elif entryMajor == 'B':
                self.__scaleList.append(B_Major.Majors())
                self.listbox.insert(0, B_Major.Majors())
            elif entryMajor == 'F#':
                self.__scaleList.append(Fsharp_Major.Majors())
                self.listbox.insert(0, Fsharp_Major.Majors())
            elif entryMajor == 'C#':
                self.__scaleList.append(C_Sharp_Major.Majors())
                self.listbox.insert(0, C_Sharp_Major.Majors())
            elif entryMajor == 'F':
                self.__scaleList.append(F_Major.Majors())
                self.listbox.insert(0, F_Major.Majors())
            elif entryMajor == 'Bb':
                self.__scaleList.append(Bflat_Major.Majors())
                self.listbox.insert(0, Bflat_Major.Majors())
            elif entryMajor == 'Eb':
                self.__scaleList.append(Eflat_Major.Majors())
                self.listbox.insert(0, Eflat_Major.Majors())
            elif entryMajor == 'Ab':
                self.__scaleList.append(Aflat_Major.Majors())
                self.listbox.insert(0, Aflat_Major.Majors())
            elif entryMajor != ('C' or 'G' or'D' or 'A' or 'E' or 'B' or 'F#' or 'C#' or 'F' or 'Bb' or 'Eb' or 'Ab'):
                raise NameError()
        except NameError:
            tkinter.messagebox.showerror('Error!',
                                         'Use a Capital letter! C or C#')
            
        # Try/except if minor scale is input incorrectly.
        try:
            # If and elif statements to determine the correct key for Minor Scales and Minor Chords.
            if entryMinor == 'C':
                self.__scaleList.append(C_Major.Minors())
                self.listbox.insert(1, C_Major.Minors()) 
            elif entryMinor == 'G':
                self.__scaleList.append(G_Major.Minors())
                self.listbox.insert(1, G_Major.Minors())
            elif entryMinor == 'D':
                self.__scaleList.append(D_Major.Minors())
                self.listbox.insert(1, D_Major.Minors())
            elif entryMinor == 'A':
                self.__scaleList.append(A_Major.Minors())
                self.listbox.insert(1, A_Major.Minors())
            elif entryMinor == 'E':
                self.__scaleList.append(E_Major.Minors())
                self.listbox.insert(1, E_Major.Minors())
            elif entryMinor == 'B':
                self.__scaleList.append(B_Major.Minors())
                self.listbox.insert(1, B_Major.Minors())
            elif entryMinor == 'F#':
                self.__scaleList.append(Fsharp_Major.Minors())
                self.listbox.insert(1, Fsharp_Major.Minors())
            elif entryMinor == 'C#':
                self.__scaleList.append(C_Sharp_Major.Minors())
                self.listbox.insert(1, C_Sharp_Major.Minors())
            elif entryMinor == 'F':
                self.__scaleList.append(F_Major.Minors())
                self.listbox.insert(1, F_Major.Minors())
            elif entryMinor == 'Bb':
                self.__scaleList.append(Bflat_Major.Minors())
                self.listbox.insert(1, Bflat_Major.Minors())
            elif entryMinor == 'Eb':
                self.__scaleList.append(Eflat_Major.Minors())
                self.listbox.insert(1, Eflat_Major.Minors())
            elif entryMinor == 'Ab':
                self.__scaleList.append(Aflat_Major.Minors())
                self.listbox.insert(1, Aflat_Major.Minors())
            elif entryMinor != ('C' or 'G' or'D' or 'A' or 'E' or 'B' or 'F#' or 'C#' or 'F' or 'Bb' or 'Eb' or 'Ab'):
                raise NameError()
        except NameError:
            tkinter.messagebox.showerror('Error!',
                                         'Use a Capital letter! B or Bb')

    # Function to for clearing GUI and exiting GUI.
    def clear(self):
        # Removing all text from the entry field.
        self.scale1_entry.delete(0, tkinter.END)
        self.scale2_entry.delete(0, tkinter.END)
        self.listbox.delete(0, tkinter.END)
        # Set focus on scale1.
        self.scale1_entry.focus()
        
    # Function to save the scales out to a .txt file.
    def save_file(self):
        # Get the filename.
        file_name = tkinter.filedialog.asksaveasfilename(initialdir = '/',
                                        filetypes = [('Text Files', '*.txt'),
                                                      ('All Files', '*.*')],
                                        title = 'Select file for saving',
                                        defaultextension = '*.txt')
        # Checking for empty string.
        if len(file_name) != 0:
            # Open file.
            self.file_var = open(file_name, 'w')
            for scale in self.__scaleList:
                scale_string = '{}\n'.format(scale)
            # Write to the file.
                self.file_var.write(scale_string)
            # Close the file.
            self.file_var.close()
            
# Creating an instance for MusicGUI class.
if __name__ == '__main__':
    music_gui = MusicGUI()
    
    
    
    
    

        
        