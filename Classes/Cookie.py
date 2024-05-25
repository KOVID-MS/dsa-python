class Cookie:
    def __init__(self,color):
        self.color=color

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

cookie_1 =  Cookie('red')
print("Cookie one color is ", cookie_1.getColor())

cookie_1.setColor("blue")
print("Cookie one color is changed", cookie_1.getColor())

