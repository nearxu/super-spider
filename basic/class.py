

class Enemy:
    life = 10
    def attack(self):
        self.life -= 1
    def check(self):
        if(self.life <1):
            print('dead')
        else:
            print('alive')


tom = Enemy()

for _ in range(2):
    tom.attack()
    print(tom.life)

tom.check()

class work:
    def __init__(self):
        print('init function')
    
    def func(self):
        print('func function is use')

ron = work()
ron.func()



