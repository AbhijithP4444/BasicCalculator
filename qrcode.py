from tkinter import*
import pyqrcode
from PIL import ImageTk,Image

root=Tk()
def generate():
    linkname=name_entry.get()
    link=link_entry.get()
    file_name=linkname+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=6)
    image=ImageTk.PhotoImage(Image.open(file_name))
    imagelabel=Label(image=image)
    imagelabel.image=image
    canvas.create_window(200,450,window=imagelabel)


canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text="QR code generator",fg="blue",font=("Arial",30))
canvas.create_window(200,50,window=app_label)
name_label=Label(root,text="Link Name")
link_label=Label(root,text="link")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)
name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)
but1=Button(root,text="generate link",fg="green",command=generate)
canvas.create_window(200,220,window=but1)
root.mainloop()