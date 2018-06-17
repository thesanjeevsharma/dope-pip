#!/usr/bin/python3
# main.py of dope-pip by Sanjeev Sharma
# GitHub: @thesanjeevsharma, Website: www.thesanjeevsharma.com

import subprocess
from tkinter import *
from tkinter import ttk, messagebox

class Dopepip:

    def __init__(self, master):

        #Basic Configuration
        master.title('Dope pip')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('Header.TLabel', font = ('Arial', 14, 'bold'))

        #Header Frame
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        self.logo = PhotoImage(file = 'res/dopepip.png')
        ttk.Label(self.header_frame, image = self.logo).grid(row = 0, column = 0, rowspan = 2, padx = 5)
        ttk.Label(self.header_frame, text = 'Easy way to install, upgrade, and remove py apps.', style = 'Header.TLabel').grid(row = 0, column = 1, padx = 5)
        ttk.Label(self.header_frame, text = 'Gifted to the community, by @thesanjeevsharma', font = ('Arial', 8 )).grid(row = 1, column = 1, padx = 5, sticky = 'n')
        
        
        #Content Frame
        self.content_frame = ttk.Frame(master)
        self.content_frame.pack()

        ##Frame to display installed apps with update functionality
        self.installed_frame = ttk.Frame(self.content_frame)
        self.installed_frame.grid(row = 0, column = 0, rowspan = 2, padx = 5, pady = 5)

        self.tree = ttk.Treeview(self.installed_frame)
        self.tree.insert('', 'end', 'installed', text = 'Installed Apps')

        self.tree.grid(row = 0, column = 0, columnspan = 3, sticky = 'ew')

        self.remove_button = ttk.Button(self.installed_frame, text = 'Remove')
        self.remove_button.grid(row = 1, column = 0)
        self.update_button = ttk.Button(self.installed_frame, text = 'Update')
        self.update_button.grid(row = 1, column = 1)
        self.updateAll_button = ttk.Button(self.installed_frame, text = 'Update All')
        self.updateAll_button.grid(row = 1, column = 2)

        ##Frame to download new apps
        self.download_frame = ttk.Frame(self.content_frame)
        self.download_frame.grid(row = 0, column = 1, padx = 5, pady = 5)

        ttk.Label(self.download_frame, text = 'Install new packages').grid(row = 0, column = 0, sticky = 'w')
        
        self.download_entry = ttk.Entry(self.download_frame, width = 30, font = ('Arial', 14))
        self.download_entry.grid(row = 1, column = 0, padx = 5)
        ttk.Button(self.download_frame, text = 'Install').grid(row = 1, column = 1, padx = 5)
        
        ##Frame to display logs
        self.logs_frame = ttk.Frame(self.content_frame)
        self.logs_frame.grid(row = 1, column = 1, padx = 5, pady = 5)

        ttk.Label(self.logs_frame, text = 'Logs').grid(row = 0, column = 0, sticky = 'w')
        
        self.logs = Text(self.logs_frame, height = 10, width = 60, font = ('Arial', 10))
        self.logs.grid(row = 1, column = 0, sticky = 'w')


        
        
def main():            
    
    root = Tk()
    result = subprocess.run(['pip','list'], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))
    dopepip = Dopepip(root)
    root.mainloop()
    
if __name__ == "__main__": main()
