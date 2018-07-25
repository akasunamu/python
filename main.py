from PIL import Image

im = Image.open("1.jpg")
box = {10:0,300:1,410:2,700:3}

region = im.crop(box)
region.save("2.jpg")