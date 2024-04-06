import pgzrun;
a = Actor("alien",(0,0),anchor=("left","top"));
rect = Rect((50, 50), (a.width, a.height))

print(rect);

#anchor=('left', 'bottom')
#a.vy=333;
#print(a.vy);
def draw():
    a.draw();
    screen.draw.rect(rect,(255,255,255))

    screen.draw.filled_circle(a.center,3,(255,0,0))

    screen.draw.text("nihao",(300,300),color=(0,255,0));
    screen.draw.textbox("kkkk",rect);

    screen.blit("alien_hurt",(500,500));
    #screen.draw.rect();
    ...

def on_key_down(key):
    print("key down",key);

def on_key_up(key):
    print("key up",key)

def on_mouse_move(pos,rel):
    #print("move:",pos);
    ...

pgzrun.go();
