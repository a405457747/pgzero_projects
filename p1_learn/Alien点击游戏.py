import pgzrun
import  random;

music.play("handel_mp3")
alien =Actor("alien");
alien.pos=600,600;
alien.is_hurt=False;
print(type(alien.pos));
WIDTH=800;
HEIGHT=800;
TITLE="alien点击游戏"
score=0;
blocks=[];
def createBlock():
    block = Actor("block");
    block.pos = (random.randint(20,800), 20);
    blocks.append(block);
clock.schedule_interval(createBlock,2);
candys=[];
def createCandy():
    c = Actor("tail_hook");
    c.pos = (random.randint(20,800), 20);
    candys.append(c);
clock.schedule_interval(createCandy,2);


#多次点击会重置计时器啊
def animal_normal():
    alien.image="alien";
    alien.is_hurt = False;
    print("点击了alien 要2秒后恢复");

def on_mouse_down(pos,button):
    if(button==mouse.LEFT):
        return;

def on_key_down(key):
    if(key==key.A):
        alien.x-=30;
        print("a");
    elif (key==key.D):
        alien.x+=30;

def shark_animal():
    alien.image="alien";

    return;
    for i in range(6):
        if i%2 ==0:
            alien.hide();
        else:
            alien.show();
            alien.opacity=0.5;

    

def draw():
    screen.fill((255,255,255))
    alien.draw();
    for item in blocks:
        item.draw();
    for item in candys:
        item.draw();
    screen.draw.text("score:"+str(score),(20,20),color=(0,0,0));

def update():
    desList=[];
    for item in blocks:
        item.y+=1;
        if((alien.is_hurt==False) and  alien.collidepoint(item.pos)):
            alien.image="alien_hurt";
            sounds.eep.play();
            alien.is_hurt=True;
            clock.schedule_unique(animal_normal,1);
        if(item.y>=800 and (item not in desList)):
            desList.append(item);


        #item.hide();

    global  score;
    for item in candys:
        item.y+=1;
        if(alien.collidepoint(item.pos) and (item not in desList)):
            score+=1;
            desList.append(item);
            sounds.bol.play();
    for item in desList:
        if(item in blocks):
            blocks.remove(item);
        if(item in candys):
            candys.remove(item);
    ...

pgzrun.go();