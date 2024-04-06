import pgzrun
a =Actor("alien",(100,100),anchor=('left', 'top'));

print(a._rect,a.topleft,a.midleft);

def draw():
    screen.fill((0,255,0))
    a.draw();
    ...

def addY():
    a.y+=10;

def gg():
    a.x+=10;
    ...

#clock.schedule_interval(gg,1);
def on_key_down(key):
    if(key==keyboard[keys.A]):
        print("aaa");
    #clock.unschedule(gg);

def on_mouse_down(pos,button):
    clock.schedule(addY,1);
def upddate():
    ...

pgzrun.go();