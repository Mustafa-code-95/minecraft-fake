from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
player.position = 2, 10, 2
Sky()
list = ['der.jpeg', 'retro.png', 'cry.png', 'obs.png', 'glo.jpg', 'bri.jpg', 'red.jpg', 'ingo.png', 'stein1.png', 'stein2.png', 'buer.jpg', 'rt.png', 'ft.png', 'rt.jpg', 'tatata.jpg', 'ste.jpg', 'derr.jpg']
list_draw = ["dirt", "Retro Obsidian", "Crying Obsidian", "Obsidian", "glow stone", "Blackstone", "Redstone", "silver erz", "Stone", "Kobbel Stone", "Zigel", "Glas", "end stone", "wood", "Nether stone", "snow", "Sand"]
d = 0
wer = []
a = list[d]
ddd = list_draw[d]
boxes = []
g = 1
b_b_text = Text('', origin=(0,7), scale=2)


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


def add_bed(position):
    wer.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color.white,
            position=position,
            texture='bed.jpg'
        )
    )


for ioo in range(7):
    g = ioo + 1
    for ou in range(18):
        x = ou + 1
        for hu in range(18):
            y = hu + 1
            add_box(position=(x, g, y), color=color.white, texture='ste.jpg')

for oi in range(21):
    for oio in range(21):
        add_bed(position=(oi, oio, 0))
        add_bed(position=(oi, oio, 19))
        add_bed(position=(0, oi, oio))
        add_bed(position=(19, oi, oio))
        add_bed(position=(oi, 0, oio))
        add_bed(position=(oi, 21, oio))


def update():
    global d, ddd, list_draw
    if ((held_keys['l']) or (held_keys['r'])):
        ddd = list_draw[d]
        b_b_text.text = ddd


def input(key):
    global a, d, ddd
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, color=color.white, texture=a)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
    if key == "l":
        if d == 0:
            d = len(list)-1
        else:
            d -= 1
        a = list[d]
    if key == "r":
        if d == len(list)-1:
            d = 0
        else:
            d += 1
        a = list[d]


app.run()
