from kivy.animation import Animation
from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class AnimateButton(Button):
    done = BooleanProperty(False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.txt = 0
        self.done = False
        self.animate1 = Animation(pos_hint={'center_x':0.8}, duration=0.75)
        self.animate2 = Animation(pos_hint={'center_x':0.2}, duration=0.75)
        self.animate = self.animate1 + self.animate2
        self.animate.repeat = True
        self.animate.on_progress = self.progr
        self.animate.on_start #запустить функцию перед анимацией


    def progr(self, obj, step):
        if step == 1:
            self.txt += 1
            self.text = str(self.txt)
        if self.txt == 30:
            self.animate.stop(self)
            self.done = True



    def on_press(self):
        print(1)
        self.animate.start(self)

