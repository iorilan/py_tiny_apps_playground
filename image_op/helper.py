from PIL import Image
from PIL import ImageColor,ImageFilter
from PIL import ImageDraw, ImageFont
import requests


def show(path):
    Image.open(path).show()

def create_with_color(path, color='blue', size =(300,300)):
    image = Image.new('RGBA',size, color)
    image.save(path)

def create_transparent(path, size=(500,500)):
    image = Image.new('RGBA',size)
    image.save(path)

def crop(file, rect, save_as):
    img = Image.open(file)
    im1 = img.crop(rect)
    im1.save(save_as)

def merge(from_img, into_img, save_as, position):
    img_from = Image.open(from_img)
    img_into = Image.open(into_img).copy()
    img_into.paste(img_from, position)
    img_into.save(save_as)
    

def resize(file_img, percent, save_as):
    img = Image.open(file_img)
    w,h = img.size
    #print(w,h)
    img1 = img.resize((int(w*percent), int(h*percent)))
    img1.save(save_as)

def rotate(file_image, degree, save_as):
    img = Image.open(file_image)
    img2=img.rotate(degree)
    img2.save(save_as)

def flip_horizontal(file_image, save_as):
    img = Image.open(file_image)
    img.transpose(Image.FLIP_LEFT_RIGHT).save(save_as)

def flip_vertical(file_image, save_as):
    img = Image.open(file_image)
    img.transpose(Image.FLIP_TOP_BOTTOM).save(save_as)

def fill_color(file_image,save_as, color='red', left_top=(0,0), width_height=(100,100)):
    img = Image.open(file_image)
    for x in range(width_height[0]):
        for y in range(width_height[1]):
            x1,y1=x+left_top[0],y+left_top[1]
            img.putpixel((x1,y1), ImageColor.getcolor(color, 'RGBA') )
    img.save(save_as)


def watermark(file_image, save_as, text, xy):
    im = Image.open(file_image)
    draw = ImageDraw.Draw(im)
    font=ImageFont.truetype('arial.ttf', size=20)
    draw.text(xy, text, fill='gray', font=font)
    im.save(save_as)


def blur(file_image, save_as):
    im = Image.open(file_image)
    im1 = im.filter(ImageFilter.BLUR)
    im1.save(save_as)

def gray_scale(file_image, save_as):
    im = Image.open(file_image)
    im1 = im.convert('L')
    im1.save(save_as)


def download(url, save_as, format='png'):
    resp = requests.get(url, stream=True).raw
    img = Image.open(resp)
    img.save(save_as, format)

def draw_sample_lines(save_as, size=(500,500), color='white'):
    im = Image.new('RGBA',size,color)
    draw = ImageDraw.Draw(im)
    lines=[(50,50)]
    x=300
    while x>0:
        lines.append((lines[-1][0]+x,lines[-1][1]))
        lines.append((lines[-1][0],lines[-1][1]+x))
        lines.append((lines[-1][0]-x,lines[-1][1]))
        lines.append((lines[-1][0],lines[-1][1]-x))
        x-=20

    draw.line(lines, fill='black')
    im.save(save_as)
def draw_sample_rect(save_as, size=(500,500), color='white'):
    im = Image.new('RGBA',size,color)
    draw = ImageDraw.Draw(im)

    p = [0,0]
    inc=10
    w=10
    color = ['red','blue','green','black','orange']
    for i in range(7):
        print(p,w)
        draw.rectangle((p[0],p[1],p[0]+w,p[1]+w),fill=color[i%5])
        p[0],p[1] = p[0]+inc,p[1]+inc
        w += inc
        inc+=10
    im.save(save_as)

def draw_sample_circle(save_as, size=(500,500), color='white'):
    im = Image.new('RGBA',size,color)
    draw = ImageDraw.Draw(im)
    p = [120,30]
    draw.ellipse((p[0],p[1],160,60), fill='red')
    
    points = [(10,10)]
    step=10
    for i in range(0,10):
        points.append((points[-1][0]+step,points[-1][1]+step))
        points.append((points[-1][0]+step,points[-1][1]-step))
    draw.polygon(points, fill='green')

    im.save(save_as)
    
