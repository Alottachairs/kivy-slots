from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.graphics import (Rectangle)
from kivy.uix.label import Label
import random as r



icons =     ("assets/icons/apple.png",
    "assets/icons/bar.png",
    "assets/icons/bigwin.png",
    "assets/icons/bonus.png",
    "assets/icons/cherry.png",
    "assets/icons/diamond.png",
    "assets/icons/dollarsign.png",
    "assets/icons/grapes.png",
    "assets/icons/fourleafclover.png",
    "assets/icons/horseshoe.png",
    "assets/icons/mellon.png",
    "assets/icons/orange.png",
    "assets/icons/ruby.png",
    "assets/icons/seven.png",
    "assets/icons/strawberry.png")



class SlotGame(Widget):

    Bank = 1000
    Bet = 10
    def __init__(self, **kwargs):
        super(SlotGame, self).__init__(**kwargs)

        with self.canvas:
             
            self.bet = Label(text = "Bet: $" + str(self.Bet), pos = (200, 500))
            self.bank = Label(text = "Credits: $" + str(self.Bank), pos = (200,450))
            self.display = Label(text = " ", pos = (100, 470))
            self.machine = Rectangle(pos=(0,0), size=(self.width *4, self.height *4 ), source=("assets/slot-machine4.png"))
            self.crank = Rectangle(pos=(0,0), size=(self.width * 4, self.height * 4), source=("assets/slot-machine2.png"))
            self.slotOne = Rectangle(pos = (121, 150), size=(self.width / 2.5, self.height / 2.5), source = (icons[0]))
            self.slotTwo = Rectangle(pos = (181, 150), size=(self.width / 2.5, self.height / 2.5), source = (icons[1]))
            self.slotThree = Rectangle(pos = (245, 150), size=(self.width / 2.5, self.height / 2.5), source = (icons[2]))

    def on_touch_down(self, touch):

        self.crank.source = "assets/slot-machine3.png"
        a = self.slotOne.source = r.choice(icons)
        b = self.slotTwo.source = r.choice(icons)
        c = self.slotThree.source = r.choice(icons)
        SlotGame.pay()
        if a == b == c:
            SlotGame.win()
            self.display.text = 'THREE IN A ROW! YOU WIN!!!'
        else:
            self.display.text = 'You lost ... try again!'
        self.bank.text = "Credits: $" + str(self.Bank)
        #print(a + b + c)


    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        self.crank.source = "assets/slot-machine2.png"
        print("Mouse up", touch)

    @classmethod    
    def pay(cls):     
        cls.Bank -= cls.Bet 

    @classmethod
    def win(cls):
        print("THREE IN A ROW!")
        cls.Bank += cls.Bet * r.randint(7, 20)

class SlotApp(App):
    def build(self):
        game = SlotGame()
        return game
        
if __name__ == '__main__':
    SlotApp().run()
