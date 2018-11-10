from random import randint


class Die():
    """创建一个色子类"""
    def __init__(self,sides=6):
        """初始化色子的属性"""
        self.sides=sides
    def roll(self):
        """掷色子"""
        return randint(1,self.sides)