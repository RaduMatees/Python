from graphics import *

def main():
    win = GraphWin('My Rectangle', 300, 300)
    rect = Rectangle(Point(50, 100), Point(250, 200))
    rect.setFill('blue')
    rect.draw(win)
    txt = Text(Point(150, 150), 'Dreptunghi')
    txt.draw(win)

    win.getMouse()
    win.close()

main()