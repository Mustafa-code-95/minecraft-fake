from ursina import color
from ursina import Button
from ursina import application
from ursina import Ursina
from ursina import Entity
from ursina import destroy
from ursina import scene
from ursina import camera
import os


points = 0
buttone = []
o = 1
backe = []
mods = []
backs = []
er = []
tr = 0
tre = 0
rt = 10
buttons = []
buttonss = []
a = ['minecraft.png', '123.jpg']
e = 0
app = Ursina()

camera.orthographic = True
camera.fov = 10

background = Entity(
    model='quad',
    texture=a[e],
    scale=(20, 12),
    z=1
    )


def add_backe():
    backe.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='ko.png',
            scale=(2.7, 1.2),
            position=(0, 4.5)
        )
    )


def add_backs():
    backs.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='back.png',
            scale=(2, 1),
            position=(0, -4.3)
        )
    )


def add_mod():
    mods.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='mods.png',
            scale=(7, 0.7),
            position=(0.4, -1)
        )
    )


def add_er():
    er.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='neu.png',
            scale=(3, 0.6),
            position=(0.1, -2)
        )
    )


def add_buto():
    buttone.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='buto.png',
            scale=(2.7, 1.2),
            position=(0, 3)
        )
    )


def add_buttone():
    buttons.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.1,
            color=color.white,
            texture='sing.png',
            scale=(7, 0.7),
            position=(0.4, 0)
        )
    )


add_er()
add_mod()
add_buttone()


def update():
    pass


def input(key):
    global buttons, background, tr, tre
    for mod in mods:
        if mod.hovered:
            if key == 'left mouse down':
                e = 1
                background.texture = a[e]
                for start in buttons:
                    buttons.remove(start)
                    destroy(start)
                for esc in er:
                    er.remove(esc)
                    destroy(esc)
                tre = 0
                tr = 1
                add_buto()
                add_backe()
                add_backs()
        if tr == 1:
            mods.remove(mod)
            destroy(mod)

    for back in backs:
        if back.hovered:
            if key == 'left mouse down':
                e = 0
                background.texture = a[e]
                for start in buttone:
                    buttone.remove(start)
                    destroy(start)
                for esc in backe:
                    backe.remove(esc)
                    destroy(esc)
                tre = 1
                tr = 0
                add_buttone()
                add_mod()
                add_er()
        if tre == 1:
            backs.remove(back)
            destroy(back)

    for start in buttons:
        if start.hovered:
            if key == 'left mouse down':
                # cwd = os.getcwd()
                os.system('python  "minecraft_crash.py"')
    for ba in backe:
        if ba.hovered:
            if key == 'left mouse down':
                os.system('python  "minecraft_lucky_block_advanter.py"')
    for esc in er:
        if esc.hovered:
            if key == 'left mouse down':
                application.quit()
    for buto in buttone:
        if buto.hovered:
            if key == 'left mouse down':
                os.system('python  "mincraft_lucky_block_battle.py"')


app.run()
