import pgzrun;

my=Actor("my2");

w,h=my.width,my.height;
print(w,h);

score=0;
def draw():
    screen.fill((0,0,0));
    my.draw()
    screen.draw.text("score:"+str(score),(30,30))

def on_mouse_down(pos,button):
    global score;
    if(button==mouse.LEFT):
        score+=1;
        sounds.bol.play();
        print(pos,button,score);

pgzrun.go();