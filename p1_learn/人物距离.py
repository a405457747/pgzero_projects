import pgzrun

my2 = Actor("2",(200,100))
animate(my2, pos=(100, 100),duration=3+2);


class MyS(Actor):
    def __init__(self, img,pos, **kwargs):
        image = img;
        super().__init__(image, pos=pos, **kwargs)
        
    def update(self):
        self.x+=1;
        self.y+=1;
my=MyS("1",(100,100));

def draw():
    screen.fill((0, 0, 0))
    my.draw();
    my2.draw();

def update():
    my.update();

def on_mouse_down(pos, button):
    if(button == mouse.LEFT):
        print(my.distance_to(my2));

pgzrun.go()
