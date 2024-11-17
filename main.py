from kivy import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import instr
from main_screen import MainScreen
from first_screen import FirstScreen
from second_screen import SecondScreen
from third_screen import ThirdScreen
from fourth_screen import FourthScreen
from final_screen import FinalScreen



class MyApp(App):
    def build(self):

        Config.set('graphics', 'width', instr.win_width)

        Config.set('graphics', 'height', instr.win_height)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FinalScreen(name='final'))
        return sm

if __name__ == '__main__':
    app = MyApp()
    app.run()


