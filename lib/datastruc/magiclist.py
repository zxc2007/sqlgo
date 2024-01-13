class Magiclist(list):
    def __init__(self):
        super().__init__(self)
    
    def append(self,*args):
        for arg in args:
            super().append(arg)
