import pyglet,serial,numpy,math
IBI = []
ser = serial.Serial('/dev/cu.usbmodem1301', 115200, timeout=1)


window = pyglet.window.Window(1200, 675)
scena = pyglet.image.load('resource/moomin2_bg.jpg')
obraz_duszka = pyglet.image.load('resource/toffle.png')


duszek = pyglet.sprite.Sprite(obraz_duszka, x=50, y=-50)
duszek.dx = 10.0

def biosignal():

    line = ser.readline()  # read a byte
    if line:
        string = line.decode()
        num = int(string)
        IBI.append(num)
        if len(IBI)>2:
            print(hrv(IBI))
        return num

def hrv(data):
    temp = []
    i = 1
    max = len (data)
    while i < max-2:
        temp.append((data[i]-data[i-1])^2)
        i = i + 1
    avg = numpy.mean(temp)
    #hrv = math.sqrt(avg)

    return avg


def update(hrv):
    hrv = biosignal()

    if isinstance(hrv, int):
        duszek.x = hrv





pyglet.clock.schedule_interval(update, 1/60.0)




@window.event
def on_draw():
    window.clear()
    scena.blit(0,0)
    duszek.draw()

pyglet.app.run()

