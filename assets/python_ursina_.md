# Python easy game engine 2D and 3D lerning German
  
*ursina game engine for easy lerning!*
  
*Python3*
  
## Info
  
Um ursina zu lernen solltest du dich mit Python gut aus kennen.
  
Diese Programme benutzen alle kein `class`.
  
Du brauchst ein `python-env` und ein Debian oder Ubuntu PC.
  
## Info zum Starten des Programms aus dem Terminal
  
Debian/Ubuntu
  
*python-env*
  
**Um aus ein ordner raus zugehen musste diesen command benutzen:**
  
```bash
cd ..
```
  
**Um in ein ordner rein zugehen verwendest du diesen commmand:**
  
```bash
cd Der_ordner_wo_rein_willst
```
  
**Umdein Programm zu runen verwändest du diesen command:**
  
```bash
python3 dateiname.py
```
  
## Ursina installation
  
Debian/Ubuntu
  
*python-env*
  
**Terminal command:**
  
```bash
pip install panda3d
```
  
**Terminal command:**
  
```bash
pip install ursina
```
  
**Terminal command:**
  
```bash
pip install ursina packages
```
  
### Fehler?
  
Falls du kein Problem bei der Installation hattest kannst du diesen Teil überspringen!
  
Debian/Ubuntu
  
*python-env*
  
**Terminal command:**
  
```bash
sudo apt install pip
```
  
**Terminal command:**
  
```bash
sudo apt upgrade pip
```
  
**Terminal commmand:**
  
```bash
pip install panda3d
```
  
**Terminal commmand:**
  
```bash
pip install ursina
```
  
**Terminal command:**
  
```bash
pip install ursina packages
```
  
## Ursina`s Geschichte
  
Die `Ursina` Engine wurde ab ca. **2019** vom Entwickler **@pokepetter** *ein norwegischer Entwickler* ins Leben gerufen. Ziel war es, eine einfache und leicht zugängliche **`3D-Game-Engine`** in **`Python`** zu schaffen. Die Engine sollte auch für Einsteiger geeignet sein und die Erstellung von **`3D-Games`** mit minimalem Code ermöglichen.
  
## Mit ursina Minecraft
  
Ursina importieren!
  
```python
from ursina import *
```
  
So importierst du ursina.Jetzt willst du natürlich wissen wie man ein bildschirm auf machen kann!
  
```python
from ursina import Ursina
  
app = Ursina()
  
app.run()
  
```
  
Gerade ist der Bild schirm noch grau doch mit einem ganz kurzem befehl krigt man auch einen himmel!
  
```python
from ursina import Ursina
from ursina import Sky
  
app = Ursina()
Sky()
  
app.run()
  
```
  
Jetzt hast du schon ein Tages Himmmel.Wenn du ein Sonnen untergang haben willst musst du noch etwas kleines hinzufügen!
  
```python
from ursina import Ursina
from ursina import Sky
  
app = Ursina()
Sky(texture="sky_sunset")
  
app.run()
  
```
  
Du hast jetzt eine Sonnen untergang texture.Doch du brauchst noch ein player den du leicht importieren kannst.
  
```python
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina
from ursina import Sky
  
app = Ursina()
player = FirstPersonController
Sky(texture='sky_sunset')
  
app.run()
  
```
  
Nun hast du auch den player importiert.Du brauchst die bewegungen nicht zu definieren nachmlich die wurden auch importiert.
  
Jetzt kommen wir zum schwierigen teil die Blöcke die in ursina cube gennant werden.
  
```python
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina
from ursina import Button
from ursina import Sky
from ursina import scene
  
app = Ursina()
player = FirstPersonController
boxes = []
Sky(texture='sky_sunset')
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene, #ursina muss wissen wo man die box sieht
            model='cube',
            origin=0.5,
            color=color,
            position=position,
        )
    )
  
  
app.run()
  
```
  
Jetzt sieht der code nicht so bunt aus aber bei Vs code oder Neovim schon.Hier habe ich eine erklärungs Zeile geschriben die mit # anfängt die brauchst du nicht.Gerade fällst du immer noch also muss unter dir eine plate sein die wir jetzt machen
  
```python
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina
from ursina import Button
from ursina import Sky
from ursina import color
from ursina import scene
  
app = Ursina()
player = FirstPersonController
boxes = []
Sky(texture='sky_sunset')
player.position = 3, 20, 3
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position
        )
    )
  
  
for u in range(20):
    for ui in range(20):
        add_box(positon=(u, 0, ui), color=color.green)
  
app.run()
  
```
  
Es kann sein das du nach den fall in einer box bags du musst nur 2/3 mal auf Space drücken, das sind nur 33 Zeile.
  
Nun fehlen zwei sachen plazieren und abauen hier braucht man zwei sachen `def update():` und `def input(key):`.Fangen wir mit update das werden wir nicht benötigen, trotzdem will ich das euch erklären `def update():` ist kein normaler def, was du in update rein schreibst wider holt sich vortlaufent bis das programm gestoppt wird wie eine `while True` schleife und input ist das gleiche in kommplizierter.Weil wir update nicht benötigen müssen wir nicht viel darein screiben.
  
```python
from ursina import Sky
from ursina import Ursina
from ursina import Button
from ursina import color
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina.prefabs.first_person_controller import FirstPersonController
  
app = Ursina()
player = FirstPersonController()
player.position = 2, 20, 2
Sky(texture='sky_sunset')
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position
        )
    )
  
for u in range(20):
    for ui in range(20):
        add_box(positon=(u, 0, ui), color=color.green)
  
  
def update():
    pass
  
def input(key):
    global a, d, ddd, cv, t
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, color=color.gray)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
  
app.run()
  
```
  
Jetzt hast du schwierig keiten beim zumachen des programmes, aber natürlich habe ich auch dafür eine lösung.
  
```python
from ursina import Sky
from ursina import Ursina
from ursina import Button
from ursina import color
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina import held_keys
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import application
  
app = Ursina()
player = FirstPersonController()
player.position = 2, 20, 2
Sky(texture='sky_sunset')
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position
        )
    )
  
for u in range(20):
    for ui in range(20):
        add_box(positon=(u, 0, ui), color=color.green)
  
  
def update():
    if held_keys['c']:
        application.quit()
  
def input(key):
    global a, d, ddd, cv, t
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, color=color.gray)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
  
app.run()
  
```
  
Wenn du c drückst schließt das programm sich von allein.Wenn du willst das man die farbe der box die man plaziert wechseln kann musst zwei listen definieren, dafür musst du text importieren das geht so:
  
```python
from ursina import Text
```
  
So kannst du text importieren.Das programm sieht aktuell so aus:
  
```python
from ursina import Sky
from ursina import Ursina
from ursina import Button
from ursina import color
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina import held_keys
from ursina import Text
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import application
  
app = Ursina()
player = FirstPersonController()
Sky(texture='sky_sunset')
list = [color.red, color.green, color.white, color.black,
    color.gray, color.blue, color.brown]
list_draw = ["red", "green", "white", "black", "gray", "blue", "brown"]
d = 0
a = list[d]
ddd = list_draw[d]
b_b = False
boxes = []
g = 1
b_b_text = Text('', origin=(0,7), scale=2)
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position
        )
    )
  
for _ in range(2):
    g -= 1
    for x in range(51):
        for y in range(51):
            add_box( (x, g, y), color=color.green)
  
  
def update():
    if ((held_keys['l']) or (held_keys['r'])):
        ddd = list_draw[d]
        b_b_text.text = ddd
    if held_keys['c']:
        application.quit()
  
  
def input(key):
    global a, d
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, color=a)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "l":
                if d == 0:
                    d = 6
                else:
                    d -= 1
                a = list[d]
                ddd = list_draw[d]
            if key == "r":
                if d == 6:
                    d = 0
                else:
                    d += 1
                a = list[d]
                ddd = list_draw[d]
  
  
app.run()
  
```
  
Jetzt brauchst du ein respawn point wo du mit einen Button hin kannst *zum beispiel* ich benutze `m` als Button.Jetzt fangen wir mal mit der andärung an.
  
```python
from ursina import Sky
from ursina import Ursina
from ursina import Button
from ursina import color
from ursina import destroy
from ursina import scene
from ursina import mouse
from ursina import held_keys
from ursina import Text
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import application
  
app = Ursina()
player = FirstPersonController()
Sky(texture='sky_sunset')
list = [color.red, color.green, color.white, color.black,
    color.gray, color.blue, color.brown]
list_draw = ["red", "green", "white", "black", "gray", "blue", "brown"]
d = 0
a = list[d]
ddd = list_draw[d]
b_b = False
boxes = []
g = 1
b_b_text = Text('', origin=(0,7), scale=2)
  
  
def add_box(position, color):
    boxes.append(
        Button(
            parent=scene,
            model='cube',
            origin=0.5,
            color=color,
            position=position
        )
    )
  
for _ in range(2):
    g -= 1
    for x in range(51):
        for y in range(51):
            add_box( (x, g, y), color=color.green)
  
  
def update():
    if ((held_keys['l']) or (held_keys['r'])):
        ddd = list_draw[d]
        b_b_text.text = ddd
    if held_keys['c']:
        application.quit()
    if held_keys['m']:
        player.position = 15, 100, 15
  
  
def input(key):
    global a, d
    for box in boxes:
        if box.hovered:
            if key == "right mouse down":
                add_box(box.position + mouse.normal, color=a)
            if key == "left mouse down":
                boxes.remove(box)
                destroy(box)
            if key == "l":
                if d == 0:
                    d = 6
                else:
                    d -= 1
                a = list[d]
                ddd = list_draw[d]
            if key == "r":
                if d == 6:
                    d = 0
                else:
                    d += 1
                a = list[d]
                ddd = list_draw[d]
  
  
app.run()
  
```
  
Jetzt kanns sein das du nach dem sturz in einem Block bags um raus aus dem Block zu kommen musst du 2/3 mal space drücken.Jetzt kannst du das ganze mit texturen machen!
  
Here is programm with textures:
  
```python
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
list = ['der.jpeg', 'retro.png', 'cry.png', 'obs.png', 'glo.jpg', 
    'bri.jpg', 'red.jpg', 'ingo.png', 'stein1.png', 'stein2.png',
    'tr1.png', 'buer.jpg', 'ft.png', 'rt.jpg',
    'tatata.jpg', 'ste.jpg', 'derr.jpg']
list_draw = ["dirt", "Retro Obsidian", "Crying Obsidian",
    "Obsidian", "glow stone", "Blackstone", "Redstone", "silver erz",
    "Stone", "Kobbel Stone", "Glas", "Zigel",
    "end stone", "wood", "Nether stone", "snow", "Sand"]
d = 0
t = 0
cv = [color.white, color.white66]
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
  
  
for ioo in range(2):
    g = ioo + 1
    for ou in range(51):
        x = ou + 1
        for hu in range(51):
            y = hu + 1
            add_box( (x, g, y), color=color.white, texture='ste.jpg')
  
  
def update():
    global d, ddd, list_draw
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
  
```
  
Die pngs/jpgs/jpegs musst du dir selber ausem internet raussuchen ein beispiel:
  
`minecraft Blockname texture`
  
So kannst du dir die images rausuchen und du musst meine image namen zu deinen tauschen.Dieses programm hat 2 Monate gedauert also unterschätze es nicht.Man kann Grass nicht anwenden, weil er mehr als 1 image verfügt.
  
Jetzt erstelle ein neue python datei ich habe diese datei **`Lucky_block_battle.py`** genannt aber du kannst sie auch anders nennen nähmlich jetzt definieren wir `add_Lucky`.Das andere programm kannst du mit copy(Ctrl+C) und paste(Ctrl+V) in dieses programm copieren.Nun müssen wir das programm ein bissche.
  