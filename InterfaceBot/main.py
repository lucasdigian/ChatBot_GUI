from tkinter import *
import tkinter.scrolledtext




def Write():

    
    message = f"Usuario: {input_area.get('1.0' , 'end')}"
    if message != '':
        
        input_area.delete('1.0' , 'end')
        text_Area.config(state='normal')
        text_Area.insert('end',message)
        text_Area.yview('end')
        text_Area.config(state='disabled')


tela = Tk()

tela.title('Charles')
tela.iconbitmap('icone.ico')
tela.minsize(width=500, height=500)
tela.resizable(width=False, height=False)
tela.config(bg = 'lightgrey')

text_Area = tkinter.scrolledtext.ScrolledText(tela)
text_Area.pack(padx = 20, pady=5)
text_Area.config(state = 'disabled')

msg_label = tkinter.Label(tela, text='Message: ', bg = 'lightgray')
msg_label.pack(padx=20,pady=5)

input_area = tkinter.Text(tela, height = 3)
input_area.pack(padx=20,pady=5)

button_send = tkinter.Button(tela, text = 'Enviar', command = Write)
button_send.pack(padx = 20,pady = 5)


tela.mainloop()

