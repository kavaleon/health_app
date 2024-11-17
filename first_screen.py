from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import instr

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        img = Image(source='fon.jpg', allow_stretch=True, fit_mode='fill')
        l1 = BoxLayout(orientation='vertical', size_hint=(0.8, 0.9), pos_hint={'center_x':0.5, 'center_y':0.5})

        self.pop = Popup(title='Ошибка', content=Label(text='Ваш возраст не подходит'),
                        size_hint=(None, None), size=(300, 300))
        self.label1 = Label(text=instr.txt_name)
        self.line_fio = TextInput(text=instr.txt_hintname, size_hint=(1, None), height='40sp')
        self.label2 = Label(text=instr.txt_age)
        self.line_age = TextInput(text=instr.txt_hintage, size_hint=(1, None), height='40sp')
        self.button = Button(text='Начать тестирование', size_hint=(.5, 0.1),
                        background_color=(0.9, 0, 0.9, 0.7), pos_hint={'center_x':0.5, 'center_y':0.5})

        self.button.on_press = self.next

        l1.add_widget(self.label1)
        l1.add_widget(self.line_fio)
        l1.add_widget(self.label2)
        l1.add_widget(self.line_age)
        l1.add_widget(self.button)

        self.add_widget(img)
        self.add_widget(l1)

    def next(self):
        instr.age = self.line_age.text
        if self.line_age.text.isdigit():
            if int(self.line_age.text) > 7 and int(self.line_age.text) < 99:
                self.manager.transition.direction = 'left'
                self.manager.current = 'second'
            else:
                self.pop.open()
        else:
            self.pop.content = Label(text='Введены неверные символы')
            self.pop.open()

