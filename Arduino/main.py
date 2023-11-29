from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello Kivy!')

TestApp().run()


# komendy
# pip install kivy
# pip install buildozer
# python main.py
# buildozer init
# buildozer -v android debug