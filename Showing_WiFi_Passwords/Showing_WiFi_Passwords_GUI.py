import os
import tkinter as tk
from tkinter import ttk


def get_password():
    script = "netsh wlan show profile > txt.txt"
    os.system(script)

    networks = []
    f = open("txt.txt", "r+")
    for line in f:
        line = line.strip()
        if line.startswith('All'):
            find = line.find(":")
            wifi = line[find+1:].strip()
            networks.append(wifi)
    f.close()
    # print("networks : ", networks)


    folders = []
    for network in networks:
        network_name = network.replace(" ", "_")
        folders.append(f"pass_{network_name}.txt")
        script = f'netsh wlan show profile "{network}" key=clear > pass_{network_name}.txt'
        # print(script)
        os.system(script)
    # print("folders : ", folders)


    passwords = {}
    for fn in folders:
        f = open(fn, "r+")
        for line in f:
            line = line.strip()
            if line.startswith('Key'):
                find = line.find(":")
                password = line[find+1:].strip()
                if password == "1":
                    continue
                # print(password)
                passwords[fn[5:-4]] = password
        f.close()

    print("=====================")
    print(passwords)
    print("=====================")


    script = f"Del txt.txt "
    for folder in folders:
        script+= folder + " "
    os.system(script)

    Add_row(list(passwords.keys()), list(passwords.values()), len(passwords))


# GUI settings : 
window = tk.Tk()
window.title(" كلمات سر الشبكات ")
window.geometry('700x500+200+150')           # we need to update the geometry in Add_row() Function


# Adding title 
title_label = ttk.Label(window, text=" Wi-Fi كلمات سر شبكات  ", font=["bold", 20])           # we need to change the line (Bold and the size and the color ...)
title_label.grid(row=0, column=0, columnspan=4)


def Add_row(name, password, n):
    for i in range(n):
        # Create Labels
        network_name_label = ttk.Label(window, text=name[i], font=["bold", 20])
        network_pass_label = ttk.Label(window, text=password[i], font=["bold", 20])

        # Showing the Labels on the screen
        network_pass_label.grid(row=2+i, column=0)
        network_name_label.grid(row=2+i, column=1)


# Create Labels
network_name_label = ttk.Label(window, text=" اسم الشبكة ", font=["bold", 20])
network_pass_label = ttk.Label(window, text=" كلمة السر ", font=["bold", 20])

# Showing the Labels on the screen
network_pass_label.grid(row=1, column=0)
network_name_label.grid(row=1, column=1)

get_password()

window.mainloop()
