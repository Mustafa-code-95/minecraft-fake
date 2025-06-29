from ursina import *
points = 0
o = 1
rt = 10
a = ['r.jpg', 'a.png', 'b.png', 'c.png', 'i.png', 'k.png', 'h.png', 'g.png', 'z.png', 'd.png', 'e.png', 'f.png', 'l.png', 'x.png', 'p.png', 'n.png', 'o.png', 'm.png']
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


score_text = Text(f'Points: {points}', position=(-0.85, 0.45), scale=1.5)
b_b_text = Text('', position=(0,0), scale=2, enabled=False)


def update():
    pass


def input(key):
    global points, o, rt, e, background, a
    if key == 'left mouse down':
        b_b_text.text = f"+{o}"
        b_b_text.position = mouse.position
        b_b_text.enabled = True
        points += o
        score_text.text = f'Points: {points}'
    if points > rt:
        rt *= 1.2
        o += 1
        b_b_text.text = f"+{o}"
        if e != len(a)+1:
            e += 1
            background.texture = f"{a[e]}"
        else:
            app.getExitErrorCode()
        score_text.text = f'Points: {points}'


app.run()
