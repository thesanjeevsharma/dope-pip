#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk, messagebox

class Dopepip:

    def __init__(self, master):

        #Basic Configuration
        master.title('Dope pip')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font = ('Arial', 16, 'bold'))

        #Header Frame
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        self.logo = PhotoImage(file = 'res/dopepip.png')
        ttk.Label(self.header_frame, image = self.logo).grid(row = 0, column = 0, rowspan = 2, padx = 5)
        ttk.Label(self.header_frame, text = 'Easy way to install, upgrade, and remove py apps.', style = 'Header.TLabel').grid(row = 0, column = 1, padx = 5)
        ttk.Label(self.header_frame, text = 'Gifted to the community, by @thesanjeevsharma', font = ('Arial', 12 )).grid(row = 1, column = 1, padx = 5)
        
        
        
        #Content Frame
        self.content_frame = ttk.Frame(master)
        self.content_frame.pack()

        ##Frame to display installed apps with update functionality
        self.installed_frame = ttk.Frame(self.content_frame)

        ##Frame to download new apps
        self.download_frame = ttk.Frame(self.content_frame)

        ##Frame to display logs
        self.logs_frame = ttk.Frame(self.content_frame)



        
        
def main():            
    
    root = Tk()
    dopepip = Dopepip(root)
    root.mainloop()
    
if __name__ == "__main__": main()
