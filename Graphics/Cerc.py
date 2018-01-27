from graphics import *

def main():
    win = GraphWin("Cercul meu", 600, 600)
    c = Circle(Point(300, 300), 150)
    c.setOutline('red')
    c.draw(win)
    x = Point(300, 150)
    y = Point(300, 450)
    d = Line(x, y)
    d.setOutline('blue')
    x1 = Point(150, 300)
    y1 = Point(450, 300)
    d1 = Line(x1, y1)
    d1.setOutline('blue')
    m = Point(100, 100)
    f = Text(Point(300, 100), 'Un cerc')
    f.draw(win)
    d.draw(win)
    d1.draw(win)
    win.getMouse()
    win.close()

main()