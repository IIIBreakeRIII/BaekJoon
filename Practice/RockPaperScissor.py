import random
import threading
 
RPS = ['Rock', 'Paper', 'Scissor']
 
def startTimer():
    print(random.choice(RPS))
    timer = threading.Timer(1, startTimer)
    timer.start()
 
if __name__ == '__main__':
    startTimer()