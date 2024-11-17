from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

import instr


class FinalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p1 = instr.p1
        self.p2 = instr.p2
        self.p3 = instr.p3
        self.age = instr.age
        self.result()

        img = Image(source='fon.jpg', allow_stretch=True, fit_mode='fill')
        l1 = BoxLayout(orientation='vertical', size_hint=(0.8, 0.9), pos_hint={'center_x':0.5, 'center_y':0.5})

        self.label1 = Label(text=instr.txt_finalwin, text_size=(instr.win_width, None), font_size=30, halign="center")
        self.label2 = Label(text=f'{instr.txt_index}{self.index}', text_size=(instr.win_width, None))
        self.label3 = Label(text=f'{instr.txt_workheart}{self.text}', text_size=(instr.win_width, None))

        l1.add_widget(self.label1)
        l1.add_widget(self.label2)
        l1.add_widget(self.label3)

        self.add_widget(img)
        self.add_widget(l1)

    def result(self):
        self.index = (4 * (int(self.p1) + int(self.p2) + int(self.p3)) - 200)/10
        if int(self.age) >= 15:
            n = 0
            self.take_number(n)
        elif int(self.age) == 13 or int(self.age) == 14:
            n = 1.5
            self.take_number(n)
        elif int(self.age) == 11 or int(self.age) == 12:
            n = 3
            self.take_number(n)
        elif int(self.age) == 9 or int(self.age) == 10:
            n = 4.5
            self.take_number(n)
        elif int(self.age) == 7 or int(self.age) == 8:
            n = 6
            self.take_number(n)
    def take_number(self, n):
        if self.index >= instr.diapason[0] + n:
            self.text = instr.txt_res1
        elif ((self.index >= instr.diapason[1][0] + n) and (self.index < instr.diapason[1][1] + n)):
            self.text = instr.txt_res2
        elif ((self.index >= instr.diapason[2][0] + n) and (self.index < instr.diapason[2][1] + n)):
            self.text = instr.txt_res3
        elif ((self.index >= instr.diapason[3][0] + n) and (self.index < instr.diapason[3][1] + n)):
            self.text = instr.txt_res4
        elif (self.index < instr.diapason[4] + n):
            self.text = instr.txt_res5