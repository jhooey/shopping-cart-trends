import Tkinter as tk
import ttk

class Root(tk.Tk):
    """Container for all frames within the application"""
    
    def __init__(self, session_user, session, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #initialize menu
        self.config(menu=MenuBar(self))
        
        self.appFrame = Application(self)
        self.appFrame.pack(side='top', fill='both', expand='True')
        
        self.status = StatusBar(self)
        self.status.pack(side='bottom', fill='x')
        
class MenuBar(tk.Menu):
    def __init__(self, root):
        tk.Menu.__init__(self, root)

        self.root = root

        filemenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=filemenu)
        filemenu.add_command(
                             label="New Receipt", 
                             command=self.select_add_receipt
                             )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, command=self.quit)

        helpmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)

    def quit(self):
        sys.exit(0)
    
    def callback(self):
        print "called the callback!"
        
    def select_add_receipt(self):
        self.root.appFrame.select(self.root.appFrame.add_Receipt)

class StatusBar(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.label = ttk.Label(self, relief='sunken', anchor='w')
        self.label.pack(fill='x')

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

            
class Application(ttk.Notebook):
    def __init__(self, root):
        ttk.Notebook.__init__(self, root, width=200, height=200)
        
        self.dashboard = ttk.Frame(self)
        self.receipts = ttk.Frame(self)
        self.stores = ttk.Frame(self)
        self.categories = ttk.Frame(self)
        self.add_Receipt = ttk.Frame(self)
        
        
        self.add(self.dashboard, text = "Dashboard")
        self.add(self.receipts, text = "My Receipts")
        self.add(self.stores, text = "Stores")
        self.add(self.categories, text = "Categories")
        self.add(self.add_Receipt, text = "Add Receipt")

class Dashboard(tk.Canvas):
    def __init__(self):
        pass