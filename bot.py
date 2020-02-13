import random
from termcolor import colored
from simpleeval import simple_eval
import time

class Bot:
    ## Use this class var to set the delay before each 
    wait = 1
    
    def __init__(self):
        self.q = ''
        self.a = ''
    
    def _think(self, s):
        return s
    
    def _say(self, s):
        time.sleep(Bot.wait)
        print(colored(s, 'yellow'))
    
    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))

class HelloBot(Bot):
    
    def __init__(self):
         self.q = 'Hi, What\'s your name?'
    
    def _think(self,s):
        return f'Hi,{s}!'

class GreetingBot(Bot):
    
    def __init__(self):
         self.q = 'How are you today?'
    
    def _think(self,s):
        if 'good' in s:
            return "I'm feeling good too!"
        else:
            return 'Sorry to hear that,'

class FavoriteColorBot(Bot):
    
    def __init__(self):
         self.q = "what's you favorite color?"
    
    def _think(self,s):
        colors = ['red','orange','yellow','green','blue','indigo','purple']
        return f'You like {s}? That is a great color, My favorite color is {random.choice(colors)}. '

class CalcBot(Bot):
    
    def __init__(self):
        self.q = 'Through recent upgrade I can do calculation now, input some arithmetic expression to try.'

    def _think(self, s):
        result = simple_eval(s)
        return f'Done.Result = {result}'



if __name__ == '__main__': 
    h = HelloBot()
    g = GreetingBot() 
    f = FavoriteColorBot() 

    h.run()
    g.run()
    f.run()