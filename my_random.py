# импорт классов
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
import random


Window.size = (300, 690)
Window.title = 'my Random'
Window.clearcolor = (1, 1, 1, 1)

class MenuScreen(Screen):  # класс-наследник
    def __init__(self, **kw):  # конструктор
        super(MenuScreen, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='vertical')
        self.title = 'MyRandom'

        # Указываем, что Label будет занимать всю ширину
        self.main_text = Label(
            text='my RANDOM',
            halign="left",
            color=(0, 0, 0, 1),
            size_hint=(1, None),  # растягиваем по ширине
            height=50,)  # фиксированная высота
        self.main_text.bind(size=self.main_text.setter('text_size'))  # Устанавливаем text_size принудительно

        self.main2_text = Label(text='Категории:', color=(0, 0, 0, 1))
        self.food_button = Button(text='', on_press=lambda x: set_screen('food_screen'), background_normal='food.jpg')
        self.food_text = Label(text='Блюдо', color=(0, 0, 0, 1))
        self.sound_button = Button(text='', background_normal='sound.jpeg', on_press=lambda x: set_screen('sound_screen'))
        self.sound_text = Label(text='Случайный звук', color=(0, 0, 0, 1))
        self.cube_button = Button(text='', background_normal='cube.jpg', on_press=lambda x: set_screen('cube_screen'))
        self.cube_text = Label(text='Бросить кубик', color=(0, 0, 0, 1))
        self.box.add_widget(self.main_text)
        self.box.add_widget(self.main2_text)
        self.box.add_widget(self.food_button)
        self.box.add_widget(self.food_text)
        self.box.add_widget(self.sound_button)
        self.box.add_widget(self.sound_text)
        self.box.add_widget(self.cube_button)
        self.box.add_widget(self.cube_text)
        self.add_widget(self.box)

class Food(Screen):
    def __init__(self, **kw):
        super(Food, self).__init__(**kw)
        self.box = BoxLayout(orientation='vertical')

        # Список блюд для случайного выбора
        self.ch_food = ['Пицца', 'Суши', 'Блины', 'Бургеры']

        # Основной заголовок
        self.main_text = Label(
            text='my RANDOM',
            halign="left",
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=50)
        self.main_text.bind(size=self.main_text.setter('text_size'))
        self.food_main_text = Label(text='Блюдо', color=(0, 0, 0, 1))
        self.image = Image(source='food.jpg')
        self.food_text = Label(text='Блюда:', color=(0, 0, 0, 1))
        self.pizza_text = Label(text='Пицца', color=(0, 0, 0, 1))
        self.sushi_text = Label(text='Суши', color=(0, 0, 0, 1))
        self.pancakes_text = Label(text='Блины', color=(0, 0, 0, 1))
        self.burgers_text = Label(text='Бургеры', color=(0, 0, 0, 1))

        self.random_text = Label(
            text='ВАМ ВЫПАЛО',
            color=(1, 0, 0, 1),
            size_hint=(1, None),
            height=40)

        self.my_ch_button = Button(text='ВЫБРАТЬ БЛЮДО')
        self.my_ch_button.bind(on_press=self.on_button_click)
        self.back_button = Button(text='НАЗАД', on_press=lambda x: set_screen('menu'))

        # Добавляем виджеты в layout
        self.box.add_widget(self.main_text)
        self.box.add_widget(self.food_main_text)
        self.box.add_widget(self.image)
        self.box.add_widget(self.food_text)
        self.box.add_widget(self.pizza_text)
        self.box.add_widget(self.sushi_text)
        self.box.add_widget(self.pancakes_text)
        self.box.add_widget(self.burgers_text)
        self.box.add_widget(self.random_text)
        self.box.add_widget(self.my_ch_button)
        self.box.add_widget(self.back_button)
        self.add_widget(self.box)

    def on_button_click(self, instance):
        # Проверяем, что список блюд не пуст
        if self.ch_food:
            random_food = random.choice(self.ch_food)
            # Обновляем текст существующего Label
            self.random_text.text = f'ВАМ ВЫПАЛО: {random_food}'

class Sound(Screen):
    def __init__(self, **kw):  # конструктор
        super(Sound, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='vertical')

        # список для случайного выбора
        self.ch_sound = ['Смех', 'Крик', 'Плачь', 'Лай']

        # Указываем, что Label будет занимать всю ширину
        self.main_text = Label(
            text='my RANDOM',
            halign="left",
            color=(0, 0, 0, 1),
            size_hint=(1, None),  # растягиваем по ширине
            height=50,)  # фиксированная высота
        self.main_text.bind(size=self.main_text.setter('text_size'))  # Устанавливаем text_size принудительно

        self.sound_main_text = Label(text='Звук', color=(0, 0, 0, 1))
        self.image = Image(source='sound.jpeg')
        self.sound_text = Label(text='Звуки:', color=(0, 0, 0, 1))
        self.sound1_text = Label(text='Смех', color=(0, 0, 0, 1))
        self.sound2_text = Label(text='Крик', color=(0, 0, 0, 1))
        self.sound3_text = Label(text='Плачь', color=(0, 0, 0, 1))
        self.sound4_text = Label(text='Лай', color=(0, 0, 0, 1))

        self.random_text = Label(
            text='ВАМ ВЫПАЛО',
            color=(1, 0, 0, 1),
            size_hint=(1, None),
            height=40)

        self.my_ch_button = Button(text='ВЫБРАТЬ ЗВУК')
        self.my_ch_button.bind(on_press=self.on_button_click)
        self.back_button = Button(text='НАЗАД', on_press=lambda x: set_screen('menu'))
        self.box.add_widget(self.main_text)
        self.box.add_widget(self.sound_main_text)
        self.box.add_widget(self.image)
        self.box.add_widget(self.sound_text)
        self.box.add_widget(self.sound1_text)
        self.box.add_widget(self.sound2_text)
        self.box.add_widget(self.sound3_text)
        self.box.add_widget(self.sound4_text)
        self.box.add_widget(self.random_text)
        self.box.add_widget(self.my_ch_button)
        self.box.add_widget(self.back_button)
        self.add_widget(self.box)

    def on_button_click(self, instance):
        # Проверяем, что список блюд не пуст
        if self.ch_sound:
            random_sound = random.choice(self.ch_sound)
            # Обновляем текст существующего Label
            self.random_text.text = f'ВАМ ВЫПАЛО: {random_sound}'

class Cube(Screen):
    def __init__(self, **kw):  # конструктор
        super(Cube, self).__init__(**kw)  # наследование свойств из супер-класса
        self.box = BoxLayout(orientation='vertical')

        self.ch_num = ['1', '2', '3', '4', '5', '6']

        # Указываем, что Label будет занимать всю ширину
        self.main_text = Label(
            text='my RANDOM',
            halign="left",
            color=(0, 0, 0, 1),
            size_hint=(1, None),  # растягиваем по ширине
            height=50,)  # фиксированная высота
        self.main_text.bind(size=self.main_text.setter('text_size'))  # Устанавливаем text_size принудительно

        self.cube_main_text = Label(text='Бросить кубик', color=(0, 0, 0, 1))
        self.image = Image(source='cube.jpg')
        self.number_text = Label(text='Число:', color=(0, 0, 0, 1))
        self.num1_text = Label(text='1', color=(0, 0, 0, 1))
        self.num2_text = Label(text='2', color=(0, 0, 0, 1))
        self.num3_text = Label(text='3', color=(0, 0, 0, 1))
        self.num4_text = Label(text='4', color=(0, 0, 0, 1))
        self.num5_text = Label(text='5', color=(0, 0, 0, 1))
        self.num6_text = Label(text='6', color=(0, 0, 0, 1))

        self.random_text = Label(
            text='ВАМ ВЫПАЛО',
            color=(1, 0, 0, 1),
            size_hint=(1, None),
            height=40)

        self.my_ch_button = Button(text='БРОСИТЬ КУБИК')
        self.my_ch_button.bind(on_press=self.on_button_click)
        self.back_button = Button(text='НАЗАД', on_press=lambda x: set_screen('menu'))
        self.box.add_widget(self.main_text)
        self.box.add_widget(self.cube_main_text)
        self.box.add_widget(self.image)
        self.box.add_widget(self.number_text)
        self.box.add_widget(self.num1_text)
        self.box.add_widget(self.num2_text)
        self.box.add_widget(self.num3_text)
        self.box.add_widget(self.num4_text)
        self.box.add_widget(self.num5_text)
        self.box.add_widget(self.num6_text)
        self.box.add_widget(self.random_text)
        self.box.add_widget(self.my_ch_button)
        self.box.add_widget(self.back_button)
        self.add_widget(self.box)

    def on_button_click(self, instance):
        # Проверяем, что список блюд не пуст
        if self.ch_num:
            random_num = random.choice(self.ch_num)
            # Обновляем текст существующего Label
            self.random_text.text = f'ВАМ ВЫПАЛО: {random_num}'

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Food(name='food_screen'))
sm.add_widget(Sound(name='sound_screen'))
sm.add_widget(Cube(name='cube_screen'))

class MyApp(App):  # класс-наследник
    # построение программы
    def build(self):
        return sm

MyApp().run()  # запускаем приложение