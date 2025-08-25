from email import message_from_string
from tkinter import *
import requests #чтобы загружать изображения из интернета
from PIL import Image,ImageTk#чтобы обрабатывать изображения из интернета
from io import BytesIO
from  tkinter import messagebox as mb
from tkinter import ttk

def show_image():
    image_url = get_dog_image() #получим ссылку на картинку с помощью другой функции
    if image_url:
        try:
            resource = requests.get(image_url,stream=True) #в ответ мы получим из запроса что-то загруженное по этой ссылке
            resource.raise_for_status()#обрабатываем ошибки,получаем статус ответа
            img_data = BytesIO(resource.content)#теперь по этой ссылке загрузили картинку в двоичном коде в переменную
            img = Image.open(img_data) #там картинка
            img_size = (int(width_spinbox.get()),int(height_spinbox.get()))
            img.thumbnail((img_size))# размер подогнали 300 на 300
            img = ImageTk.PhotoImage(img)
            new_window = Toplevel(window)
            new_window.title("случайное изображение")
            lb = ttk.Label(new_window, image=img)
            lb.pack()
            lb.image = img #сборщик мусора чтобы не удалил картинку
        except Exception as e:  # Исправлено: EXCEPTION -> Exception
            mb.showerror ("ошибка",f"возникла ошибка при загрузке изображения {e}")
    progress.stop()

def get_dog_image(): # получить изображение
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random") #вернет json
        response.raise_for_status()
        data = response.json() #лежит ответ в формате json
        return data["message"] #строка с адресом картинки
    except Exception as e:  # Исправлено: EXCEPTION -> Exception
        mb.showerror("ошибка", f"возникла ошибка при запросе к API {e}")
        return None

def prog():
    progress['value'] = 0 #рпустой прогрессбар, равен нулю
    progress.start(30) #увеличивается 1 раз в 30 милисекунд
    window.after(3000, show_image) # ждем 3 секурды и запускаем функцию

window = Tk()
window.title("картинки с собачками")
window.geometry("360x420")

label =ttk.Label(text="Нажмите кнопку для загрузки изображения")  # Добавлен текст
label.pack(pady=10)

button = ttk.Button(text="загрузить изображение", command=prog)
button.pack(pady=10)

progress = ttk.Progressbar (mode="indeterminate",length=300)  # Исправлено: determinate -> indeterminate
progress.pack(pady=10)

# Создаем фрейм для размещения элементов управления размером
frame = Frame(window)
frame.pack(pady=10)

width_label = ttk.Label(frame, text="ширина:")  # Исправлено: добавлен параметр text
width_label.pack(side=LEFT, padx=(10,0))
width_spinbox = ttk.Spinbox(frame, from_=200, to=500, increment=50, width=5)
width_spinbox.set(300)  # Установлено значение по умолчанию
width_spinbox.pack(side=LEFT, padx=(0,10))

height_label = ttk.Label(frame, text="высота")  # Исправлено: добавлен параметр text
height_label.pack(side=LEFT, padx=(10,0))
height_spinbox = ttk.Spinbox(frame, from_=200, to=500, increment=50, width=5)
height_spinbox.set(300)  # Установлено значение по умолчанию
height_spinbox.pack(side=LEFT, padx=(0,10))

window.mainloop()