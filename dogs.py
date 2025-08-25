from email import message_from_string
from tkinter import *
import requests #чтобы загружать изображения из интернета
from PIL import Image,ImageTk#чтобы обрабатывать изображения из интернета
from io import BytesIO
from  tkinter import messagebox as mb

from bottle import response


def show_image():
    image_url = get_dog_image() #получим ссылку на картинку с помощью другой функции
    if image_url:
        try:
            resource = requests.get(image_url,stream=True) #в ответ мы получим из запроса что-то загруженное по этой ссылке
            resource.raise_for_status()#обрабатываем ошибки,получаем статус ответа
            img_data = BytesIO(resource.content)#теперь по этой ссылке загрузили картинку в двоичном коде в переменную
            img = Image.open(img_data) #там картинка
            img.thumbnail((300,300))# размер подогнали 300 на 300
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img #сборщик мусора чтобы не удалил картинку
        except EXCEPTION as e:
            mb.showerror ("ошибка",f"возникла ошибка при загрузке изображения {e}")


def get_dog_image(): # получить изображение
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random") #вернет json
        response.raise_for_status()
        data = response.json() #лежит ответ в формате json
        return data("message") #строка с адресом картинки
    except EXCEPTION as e:
        mb.showerror("ошибка", f"возникла ошибка при запросе к API {e}")
        return None



window = Tk()
window.title("картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()
