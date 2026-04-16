# импорт классов
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

class MenuScreen(Screen):  # класс-наследник
    def __init__(self, **kw):  # конструктор
        super(MenuScreen, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='horizontal')  # создаём горизонтальную направляющую линию
        self.box.add_widget(Button(text='Кошки', on_press=lambda x: set_screen('left_screen')))  # создаём кнопку (левую)
        self.box.add_widget(Button(text='Собаки', on_press=lambda x: set_screen('right_screen')))  # создаём кнопку (правую)
        self.add_widget(self.box)  # добавляем виджеты на линию

class Left(Screen):  # класс-наследник
    def __init__(self, **kw):  # конструктор
        super(Left, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='horizontal')  # создаём горизонтальную направляющую линию
        back_button = Button(text='Назад в меню', on_press=lambda x: set_screen('menu'))  # создаём кнопку
        self.image = Image(source='cat.jpeg')  # загружаем изображение
        # добавляем виджеты на линию
        self.box.add_widget(back_button)
        self.box.add_widget(self.image)
        self.add_widget(self.box)

class Right(Screen):  # класс-наследник
    def __init__(self, **kw):  # конструктор
        super(Right, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='horizontal')  # создаём горизонтальную направляющую линию
        back_button = Button(text='Назад в меню', on_press=lambda x: set_screen('menu'))  # создаём кнопку
        self.image = Image(source='dog.png')  # загружаем изображение
        # добавляем виджеты на линию
        self.box.add_widget(back_button)
        self.box.add_widget(self.image)
        self.add_widget(self.box)

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()  # добавляем переключение между экранами
# добавляем виджеты
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Left(name='left_screen'))
sm.add_widget(Right(name='right_screen'))

class MyApp(App):  # класс-наследник
    # построение программы
    def build(self):
        return sm

MyApp().run()  # запускаем приложение