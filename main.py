from kivy.app import App
from kivy.uix.widget import Widget

class SlotGame(Widget):

    pass

class SlotApp(App):
    def build(self):
        game = SlotGame()
        return game

if __name__ == '__main__':
    SlotApp().run()