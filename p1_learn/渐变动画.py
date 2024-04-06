import pgzrun
import pygame;
import pgzero;

clock = pygame.time.Clock()
a =Actor("alien",(100,100),anchor=('left', 'top'));
print(type(a._rect));

#animate(a,pos=(300,300),duration=5);

def draw():
    screen.fill((0,0,255))
    a.draw();
    #clock.tick(60);
    ...
def on_key_down(key):
    if key == keys.SPACE:
        print("Space key is pressed!")
        image = a.image
        rect = a.rect
        print("Image:", image)
        print("Rect:", rect)

def on_key_up(key):
    if key == keys.SPACE:
        print("Space key is released!")
def update():
    t =clock.tick();
    #a.x+=(t/1000)*20;
    #print("per t:",t);
    #clock.tick(60);
    ...

pgzrun.go();