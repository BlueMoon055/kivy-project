# импорт классов
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window


Window.size = (300, 690)
Window.title = 'my Random'
Window.clearcolor = (1, 1, 1, 1)

class MenuScreen(Screen):  # класс-наследник
    def __init__(self, **kw):  # конструктор
        super(MenuScreen, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='vertical')

        # Указываем, что Label будет занимать всю ширину
        self.main_text = Label(
            text='my RANDOM',
            halign="left",
            color=(0, 0, 0, 1),
            size_hint=(1, None),  # растягиваем по ширине
            height=50,)  # фиксированная высота

        self.main_text.bind(size=self.main_text.setter('text_size'))  # Устанавливаем text_size принудительно
        # Растягиваем картинку на всю ширину

        self.food_button = Button(text='', background_normal='food.jpg')
        self.food_text = Label(text='Блюдо', color=(0, 0, 0, 1))
        self.sound_button = Button(text='', background_normal='sound.jpeg')
        self.sound_text = Label(text='Случайный звук', color=(0, 0, 0, 1))
        self.cube_button = Button(text='', background_normal='cube.jpg')
        self.cube_text = Label(text='Бросить кубик', color=(0, 0, 0, 1))
        self.box.add_widget(self.main_text)
        self.box.add_widget(self.food_button)
        self.box.add_widget(self.food_text)
        self.box.add_widget(self.sound_button)
        self.box.add_widget(self.sound_text)
        self.box.add_widget(self.cube_button)
        self.box.add_widget(self.cube_text)
        self.add_widget(self.box)

sm = ScreenManager()
sm.add_widget(MenuScreen())

class MyApp(App):  # класс-наследник
    # построение программы
    def build(self):
        return sm

MyApp().run()  # запускаем приложение