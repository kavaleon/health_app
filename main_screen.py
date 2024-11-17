from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import instr


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        img = Image(source='fon.jpg', allow_stretch=True, fit_mode='fill')
        label_title = Label(text=instr.txt_hello, pos_hint={'center_x':0.5, 'center_y':0.5},
                            halign="center", font_size=20, text_size=(instr.win_width, None))
        label = Label(text=instr.txt_instruction, pos_hint={'center_x':0.5, 'center_y':0.5},
                      halign="center", text_size=(instr.win_width, None))
        l1 = BoxLayout(orientation='vertical', size_hint=(0.8, 0.9), pos_hint={'center_x':0.5, 'center_y':0.5})
        button = Button(text=instr.txt_next, size_hint=(.5, 0.1),
                        background_color=(0.9, 0, 0.9, 0.7), pos_hint={'center_x':0.5, 'center_y':0.5})
        l1.add_widget(label_title)
        l1.add_widget(label)
        l1.add_widget(button)
        button.on_press = self.next
        self.add_widget(img)
        self.add_widget(l1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
