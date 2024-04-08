import  pgzrun;
hp=100.0;

def hp_line(sc,curHp):
    ratio =curHp/100.0;
    initY=200;
    targetY=280;
    offset =targetY-initY;
    newY =initY+ratio*offset;
    sc.draw.line((220,initY),(220,newY),color=(255,255,255))

def draw():
    screen.fill((0,0,0));
    screen.draw.text("hp",(200,200),color=(255,255,255));
    hp_line(screen,hp);
    ...

def update():
    global hp;
    hp+=0.1;
    ...

pgzrun.go();
