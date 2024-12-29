import tkinter as tk
from tkinter import ttk
import computer


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('900x700')
        self.title('Vitaping')
        self.__create_tabs()


    def __create_tabs(self):
        tab_manager = ttk.Notebook(self)
        tab1 = ttk.Frame(tab_manager)
        tab_manager.add(tab1, text='Ping')
        self.__create_tab1(tab1)
        tab2 = ttk.Frame(tab_manager)
        tab_manager.add(tab2, text='Addresses')
        self.__create_tab2(tab2)
        tab_manager.pack(fill='both')


    def __create_tab1(self, tab):
        ping_all_button = ttk.Button(tab,text='Ping all')
        ping_all_button.grid(row=0, column=0)
        devices = ttk.Treeview(tab, columns=('status', 'name', 'ipv4', 'ipv6', 'ping'), show='headings')
        devices.heading('status', text='Status')
        devices.heading('name', text='Device name')
        devices.heading('ipv4', text='IPv4')
        devices.heading('ipv6', text='IPv6')
        devices.grid(row=1, column=0, columnspan=5)


    def __create_tab2(self, tab):
        def __create_add_window():
            def save_computer():
                comp.name = name_entry.get()
                comp.ipv4 = ipv4_entry.get()
                comp.ipv6 = ipv6_entry.get()
                comp.add()
                name_entry.delete(0, tk.END)
                ipv4_entry.delete(0, tk.END)
                ipv6_entry.delete(0, tk.END)

            add_window = tk.Toplevel(index)
            add_window.geometry('500x200')
            add_window.title('New device')
            name_label = ttk.Label(add_window, text='Device name: ')
            name_label.grid(row=0, column=0)
            name_entry = ttk.Entry(add_window)
            name_entry.grid(row=0, column=1)
            ipv4_label = ttk.Label(add_window, text='IPv4: ')
            ipv4_label.grid(row=1, column=0)
            ipv4_entry = ttk.Entry(add_window)
            ipv4_entry.grid(row=1, column=1)
            ipv6_label = ttk.Label(add_window, text='IPv6')
            ipv6_label.grid(row=2, column=0)
            ipv6_entry = ttk.Entry(add_window)
            ipv6_entry.grid(row=2, column=1)
            save_button = ttk.Button(add_window, text='Save', command=save_computer)
            save_button.grid(row=3, column=0, rowspan=2)

        add_button = ttk.Button(tab, text='+', command=__create_add_window)
        add_button.grid(row=0, column=0)
        add_text = ttk.Label(tab, text='Add new device')
        add_text.grid(row=0, column=1)
        devices = ttk.Treeview(tab, columns=('name', 'ipv4', 'ipv6', 'edit', 'delete'), show='headings')
        devices.heading('name', text='Device name')
        devices.heading('ipv4', text='IPv4')
        devices.heading('ipv6', text='IPv6')
        devices.grid(row=1, column=0, columnspan=5)



if __name__ == '__main__':
    index = Interface()
    comp = computer.Computer()
    index.mainloop()

