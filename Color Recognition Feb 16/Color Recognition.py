from PIL import Image, ImageDraw
import os
import math

def jump(distance):
    press_time = distance * 1.36
    press_time = int(press_time)
    cmd = 'adb shell input swipe 1000 420 1000 420 ' + str(press_time)
    os.system(cmd)

#intialize adb, get screenshot, save it to computer, then delete it from the phone        
os.system('adb version')
os.system('adb shell screencap -p /sdcard/adbscreenshot/screenshot.png')
os.system('adb pull /sdcard/adbscreenshot/screenshot.png C:\Bruce\screenshotsaver\screenshot.png')
os.system('adb shell rm /sdcard/adbscreenshot/screenshot.png')

im = Image.open("C:\Bruce\screenshotsaver\screenshot.png")
#load the image from the computer
im_pixel = im.load()
width, height = im.size
draw = ImageDraw.Draw(im)

#   variables
#   chess(x,y)
c_x = 0
c_y = 0
#   platform(x,y)
p_x = 0
p_y = 0
up_p_x = 0
up_p_y = 0
down_p_x = 0
down_p_y = 0
#   sum of chess(x,y)and number of pixels(x,y)
sum_c_x = 0
sum_c_y = 0
count_c_x = 0
count_c_y = 0
#   sum of platform(x,y)and number of pixels(x,y)
sum_p_x = 0
sum_p_y = 0
count_p_x = 0
count_p_y = 0

#   scan for possible area of chess piece
for i in range(width):
    for j in range(height):
        pixel = im_pixel[i, j]
        if (50 < pixel[0] < 60) and (53 < pixel[1] < 63) and (95 < pixel[2] < 110): #find the bottom of the chess piece, a special color, then paint it yellow during testing
            draw.ellipse((i, j, i, j), fill=(255, 255, 0))
            sum_c_x += i   #sum of the coordinates, used later to find the center
            count_c_x += 1
            sum_c_y += j
            count_c_y += 1

#   calculate chess(x,y)
c_x = sum_c_x // count_c_x
c_y = sum_c_y // count_c_y
 
#   scan for possible area of next plaform
#   narrow the search of area to left or right side of the screen
if c_x < (width/2):
    border_x_s = c_x
    border_x_e = width
else:
    border_x_s = 0
    border_x_e = c_x
#  find the top pixel[x,y] of the next platform 
for j in range(int(height/3),int(height*2/3)): #search middle third of the screen
    test_pixel_l = im_pixel[0,j]
    #test_pixel_r = im_pixel[width-1,j]
    if p_x != 0 or p_y != 0:
        break
    for i in range(int(border_x_s),int(border_x_e)):
        pixel = im_pixel[i,j]
        if abs(i - c_x) < 102:
            continue
        #if abs(2*pixel[0] - test_pixel_l[0] - test_pixel_r[0]) + abs(2*pixel[1] - test_pixel_l[1] - test_pixel_r[1]) + abs(2*pixel[2] - test_pixel_l[2] - test_pixel_r[2]) > 20:
        if abs(pixel[0] - test_pixel_l[0]) + abs(pixel[1] - test_pixel_l[1]) + abs(pixel[2] - test_pixel_l[2]) > 10 :
            sum_p_x += i
            count_p_x += 1
    if sum_p_x:
        up_p_x = int(sum_p_x / count_p_x)
        up_p_y = j
        up_p_pixel = im_pixel[up_p_x,up_p_y]
        #   the bottom pixel[x,y] of the platform
        for m in range(up_p_y + 247, up_p_y , -1):
            guess_pixel = im_pixel[up_p_x, m]
            if (guess_pixel[0] == up_p_pixel[0]) and (guess_pixel[1] == up_p_pixel[1]) and (guess_pixel[2] == up_p_pixel[2]):
                down_p_y = m
                down_p_x = up_p_x
                break
        #exceptions 
        #exception 6
        if im_pixel[up_p_x,up_p_y][0] == 255 and im_pixel[up_p_x,up_p_y][1] == 255 and im_pixel[up_p_x,up_p_y][2] == 255 and abs(up_p_y - down_p_y) < 105:
            #print(down_p_x)
            #print(down_p_y)
            #print("Let's take some medicine")
            down_p_x = up_p_x
            down_p_y = up_p_y + 60
        #exception 5
        elif im_pixel[up_p_x,up_p_y][0] == 227 and im_pixel[up_p_x,up_p_y][1] == 227 and im_pixel[up_p_x,up_p_y][2] == 227:
            #print("Oh it's Wecchat Bank")
            down_p_x = up_p_x
            down_p_y = up_p_y + 305
        #exception 3
        elif (140 < im_pixel[up_p_x,up_p_y][0] < 150) and (105 < im_pixel[up_p_x,up_p_y][1] < 110) and (100 < im_pixel[up_p_x,up_p_y][2] < 110):
            #print("433 days of what?")
            down_p_x = up_p_x
            down_p_y = up_p_y + 180
        #exception 7
        elif(210 < im_pixel[up_p_x,up_p_y][0] < 235) and (175 < im_pixel[up_p_x,up_p_y][1] < 200) and (145 < im_pixel[up_p_x,up_p_y][2] < 170):
             #print("I want to eat hotpot on this wooden table")
             down_p_x = up_p_x
             down_p_y = up_p_y + 180
        #exception 8
        elif im_pixel[up_p_x,up_p_y][0] == 224 and im_pixel[up_p_x,up_p_y][1] == 224 and im_pixel[up_p_x,up_p_y][2] == 224:
            #print("WebDesign seems to be fun")
            down_p_x = up_p_x
            down_p_y = up_p_y + 180
        #exception 1
        elif im_pixel[up_p_x,up_p_y][0] == 214 and im_pixel[up_p_x,up_p_y][1] == 217 and im_pixel[up_p_x,up_p_y][2] == 249:
            #print("I hope it's a good song")           
            down_p_x = up_p_x
            down_p_y = up_p_y + 180
        elif down_p_x == 0 or down_p_y == 0:
            #print("I have no idea about what's going on")
            down_p_x = up_p_x
            down_p_y = up_p_y + 180
        p_x = (up_p_x + down_p_x) / 2
        p_y = (up_p_y + down_p_y) / 2

#test
#print("c x y")
#print(c_x)
#print(c_y)
#print("up x y")
#print(up_p_x)
#print(up_p_y)
#print("down x y")
#print(down_p_x)
#print(down_p_y)
#print("p x y")
#print(p_x)
#print(p_y)
#print("up RGB")
#print(im_pixel[up_p_x,up_p_y])
      
#draw.line(((0, int(height / 3)), (width, int(height / 3))), (0, 0, 0))
#draw.line(((0, int(height * 2 / 3)), (width, int(height * 2 / 3))), (0, 0, 0))

#draw.line(((c_x, int(height * 1 / 3)), (c_x, int(height * 2 / 3))), (0, 123, 45))
#draw.line(((0, c_y), (width, c_y)), (0, 123, 45))

#draw.ellipse((c_x - 3, c_y - 3, c_x + 3, c_y + 3), fill=(255, 0, 0))

#draw.line(((p_x, int(height / 3)), (p_x, int(height * 2 / 3))), (255, 0, 128))
#draw.line(((0, p_y), (width, p_y)), (255, 0, 128))

#draw.ellipse((up_p_x - 3, up_p_y - 3, up_p_x + 3, up_p_y + 3), fill=(0, 0, 0))
#draw.ellipse((down_p_x - 3, down_p_y - 3, down_p_x + 3, down_p_y + 3), fill=(0, 0, 0))
#draw.ellipse((p_x - 3, p_y - 3, p_x + 3, p_y + 3), fill=(0, 0, 0))

#draw.line(((c_x, c_y), (p_x, p_y)), (255, 128, 64))

#im.show()

distance = math.sqrt(math.pow(c_x-p_x,2)+math.pow(c_y-p_y,2))
#print(distance)


jump(distance)
