from tkinter import *
import morse, cesar, base64

def change_win(id_win):
    global entry, return_label, param, buttons
    [i.destroy() for i in buttons]
    title = Label(win, text="Decode", fg="white", bg="black")
    title.pack()

    Label(win, text="Entrée", fg="white", bg="black").pack()
    entry = Entry(win, fg="white", bg="black")
    entry.pack()

    param_label = Label(win, text="Clé", fg="white", bg="black")
    param = Entry(win, fg="white", bg="black")

    if id_win == 4:
        param_label.pack()
        param.pack()

    enter_button = Button(win, text="Decode", fg="white", bg="black")
    enter_button.pack()

    return_label = Label(win, fg="white", bg="black")
    return_label.pack()

    if id_win == 0:
        title.configure(text="Binaire", fg="white", bg="black")
        enter_button.configure(command=decode_bin)

    elif id_win == 1:
        title.configure(text="Héxadécimal", fg="white", bg="black")
        enter_button.configure(command=decode_hexa)
    
    
    elif id_win == 2:
        title.configure(text="Base64", fg="white", bg="black")
        enter_button.configure(command=decode_base64)

    elif id_win == 3:
        title.configure(text="Morse", fg="white", bg="black")
        enter_button.configure(command=decode_morse)

    else:
        title.configure(text="César", fg="white", bg="black")
        enter_button.configure(command=decode_cesar)


def decode_bin():
    entry_val = entry.get()
    if not entry_val.isdigit():
        return_label.configure(text="Veuillez rentrer un nombre")
        return
    return_label.configure(text=str(int(entry_val, 2)))

def decode_hexa():
    entry_val = entry.get()
    return_label.configure(text=str(int(entry_val, 16)))

def decode_base64():
    entry_val = entry.get()
    return_label.configure(text=base64.b64decode(entry_val))

def decode_morse():
    entry_val = entry.get()
    return_label.configure(text=morse.decode(entry_val))

def decode_cesar():
    entry_val = entry.get()
    entry_param = int(param.get())
    print(entry_val, entry_param)
    return_label.configure(text=cesar.decode(entry_val, entry_param))

def run_decode():
    global win, buttons
    win = Toplevel(bg="black")
    buttons = [ 
        Button(win, text='Binaire', command=lambda:change_win(0), fg="white", bg="black"),
        Button(win, text='Héxadécimal', command=lambda:change_win(1), fg="white", bg="black"),
        Button(win, text='Base64', command=lambda:change_win(2), fg="white", bg="black"),
        Button(win, text='Morse', command=lambda:change_win(3), fg="white", bg="black"),
        Button(win, text='César', command=lambda:change_win(4), fg="white", bg="black")
    ]

    [i.pack() for i in buttons]


    win.mainloop()

if __name__=='__main__':
    run_decode()


""" import tkinter
import tkinter.ttk as ttk

app = tkinter.Tk()
 
app.title("Escape Game")
app.geometry("500x500")
s=ttk.Style()
s.theme_use('clam')

 
def decode_cesar(code):
    shift = 3
 
    code = code.upper()
 
    plain_text = ""
 
    for c in code:
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index - shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        plain_text = plain_text + new_character
    return plain_text

print(decode_cesar("abc"))

 
def action():
    code = entry_input_code.get()
    if not(code.isnumeric()):
        label_error.config(text="Veuillez rentrer un nombre")
        return
 
 
    decode = int(code,2)
    select = listbox.curselection()
    decode = str(select[0]) + str(decode)
    entry_output_code.delete(0, tkinter.END)
    entry_output_code.insert(0,decode)
 
 
 
label_input_code = tkinter.Label(app, text="Entrée")
entry_input_code = tkinter.Entry(app)
 
label_output_code = tkinter.Label(app, text="Sortie")
entry_output_code = tkinter.Entry(app)
 
label_error = tkinter.Label(app, text="", fg="red")
 
button_enter=tkinter.Button(app, text="Entrer", command=action)
 
 
 
values=["Binaire","Héxa", "César"]
 
var = tkinter.Variable(value=values)
 
listbox = tkinter.Listbox(
    app,
    listvariable=var,
    height=6,
    selectmode=tkinter.SINGLE
)
 
 
 
 
 
 
 
 
 
 
 
entry_input_code.place(x=100,y=100)
label_input_code.place(x=0,y=100)
entry_output_code.place(x=150,y=150)
label_output_code.place(x=0,y=150)
label_error.place(x=0,y=300)
button_enter.place(x=0, y=200)

listbox.pack(expand=False)
entry_input_code.pack()
label_input_code.pack()
entry_output_code.pack()
label_output_code.pack()
label_error.pack()
button_enter.pack()



app.mainloop() """