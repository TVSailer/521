from graph import *
brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
x2 = 300
y2 = 200
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)
obj2 = rectangle(x2, y2, x2+20, y2+20)
px = 5
def update():
  global px
  moveObjectBy(obj, px, 0)
  moveObjectBy(obj2, -px, 0)
  if xCoord(obj) == 380:
    px = -5
    moveObjectBy(obj, px, 20)
    moveObjectBy(obj2, -px, -20)
  if xCoord(obj) == 20:
    px = 5
    moveObjectBy(obj, px, 20)
    moveObjectBy(obj2, -px, -20)

def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()



onKey(keyPressed)
onTimer(update, 50)

run()
