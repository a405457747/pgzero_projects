import pgzrun
a =Actor("alien",(100,100),anchor=('left', 'top'));
s =a._rect;
print(s);
def draw():
    a.draw();
    ...

pgzrun.go();