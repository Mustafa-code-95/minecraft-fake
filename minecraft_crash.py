import os
import json
from ursina import Sky
from ursina import Ursina
from ursina import Button
from ursina import color
from ursina import Text
from ursina import held_keys
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import application

app = Ursina()
player = FirstPersonController()
player.position = 2, 20, 2
Sky(texture='sky_sunset')
list = ['der.jpeg', 'retro.png', 'cry.png', 'obs.png', 'glo.jpg', 'bri.jpg', 'red.jpg', 'ingo.png', 'stein1.png', 'stein2.png', 'oo.png', '44.png', 'rt.png', 'buer.jpg', 'ft.png', 'rt.jpg', 'tatata.jpg', 'ste.jpg', 'derr.jpg']
list_draw = ["dirt", "Retro Obsidian", "Crying Obsidian", "Obsidian", "glow stone", "Blackstone", "Redstone", "silver erz", "Stone", "Kobbel Stone", "Nubered hotbar", "Clear Glas", "Glas", "Zigel", "end stone", "wood", "Nether stone", "snow", "Sand"]
d = 0
t = 0
cv = [color.white, color.white66]
wer = []
a = list[d]
ddd = list_draw[d]
boxes = []
g = 1
b_b_text = Text('', origin=(0,7), scale=2)


def save_world():
    world_data = []
    for box in boxes:
        world_data.append({
            'position': list(box.position),
            'texture': box.texture.name if box.texture else None
        })
    with open('world_save.json', 'w') as f:
        json.dump(world_data, f)


def load_world():
    if not os.path.exists('world_save.json'):
        return
    with open('world_save.json', 'r') as f:
        world_data = json.load(f)
    for data in world_data:
        pos = tuple(data['position'])
        tex = data['texture']
        add_box(pos, color=color.white, texture=tex)




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


for ioo in range(2):
    g = ioo + 1
    for ou in range(51):
        x = ou + 1
        for hu in range(51):
            y = hu + 1
            add_box( (x, g, y), color=color.white, texture='ste.jpg')


def update():
    global d, ddd, list_draw
    if held_keys['v']:
        save_world()
    if held_keys['b']:
        load_world()
    if held_keys['c']:
        application.quit()
    if held_keys['m']:
        player.position = 0, 17, 0
    if ((held_keys['l']) or (held_keys['r'])):
        ddd = list_draw[d]
        b_b_text.text = ddd


def input(key):
    global a, d, ddd, cv, t
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                if a == 'tr1.png':
                    t = 1
                else:
                    t = 0
                add_box(box.position + mouse.normal, color=cv[t], texture=a)
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
