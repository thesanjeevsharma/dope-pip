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

        self.logo = PhotoImage(file = 'res/dopepip.png')
        self.ok = PhotoImage(file = 'res/ok.png')
        self.notok = PhotoImage(file = 'res/notok.png')

        #Header Frame
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, image = self.logo).grid(row = 0, column = 0, rowspan = 2, padx = 5)
        ttk.Label(self.header_frame, text = 'Easy way to install, upgrade, and remove py apps.', style = 'Header.TLabel').grid(row = 0, column = 1, padx = 5)
        ttk.Label(self.header_frame, text = 'Gifted to the community, by @thesanjeevsharma', font = ('Arial', 8 )).grid(row = 1, column = 1, padx = 5, sticky = 'n')
        
        
        #Content Frame
        self.content_frame = ttk.Frame(master)
        self.content_frame.pack()

        ##Frame to display installed apps with update functionality
        self.installed_frame = ttk.Frame(self.content_frame)
        self.installed_frame.grid(row = 0, column = 0, rowspan = 2, padx = 5, pady = 5)

        self.tree = ttk.Treeview(self.installed_frame, selectmode = 'browse')
        self.tree.heading('#0', text = 'Installed apps')

        self.tree.grid(row = 0, column = 0, columnspan = 3, sticky = 'ew')

        self.remove_button = ttk.Button(self.installed_frame, text = 'Remove', command = self.remove)
        self.remove_button.grid(row = 1, column = 0)
        self.update_button = ttk.Button(self.installed_frame, text = 'Update', command = self.upgrade)
        self.update_button.grid(row = 1, column = 1)
        self.updateAll_button = ttk.Button(self.installed_frame, text = 'Update All', command = self.upgradeAll)
        self.updateAll_button.grid(row = 1, column = 2)

        ##Frame to download new apps
        self.download_frame = ttk.Frame(self.content_frame)
        self.download_frame.grid(row = 0, column = 1, padx = 5, pady = 5)

        ttk.Label(self.download_frame, text = 'Install new packages').grid(row = 0, column = 0, sticky = 'w')
        
        self.download_entry = ttk.Entry(self.download_frame, width = 30, font = ('Arial', 8))
        self.download_entry.grid(row = 1, column = 0, padx = 5)
        ttk.Button(self.download_frame, text = 'Install', command = self.install).grid(row = 1, column = 1, padx = 5)
        
        ##Frame to display logs
        self.logs_frame = ttk.Frame(self.content_frame)
        self.logs_frame.grid(row = 1, column = 1, padx = 5, pady = 5)

        ttk.Label(self.logs_frame, text = 'Logs').grid(row = 0, column = 0, sticky = 'w')
        
        self.logs = Text(self.logs_frame, height = 10, width = 60, font = ('Courier', 9))
        self.logs.grid(row = 1, column = 0, sticky = 'w')

        #run app
        self.startup()

    def startup(self):
        self.writeToLog('Getting info! Wait.')
        self.checkApps()
        self.writeToLog('Done.')

    def writeToLog(self,msg):
        numlines = int(self.logs.index('end -1 line').split('.')[0])
        self.logs['state'] = 'normal'
        if numlines >= 9:
            self.logs.delete(1.0, 2.0)
        if self.logs.index('end-1c')!='1.0':
            self.logs.insert('end', '\n')
        self.logs.insert('end', msg)
        self.logs['state'] = 'disabled'

    def checkApps(self):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        installed_result = subprocess.run(['pip','list'], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode().split('\n')[2:-1]
        print(installed_result)
        outdated_result = subprocess.run(['pip','list','--outdated'], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode().split('\n')[2:-1]
        self.outdated_apps = []
        for i in range(len(outdated_result)):
            self.outdated_apps.append(outdated_result[i].split(' ')[0])
        for i in range(len(installed_result)):
            package = installed_result[i].split(' ')
            print(package[0])
            if (package[0] in self.outdated_apps):
                self.tree.insert('', 'end', str(package[0]), text = str(package[0]), image = self.notok)
            else:
                self.tree.insert('', 'end', str(package[0]), text = str(package[0]), image = self.ok)
        if len(self.outdated_apps) == 0:
            self.update_button.configure(state = 'disabled')
            self.updateAll_button.configure(state = 'disabled')
        
    def remove(self):
        app = str(self.tree.focus())
        messagebox.askyesno("Remove " + app, "Are You Sure?", icon='warning')
        if 'yes':
            self.writeToLog('Removing ' + app + '! Wait.')
            try:
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                removed_result = subprocess.run(['pip','uninstall',app,'-y'], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode()
                print(removed_result)
                self.writeToLog('Succesfully uninstalled ' + app + '.')
                self.tree.delete(app)
            except:
                self.writeToLog('ERROR! Package not there maybe.')
                
        else:
            pass

    def upgrade(self):
        app = str(self.tree.focus())
        self.writeToLog('Upgrading ' + app + '! Wait.')
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            upgrade_result = subprocess.run(['pip','install',app,'-U'], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode()
            print(upgrade_result)
            self.writeToLog('Succesfully upgraded ' + app + '.')
            index = self.tree.index(app)
            self.tree.delete(app)
            self.tree.insert('', str(index), app, text = app, image = self.ok)
            self.outdated_apps.remove(app)
            if len(self.outdated_apps) == 0:
                self.update_button.configure(state = 'disabled')
                self.updateAll_button.configure(state = 'disabled')
            
        except:
            self.writeToLog('ERROR.')


    def upgradeAll(self):
        for app in self.outdated_apps:
            self.writeToLog('Upgrading ' + app + '! Wait.')
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            upgrade_result = subprocess.run(['pip','install',app,'-U'], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode()
            print(upgrade_result)
            self.writeToLog('Succesfully upgraded ' + app + '.')
            index = self.tree.index(app)
            self.tree.delete(app)
            self.tree.insert('', str(index), app, text = app, image = self.ok)
            self.outdated_apps.remove(app)
            if len(self.outdated_apps) == 0:
                self.update_button.configure(state = 'disabled')
                self.updateAll_button.configure(state = 'disabled')
            
        except:
            self.writeToLog('ERROR.')
            

    def install(self):
        app = self.download_entry.get()
        self.writeToLog('Trying to download ' + app + '.')
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            download_result = subprocess.run(['pip','install',app,], stdout = subprocess.PIPE,startupinfo=startupinfo).stdout.decode()
            print(download_result)
            self.writeToLog('Successfully downloaded ' + app + '.')
            self.download_entry.delete(0, END)
            self.tree.insert('', 'end', app, text = app, image = self.ok)
        except:
            self.writeToLog('ERROR. Not an app or already install.')
            
        
        
def main():            
    
    root = Tk()
    dopepip = Dopepip(root)
    root.mainloop()
    
if __name__ == "__main__": main()
