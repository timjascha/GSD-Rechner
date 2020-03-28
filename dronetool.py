from guizero import App, Text, TextBox, Combo, PushButton
import math as m

def update():
    if drone.value=="-Custom-":
        resw.value="0"
        resh.value="0"
        sensw.value="0"
        sensh.value="0"
        pcount.value="0"
        psize.value="0"
        fole.value="0"
    elif drone.value=="DJI Inspire 1 - Zenmuse X5":
        resw.value = "4096"
        resh.value = "2160"
        sensw.value = "17.3"
        sensh.value = "13"
        fole.value = "15"

def calcgsd():
    x=float(gsd_v.value)/100
    y=float(fole.value)
    z=float(psize.value)
    fheight=x*y/z
    gsd_h.value=str(fheight)

def pixelsize():
    a = float(sensw.value)
    b = float(sensh.value)
    asens = a * b
    c=float(resh.value)*float(resw.value)
    pcount.value=str(c)
    apixel = asens / c
    pixels = m.sqrt(apixel)
    psize.value = str(pixels)

app = App(title="Drone-Tool", width=550, height=300,layout="grid")
drone_t = Text(app, text="Drone:", grid=[0,0])
drone=Combo(app, options=["-Custom-","DJI Inspire 1 - Zenmuse X5"],grid=[1,0], command=update)
gsd_vt = Text(app, text="Desired GSD", grid=[0,1])
gsd_v = TextBox(app, text="GSD", grid=[1,1])
gsd_ht = Text(app, text="Needed height", grid=[0,2])
gsd_h = TextBox(app, text="height", grid=[1,2])
gsd_c = PushButton(app, text="Calculate flightheight", command=calcgsd, grid=[2,2])
resw_t = Text(app, text="Resolution width", grid=[0,3])
resw = TextBox(app, text="resolution width", grid=[1,3])
resh_t = Text(app, text="Resolution height", grid=[2,3])
resh = TextBox(app, text="resolution height", grid=[3,3])
sensw_t = Text(app, text="Width of Sensor", grid=[0,4])
sensw = TextBox(app, text="width of sensor", grid=[1,4])
sensh_t = Text(app, text="Height of sensor", grid=[2,4])
sensh= TextBox(app,text="height of sensor", grid=[3,4])
fole_t = Text(app, text="focal lenght", grid=[0,5])
fole = TextBox(app, text="focal length", grid=[1,5])
psize_t = Text(app, text="Size of a pixel", grid=[0,6])
psize = TextBox(app, text="size of a pixel", grid=[1,6])
pcount_t = Text(app, text="Count of pixels", grid=[0,7])
pcount = TextBox(app, text="count of pixels", grid=[1,7])
psize_but = PushButton(app, text="calculate size of pixel", command=pixelsize, grid=[2,7])
app.display()