from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

import instr
from animate_button import AnimateButton
from timer_label import TimerLabel


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        img = Image(source='fon.jpg', allow_stretch=True, fit_mode='fill')
        l1 = BoxLayout(orientation='vertical', size_hint=(0.9, 0.9), pos_hint={'center_x':0.5, 'center_y':0.5})

        self.label = Label(text=instr.txt_test2, halign="left", text_size=(instr.win_width, None))
        self.label2 = Label(text='', halign="center")
        self.button = AnimateButton(text='0', font_size=40, size_hint=(0.4, 0.4),
                                    pos_hint={'center_x': 0.1, 'center_y': 0.1}, background_color=(0.9, 0, 0.9, 0.9))
        self.button1 = Button(text=instr.txt_starttest2, size_hint=(.5, 0.1),
                              pos_hint={'center_x':0.5, 'center_y':0.5}, background_color=(0.9, 0, 0.9, 0.7))
        self.button2 = Button(text='Перейти к третьему тесту', size_hint=(.5, 0.1), pos_hint={'center_x':0.5, 'center_y':0.5},
                                background_color=(0.9, 0, 0.9, 0.7))

        self.button.bind(done=self.animate_finish)
        self.button1.on_press = self.button.on_press
        self.button2.on_press = self.next
        self.button2.set_disabled(True)

        l1.add_widget(self.label)
        l1.add_widget(self.button1)
        l1.add_widget(self.button)
        l1.add_widget(self.button2)

        self.add_widget(img)
        self.add_widget(l1)

    def animate_finish(self, *args):
        self.button2.set_disabled(False)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'