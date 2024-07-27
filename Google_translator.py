from tkinter import ttk
from tkinter import*
from googletrans import Translator,LANGUAGES

root = Tk()
root.geometry("600x700")
root.title("Translator")
root.configure(background="yellow")


level1 = Label(root,text="Translator",font=("Time New Roman", 40, "bold"),fg="white",bg="black")
level1.place(x=150,y=30)
level2 = Label(root,text="Source Code",font=("Helvetica", 15))
level2.place(x=210,y=100)
sor_word = Text(root,font=("Helvetica", 12), fg="black", bg="lightgrey", height=10, width=60)
sor_word.place(x=20,y=150)



def Translate(text="type",src="en",dest="hi"):
    text1 = text
    sorce1 = src
    dest1 = dest
    gt = Translator()
    rest = gt.translate(text,src=sorce1,dest=dest1)
    return rest.text


def data():
    msg = sor_word.get(1.0, END).strip()
    s = button1.get()
    d = button2.get()
    word = Translate(text=msg,src=s,dest=d)
    des_word.delete(1.0,END)
    des_word.insert(END,word)



lang = list(LANGUAGES.values())

button1 = ttk.Combobox(root, values=lang, font=("Helvetica", 12))
button1.place(x=20,y= 400)
button1.set("english")

button2 = ttk.Combobox(root, values=lang, font=("Helvetica", 12))
button2.place(x=350,y=400)
button2.set("hindi")

button3 = Button(root,text="Translate",command=data,bg="light blue",relief="raised",width=10)
button3.place(x=250,y=400)

des_word = Text(root,font=("Helvetica", 12), fg="black", bg="lightgrey", height=10, width=60)
des_word.place(x=20,y=470)

root.mainloop()