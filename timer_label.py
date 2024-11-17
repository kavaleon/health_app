from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.clock import Clock

'''Clock.schedule_once(function, 2)
Clock.schedule_interval(function, 2)
для остановки функция должна вернуть False'''

class TimerLabel(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        super().__init__(**kwargs)
        self.done = False
        self.total = total
        self.current = total


    def start(self):
        self.current = self.total
        self.done = False
        Clock.schedule_interval(self.label_change, 1)

    def label_change(self, _):
        self.change_color()
        self.text = f'Прошло {self.current} секунд'
        self.current -= 1
        if self.current == -1:
            self.done = True
            return False

    def change_color(self):
        if self.total == 60:
            if self.current == 15:
                self.color = (1, 1, 1)
            if self.current == 45:
                self.color = (0.8, 0, 0.5)