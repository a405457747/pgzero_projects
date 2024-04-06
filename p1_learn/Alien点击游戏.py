import pgzrun

alien =Actor("alien");
alien.pos=200,200;
print(type(alien.pos));
WIDTH=800;
HEIGHT=800;
TITLE="alien点击游戏"

#多次点击会重置计时器啊
def animal_normal():
    alien.image="alien";
    print("点击了alien 要2秒后恢复");

def on_mouse_down(pos,button):
    if(button==mouse.LEFT):
        if(alien.collidepoint(pos)):
            alien.image="alien_hurt";
            sounds.eep.play();
            clock.schedule_unique(animal_normal,2);


def shark_animal():
    for i in range(6):
        if i%2 ==0:
            alien.hide();
        else:
            alien.show();

    

def draw():
    screen.fill((255,255,255))
    alien.draw();


pgzrun.go();