from tkinter import *
from pprint import pformat

window = Tk() #New window 
window.title('Favorite digit')
window.geometry('500x500')

text = Text(window, wrap=WORD)
text.pack()


text = Text(width=200, height=100)
text.pack()
text.insert(1.0, "Добро пожаловать!\n\n\n Введите имя человека из списка и узнаете его любимое число\n")
text.tag_add('title', 1.0, '1.end')
text.tag_config('title', justify=CENTER,
                 font=("Times New Romans", 20, 'bold'))

favorite_digits = {
    'Екатерина' : '2',
    'Алексей' : '1',
    'Тимофей' : '3',
    'Сергей' : '5',   
    'Валентина' : '8',
    'Сергей' : '9',
    'Светлана' : '6',
    'Ольга' : '4',
    'Наташа' : '10',
    'Иван' : '7',
    }
text.insert(3.0, pformat(favorite_digits, width=text['width'] ))

window.mainloop()   