from ursina import Ursina
from ursina import Sky
from ursina import color
from ursina import Text
from ursina import Button
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
app = Ursina()
player = FirstPersonController()
eur = 0
liste = ['luck.png', 'wat.jpg']
io = liste[randint(0, 1)]
player.position = 2, 20, 2
Sky(texture='sky_sunset')
list = ['retro.png', 'cry.png', 'obs.png', 'glo.jpg', 'bri.jpg', 'red.jpg', 'ingo.png']
noob = ['stein1.png', 'stein2.png', 'rt.png', 'buer.jpg', 'der.jpeg', 'ft.png', 'rt.jpg', 'tatata.jpg', 'ste.jpg', 'derr.jpg']
d = 0
lucky = []
z = 0
aaaa = 0
t = 0
n = 0
a = 0
ur = 0
cv = [color.white, color.white66]
wer = []
boxes = []
g = 1
d_text = Text('', origin=(0,-10), scale=1)
b_text = Text('', origin=(0,-11), scale=1)


def add_box(position, color, texture):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position,
            texture=texture
        )
    )


def add_lucky(position, color, texture):
    lucky.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position,
            texture=texture
        )
    )


def add_lu(position, color):
    wer.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position,
            texture='lu.png'
        )
    )


def pro():
    for ui in range(15):
        for u in range(10):
            u += n
            for i in range(10):
                io = liste[randint(0, 1)]
                add_lucky(position=(i, ui, u), color=color.white, texture=io)


def noobi():
    for ui in range(15):
        for u in range(10):
            u += n
            for i in range(10):
                add_lu(position=(i, ui, u), color=color.white)


def update():
    global aaaa, z, wer, lucky, n
    if aaaa == 0:
        for _ in range(2):
            aaaa = 1
            if z == 0:
                noobi()
                z = 1
            else:
                pro()
                z = 0
            n += 20
            player.position = 0, 100, 0


def input(key):
    global a, d, ddd, cv, t, eur, d_text, ur, b_text, noob
    destroyed_lucks = []
    destroyed_lu = []
    for luck in lucky:
        if luck.hovered:
            if key == "left mouse down":
                destroyed_lucks.append(luck)
                eur += 1
                d_text.text = str(f'box:{eur}')
            elif key == "right mouse down" and eur != 0:
                eur -= 1
                a = randint(0, len(list)-1)
                o = list[a]
                t = 1 if o == 'tr1.png' else 0
                add_box(luck.position + mouse.normal, color=cv[t], texture=o)
                d_text.text = str(f'box:{eur}')

    for luck in destroyed_lucks:
        lucky.remove(luck)
        destroy(luck)

    for lu in wer:
        if lu.hovered:
            if key == "left mouse down":
                destroyed_lu.append(lu)
                ur += 1
                b_text.text = str(f'noob box:{ur}')
            elif key == "right mouse down" and ur != 0:
                ur -= 1
                a = randint(0, len(noob)-1)
                o = noob[a]
                t = 1 if o == 'tr1.png' else 0
                add_box(lu.position + mouse.normal, color=cv[t], texture=o)
                b_text.text = str(f'noob box:{ur}')

    for lu in destroyed_lu:
        wer.remove(lu)
        destroy(lu)

    for box in boxes:
        if box.hovered:
            if key == "right mouse down" and eur != 0:
                eur -= 1
                a = randint(0, len(list)-1)
                o = list[a]
                t = 1 if o == 'tr1.png' else 0
                add_box(box.position + mouse.normal, color=cv[t], texture=o)
                d_text.text = str(f'box:{eur}')
            elif key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "right mouse down" and ur != 0:
                ur -= 1
                a = randint(0, len(noob)-1)
                o = noob[a]
                t = 1 if o == 'tr1.png' else 0
                add_box(box.position + mouse.normal, color=cv[t], texture=o)
                b_text.text = str(f'noob box:{ur}')


app.run()
