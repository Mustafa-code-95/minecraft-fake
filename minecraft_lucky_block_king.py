from ursina import Sky
from ursina import Ursina
from ursina import Text
from ursina import color
from ursina import Button
from ursina import destroy
from ursina import mouse
from ursina import scene
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()
player = FirstPersonController()
eur = 0
liste = ['luck.png', 'wat.jpg']
io = liste[randint(0, 1)]
Sky(texture='sky_sunset')
list = ['retro.png', 'cry.png', 'obs.png', 'glo.jpg', 'bri.jpg', 'red.jpg', 'ingo.png']

noob = ['stein1.png', 'stein2.png', 'rt.png', 'buer.jpg', 'der.jpeg', 'ft.png', 'rt.jpg', 'tatata.jpg', 'ste.jpg', 'derr.jpg']
d = 0
aa = 0
bb = 0
tvee = " "
ui = 0
cc = 0
lucky = []
z = 0
mixes = []
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
player.position = 8, 100, 0


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


def add_mix(position, texture):
    mixes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color.white,
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


n = -21
ccc = -6
for _ in range(20):
    n += 1
    ccc = -6
    for _ in range(27):
        ccc += 1
        add_box(position=(ccc, 0, n), color=color.white, texture='retro.png')


n = -1
for _ in range(150):
    n += 2
    add_lu(position=(15, 1, n), color=color.white)


n = -1
for _ in range(150):
    n += 2
    a = ['mix.png', 'fant.png']
    add_mix(position=(8, 1, n), texture=a[randint(0, 1)])

n = -1
for _ in range(150):
    n += 2
    io = liste[randint(0, 1)]
    add_lucky(position=(1, 1, n), color=color.white, texture=io)


for u in range(300):
    for i in range(3):
        add_box(position=(i+14, 0, u), color=color.white, texture='derr.jpg')

for u in range(300):
    for i in range(3):
        zu = randint(0, len(noob)-1)
        tv = noob[zu]
        add_box(position=(i+7, 0, u), color=color.white, texture=tv)

for u in range(300):
    for i in range(3):
        add_box(position=(i, 0, u), color=color.white, texture='ste.jpg')


def update():
    pass


tv = None


def input(key):
    global a, d, ddd, cv, t, eur, d_text, ur, b_text, noob, tvee, bb, cc, aa, ui, tv
    destroyed_lucks = []
    destroyed_lu = []
    destroyed_mix = []
    for luck in lucky:
        if luck.hovered:
            if key == "left mouse down":
                destroyed_lucks.append(luck)
                eur += 1
                d_text.text = str(f'box:{eur+ui}')
            elif key == "right mouse down" and eur != 0:
                eur -= 1
                a = randint(0, len(list)-1)
                o = list[a]
                t = 1 if o == 'tr1.png' else 0
                add_box(luck.position + mouse.normal, color=cv[t], texture=o)
                d_text.text = str(f'box:{eur+ui}')

    for luck in destroyed_lucks:
        aa += 1
        lucky.remove(luck)
        destroy(luck)

    for mix in mixes:
        if mix.hovered:
            if key == "left mouse down":
                destroyed_mix.append(mix)
                ui += 1
                d_text.text = str(f'box:{eur+ui}')
            elif key == "right mouse down" and ui != 0:
                ui -= 1
                tzeer = randint(0, 2)
                if tzeer == 2:
                    a = randint(0, len(list)-1)
                    tvee = list[a]
                else:
                    zu = randint(0, len(noob)-1)
                    tvee = noob[zu]
                t = 1 if tvee == 'tr1.png' else 0
                add_box(mix.position + mouse.normal, color=cv[t], texture=tvee)
                d_text.text = str(f'box:{eur+ui}')

    for mix in destroyed_mix:
        bb += 1
        mixes.remove(mix)
        destroy(mix)

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
                rtr = randint(1, 20)
                if not rtr == 1:
                    add_box(lu.position + mouse.normal, color=cv[t], texture=o)
                else:
                    a = ['mix.png', 'fant.png']
                    add_mix(lu.position + mouse.normal, texture=a[randint(0, 1)])
                b_text.text = str(f'noob box:{ur}')

    for lu in destroyed_lu:
        cc += 1
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
                d_text.text = str(f'box:{eur+ui}')
            elif key == "right mouse down" and ui != 0:
                ui -= 1
                tzeer = randint(0, 2)
                if tzeer == 2:
                    a = randint(0, len(list)-1)
                    tvee = list[a]
                else:
                    zu = randint(0, len(noob)-1)
                    tvee = noob[zu]
                t = 1 if tvee == 'tr1.png' else 0
                add_box(box.position + mouse.normal, color=cv[t], texture=tvee)
                d_text.text = str(f'box:{eur+ui}')
            elif key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "right mouse down" and ur != 0:
                ur -= 1
                a = randint(0, len(noob)-1)
                o = noob[a]
                t = 1 if o == 'tr1.png' else 0
                rtr = randint(1, 20)
                if not rtr == 1:
                    add_box(box.position + mouse.normal, color=cv[t], texture=o)
                else:
                    a = ['mix.png', 'fant.png']
                    add_mix(box.position + mouse.normal, texture=a[randint(0, 1)])
                b_text.text = str(f'noob box:{ur}')


app.run()
