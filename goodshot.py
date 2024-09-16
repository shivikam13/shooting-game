import pgzrun

WIDTH=500
HEIGHT=500
TITLE="goodshot game"
shrek=Actor("shrek")
message=""
def draw():
  screen.clear()
  screen.fill("pink")
  shrek.draw()
  screen.draw.text(message,center=(250,10))

def on_mouse_down(pos):
  global message
  if shrek.collidepoint(pos):
    message="goodshot" 
  else:
    message="goodluck try again"  
















pgzrun.go()