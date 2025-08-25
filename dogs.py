from tkinter import *
import requests #чтобы загружать изображения из интернета
from PIL import Image,ImageTk#чтобы обрабатывать изображения из интернета
from io import BytesIO



window = Tk()
window.title("картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()
