from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Google Translator")
root.geometry("1080x500")
root.configure(bg="#e0f7fa")  

history = []

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    global language, history
    translator = Translator()
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combo1.get()
        c3 = combo2.get()

        if text_:
            src_lang = None
            dest_lang = None
            for key, value in language.items():
                if value.lower() == c2.lower():
                    src_lang = key
                if value.lower() == c3.lower():
                    dest_lang = key
            
            if src_lang and dest_lang:
                translated = translator.translate(text_, src=src_lang, dest=dest_lang)
                text2.delete(1.0, END)
                text2.insert(END, translated.text)
                
                history.insert(0, f"{text_} ({c2} to {c3}): {translated.text}")
                if len(history) > 5:
                    history.pop()

                update_history_display()
            else:
                messagebox.showerror("Translation Error", "Selected languages are not supported.")
        else:
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
    
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

def update_history_display():
    history_display.config(state=NORMAL)
    history_display.delete(1.0, END)
    for entry in history:
        history_display.insert(END, entry + "\n")
    history_display.config(state=DISABLED)

image_icon = PhotoImage(file="translate.png")
root.iconphoto(False, image_icon)

language = LANGUAGES
languageV = list(language.values())

frame1 = Frame(root, bg="#ffffff", bd=5, relief=RAISED)
frame1.place(x=10, y=20, width=450, height=130)

combo1 = ttk.Combobox(frame1, values=languageV, font="Arial 14", state="readonly")
combo1.place(x=30, y=70)
combo1.set("ENGLISH")

label1 = Label(frame1, text="ENGLISH", font="Arial 24 bold", bg="#ffffff", width=15, bd=5, relief=GROOVE)
label1.place(x=30, y=20)

f = Frame(root, bg="#ffffff", bd=5, relief=RAISED)
f.place(x=10, y=160, width=450, height=240)

text1 = Text(f, font="Arial 16", bg="#f1f8e9", relief=GROOVE, wrap=WORD)  
text1.place(x=0, y=0, width=430, height=230)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame2 = Frame(root, bg="#ffffff", bd=5, relief=RAISED)
frame2.place(x=620, y=20, width=450, height=130)

combo2 = ttk.Combobox(frame2, values=languageV, font="Arial 14", state="readonly")
combo2.place(x=30, y=70)
combo2.set("SELECT LANGUAGE")

label2 = Label(frame2, text="SELECT LANGUAGE", font="Arial 24 bold", bg="#ffffff", width=15, bd=5, relief=GROOVE)
label2.place(x=30, y=20)

f1 = Frame(root, bg="#ffffff", bd=5, relief=RAISED)
f1.place(x=620, y=160, width=450, height=240)

text2 = Text(f1, font="Arial 16", bg="#f1f8e9", relief=GROOVE, wrap=WORD)  
text2.place(x=0, y=0, width=430, height=230)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Translate", font="Arial 14 bold", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=300)


history_frame = Frame(root, bg="#ffffff", bd=5, relief=RAISED)
history_frame.place(x=10, y=410, width=1060, height=80)

history_display = Text(history_frame, font="Arial 12", bg="#ffffff", wrap=WORD, state=DISABLED)
history_display.place(x=0, y=0, width=1040, height=70)

label_change()

root.mainloop()
