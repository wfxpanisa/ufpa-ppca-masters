import gizeh as gz
from math import pi

img_scale = 200
imsz = 12*img_scale
imszx = imsz
imszy = imsz//3

# Create pdf surface
filepath = "/tmp/out.pdf"
s = gz.PDFSurface(filepath, imszx, imszy)

def draw_block(sx=3, sy=8, xdiv=2, ydiv=10, text=""):
    gz.rectangle(
            lx=imszx//sx,
            ly=imszy//sy,
            xy=(imszx//xdiv, imszy//ydiv + 100),
            stroke_width=img_scale//20).draw(s)

    gz.text(
            text,
            fontfamily="Arial",
            fontsize=imsz//26,
            xy=(imszx//xdiv, imszy//ydiv + 100)).draw(s)

def main():
    draw_block(sx=3,    ydiv=8,    text="Registers")
    draw_block(sx=2.7,  ydiv=4,     text="Cache")
    draw_block(sx=2.4,  ydiv=2.666,  text="Main Memory")
    draw_block(sx=2.1,  ydiv=2,  text="Solid-State Drive")
    draw_block(sx=1.8,  ydiv=1.599,  text="Hard Disk")
    draw_block(sx=1.5,  ydiv=1.333, text="Data Cartridge Tape")

    gz.rectangle(
            fill=(0,0,0),
            lx=imszx//60,
            ly=imszy//2,
            xy=(imszx//20, imszy//2)).draw(s)

    gz.regular_polygon(
            imsz//50,
            n=3,
            angle=3*pi/2,
            fill=(0,0,0),
            stroke=(0,0,0),
            stroke_width=3,
            xy = (imszx//20, imszy//4)).draw(s)

    gz.text(
            "Speed",
            fontfamily="Arial",
            fontsize=imsz//30,
            xy=(imszx//6, imszy//4 - 100)).draw(s)

    gz.text(
            "Increases",
            fontfamily="Arial",
            fontsize=imsz//30,
            xy=(imszx//6, imszy//4)).draw(s)


    gz.rectangle(
            fill=(0,0,0),
            lx=imszx//60,
            ly=imszy//2,
            xy=(imszx-imszx//20, imszy//2)).draw(s)

    gz.regular_polygon(
            imsz//50,
            n=3,
            angle=pi/2,
            fill=(0,0,0),
            stroke=(0,0,0),
            stroke_width=3,
            xy = (imszx-imszx//20, imszy-imszy//4)).draw(s)

    gz.text(
            "Size",
            fontfamily="Arial",
            fontsize=imsz//30,
            xy=(imszx - imszx//6, imszy//4 - 100)).draw(s)

    gz.text(
            "Increases",
            fontfamily="Arial",
            fontsize=imsz//30,
            xy=(imszx - imszx//6, imszy//4)).draw(s)

    s.flush()
    s.finish()

if __name__ == '__main__':
    main()
