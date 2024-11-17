from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from timer_label import TimerLabel
import instr

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        img = Image(source='fon.jpg', allow_stretch=True, fit_mode='fill')
        l1 = BoxLayout(orientation='vertical', size_hint=(0.8, 0.9), pos_hint={'center_x':0.5, 'center_y':0.5})

        self.pop = Popup(title='Ошибка', content=Label(text='Введены неверные символы'),
                         size_hint=(None, None), size=(300, 300))
        self.timer_label = TimerLabel(total=15, text='Запустите таймер', font_size=40)
        self.timer_label.bind(done=self.timer_finish)
        self.label = Label(text=instr.txt_test1, text_size=(instr.win_width, None))
        self.button1 = Button(text=instr.txt_starttest1, size_hint=(.5, 0.1),
                              pos_hint={'center_x':0.5, 'center_y':0.5}, background_color=(0.9, 0, 0.9, 0.7))
        self.line_test = TextInput(text=instr.txt_hinttest1, size_hint=(1, None), height='30sp')
        self.button2 = Button(text='Перейти ко второму тесту', size_hint=(.5, 0.1), pos_hint={'center_x':0.5, 'center_y':0.5},
                                background_color=(0.9, 0, 0.9, 0.7))

        self.button2.set_disabled(True)

        self.button1.on_press = self.timer_label.start
        self.button2.on_press = self.next


        l1.add_widget(self.label)
        l1.add_widget(self.timer_label)
        l1.add_widget(self.button1)
        l1.add_widget(self.line_test)
        l1.add_widget(self.button2)

        self.add_widget(img)
        self.add_widget(l1)

    def timer_finish(self, *args):
        self.button2.set_disabled(False)

    def next(self):
        instr.p1 = self.line_test.text
        if self.line_test.text.isdigit():
            self.manager.transition.direction = 'left'
            self.manager.current = 'third'
        else:
            self.pop.open()