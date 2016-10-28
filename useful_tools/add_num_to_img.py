#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 该小脚本的目的在于实现在图片上添加数字

from PIL import Image,ImageDraw,ImageFont


# 打开一张图片
def add_num_to_img(img):
    draw=ImageDraw.ImageDraw(img)
    myFont=ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor='#ff0000'
    width,height=img.size
    draw.text((width-40,0),'99',font=myFont,fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0

if __name__=="__main__":
    image=Image.open('test.jpg')
    add_num_to_img(image)
