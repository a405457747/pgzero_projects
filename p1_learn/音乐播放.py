import pgzrun
import pygame;

vol =1;
music.set_volume(1);
music.play("handel_mp3")

switch=False;
def on_off():
    global switch;
    switch=not switch;
    if(switch):
        music.pause();
    else:
        music.unpause();

def update():
    ...

def on_mouse_down(pos, button):
    global vol;
    if button == mouse.WHEEL_UP:  # 滚轮向上滚动
        vol+=0.1;
        if(vol>=1):
            vol=1;
        music.set_volume(vol);    
        print("up");
    elif button == mouse.WHEEL_DOWN:  # 滚轮向下滚动
        vol-=0.1;
        if(vol<=0):
            vol=0;
        music.set_volume(vol);    
        print("down");
    elif button ==mouse.LEFT:
        on_off();


pgzrun.go();