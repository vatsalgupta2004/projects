import random

class Colors_collection():
    def __init__(self):
        self.colors_list=[]
        self.color_genertaor()

    def color_genertaor(self):
        self.colors_list
        for i in range(0,100,1):
            a=random.randint(1,255)
            b=random.randint(1,255)
            c=random.randint(1,255)
            self.colors_list.append((a,b,c))
