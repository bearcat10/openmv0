import sensor, image,time,lcd, pyb , ustruct , ubinascii
from pyb import UART,Timer,LED
#

red_threshold_01 = (52, 83, 33, 84, 30, 86)
green_threshold_01 = (77, 100, -72, 17, 3, 96)
yellow_threshold_01 = (75, 100, -48, 11, 3, 96)

# BZ_mode  = "A55A04B3B7AA"
# Forward  = "A55A04B2B6AA"
# stop     = "A55A04B5B9AA"

sensor.reset()
sensor.set_pixformat(sensor.RGB565)#格式为RG565
sensor.set_framesize(sensor.QVGA)#320*240QVGA：Quarter VGA，即：VGA的四分之一
sensor.set_windowing((320, 240))
sensor.skip_frames(30)#设置跳帧，使新设置生效,并自动调节白平衡
sensor.set_auto_whitebal(False)      #关闭白平衡
sensor.set_auto_gain(False)          #关闭自动增益
clock = time.clock()# 追踪帧率
lcd.init() #初始化lcd
uart = UART(3,9600,8,None,1)       #创建串口对象，波特率9600，数据位数为8位，无校验位，1位停止位
data = []


data = []

LED_Red = LED(1)
LED_Green = LED(2)
LED_Blue = LED(3)
BLUE_LED_PIN = 3

def expand_roi(roi):
     #set for QQVGA 160*120
    extra = 5
    win_size = (640, 480)
    (x, y, width, height) = roi
    new_roi = [x-extra, y-extra, width+2*extra, height+2*extra]

    if new_roi[0] < 0:
        new_roi[0] = 0
    if new_roi[1] < 0:
        new_roi[1] = 0
    if new_roi[2] > win_size[0]:
        new_roi[2] = win_size[0]
    if new_roi[3] > win_size[1]:
        new_roi[3] = win_size[1]

    return tuple(new_roi)
sensor.skip_frames(time = 1000) # Give the user time to get ready.

tim = Timer(4,freq=1)              # create a timer object using timer 4
#tim.callback(tick)
tim.deinit()

#time.sleep(5000)                     # 等一下stm32,5秒钟



#uart.write(ustruct.pack("b",0xA5))
#uart.write(ustruct.pack("b",0x5A))
#uart.write(ustruct.pack("b",0x04))
#uart.write(ustruct.pack("b",0xB1))
#uart.write(ustruct.pack("b",0xB5))
#uart.write(ustruct.pack("b",0xAA))         #开机，进入寻迹模式
#print("寻迹模式")

#uart.write(ustruct.pack("b",0xA5))
#uart.write(ustruct.pack("b",0x5A))
#uart.write(ustruct.pack("b",0x04))
#uart.write(ustruct.pack("b",0xB3))
#uart.write(ustruct.pack("b",0xB7))
#uart.write(ustruct.pack("b",0xAA))     #开机，进入避障模式
#print("避障模式")



#time.sleep(100000)




while(True):

    sensor.skip_frames(5) #     检测的慢一点

    img = sensor.snapshot()
    clock.tick() # Track elapsed milliseconds between snapshots().
    blobs_red = img.find_blobs([red_threshold_01], area_threshold=150)
    blobs_green = img.find_blobs([green_threshold_01], area_threshold=150)
    blobs_yellow = img.find_blobs([yellow_threshold_01], area_threshold=150)



    #print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected




    #if blobs_yellow:
    ##如果找到了目标颜色
        ##print(blobs)
        ##print("黄灯")bgf
        #numjtdy = 0
        #numjtdy = numjtdy+1
        #for blob in blobs_yellow:
        ##迭代找到的目标颜色区域
            #is_circle = False
            #max_circle = None
            #max_radius = -1

            #new_roi = expand_roi(blob.rect())

            #for c in img.find_circles(threshold = 2000, x_margin = 20, y_margin = 20, r_margin = 1, roi=new_roi):
                #is_circle = True
                ## img.draw_circle(c.x(), c.y(), c.r(), color = (255, 255, 255))
                #if c.r() > max_radius:
                    #max_radius = c.r()
                    #max_circle = c
            #if is_circle:
                ## 如果有对应颜色的圆形 标记外框
                ## Draw a rect around the blob.
                #img.draw_rectangle(new_roi) # rect
                #img.draw_rectangle(blob.rect()) # rect
                ##用矩形标记出目标颜色区域
                #img.draw_cross(blob[5], blob[6]) # cx, cy
                #img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r(), color = (0, 255, 0))
                #img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r() + 1, color = (0, 255, 0))


                ##uart.write(ustruct.pack("<b",0xA55A04B5B9AA))
                ##uart.write(ubinascii.hexlify(stop))

                #uart.write(ustruct.pack("b",0xA5))
                #uart.write(ustruct.pack("b",0x5A))
                #uart.write(ustruct.pack("b",0x04))
                #uart.write(ustruct.pack("b",0xB5))
                #uart.write(ustruct.pack("b",0xB9))
                #uart.write(ustruct.pack("b",0xAA))

                ##uart.write("A55A04B5B9AA")
                #print("黄灯")


                #sensor.snapshot().save("example.jpg") # or "example.bmp" (or others)
                #pyb.LED(BLUE_LED_PIN).off()
                #sensor.skip_frames(time = 2000) # Give the user time to get ready.


    if blobs_yellow:
    #如果找到了目标颜色
        #print(blobs)
        #print("黄灯")
        numjtdg = 0
        numjtdg = numjtdg+1
        for blob in blobs_yellow:
        #迭代找到的目标颜色区域
            is_circle = False
            max_circle = None
            max_radius = -1

            new_roi = expand_roi(blob.rect())

            for c in img.find_circles(threshold = 2000, x_margin = 20, y_margin = 20, r_margin = 1,  roi=new_roi):
                is_circle = True
                # img.draw_circle(c.x(), c.y(), c.r(), color = (255, 255, 255))
                if c.r() > max_radius:
                    max_radius = c.r()
                    max_circle = c
            if is_circle:
                # 如果有对应颜色的圆形 标记外框
                # Draw a rect around the blob.
                img.draw_rectangle(new_roi) # rect
                img.draw_rectangle(blob.rect()) # rect
                #用矩形标记出目标颜色区域
                img.draw_cross(blob[5], blob[6]) # cx, cy
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r(), color = (0, 255, 0))
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r() + 1, color = (0, 255, 0))
                #uart.write(ubinascii.hexlify(Forward))
                #uart.write("A55A04B2B6AA")

                uart.write(ustruct.pack("b",0xA5))
                uart.write(ustruct.pack("b",0x5A))
                uart.write(ustruct.pack("b",0x04))
                uart.write(ustruct.pack("b",0xB3))
                uart.write(ustruct.pack("b",0xB7))
                uart.write(ustruct.pack("b",0xAA))     #开机，进入避障模式
                print("避障模式")
                print("黄灯")






    if blobs_green:
    #如果找到了目标颜色
        #print(blobs)
        #print("绿灯")
        numjtdg = 0
        numjtdg = numjtdg+1
        for blob in blobs_green:
        #迭代找到的目标颜色区域
            is_circle = False
            max_circle = None
            max_radius = -1

            new_roi = expand_roi(blob.rect())

            for c in img.find_circles(threshold = 2000, x_margin = 20, y_margin = 20, r_margin = 1,  roi=new_roi):
                is_circle = True
                # img.draw_circle(c.x(), c.y(), c.r(), color = (255, 255, 255))
                if c.r() > max_radius:
                    max_radius = c.r()
                    max_circle = c
            if is_circle:
                # 如果有对应颜色的圆形 标记外框
                # Draw a rect around the blob.
                img.draw_rectangle(new_roi) # rect
                img.draw_rectangle(blob.rect()) # rect
                #用矩形标记出目标颜色区域
                img.draw_cross(blob[5], blob[6]) # cx, cy
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r(), color = (0, 255, 0))
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r() + 1, color = (0, 255, 0))
                #uart.write(ubinascii.hexlify(Forward))
                #uart.write("A55A04B2B6AA")

                uart.write(ustruct.pack("b",0xA5))
                uart.write(ustruct.pack("b",0x5A))
                uart.write(ustruct.pack("b",0x04))
                uart.write(ustruct.pack("b",0xB3))
                uart.write(ustruct.pack("b",0xB7))
                uart.write(ustruct.pack("b",0xAA))     #开机，进入避障模式
                print("避障模式")
                print("绿灯")





    if blobs_red:
    #如果找到了目标颜色
        #print(blobs)
        #print("红灯")

        numjtdr = 0
        numjtdr = numjtdr+1
        for blob in blobs_red:
        #迭代找到的目标颜色区域
            is_circle = False
            max_circle = None
            max_radius = -1

            new_roi = expand_roi(blob.rect())

            for c in img.find_circles(threshold = 4000, x_margin = 20, y_margin = 20, r_margin = 20, roi=new_roi):
                is_circle = True
                # img.draw_circle(c.x(), c.y(), c.r(), color = (255, 255, 255))
                if c.r() > max_radius:
                    max_radius = c.r()
                    max_circle = c
            if is_circle:
                # 如果有对应颜色的圆形 标记外框
                # Draw a rect around the blob.
                img.draw_rectangle(new_roi) # rect
                img.draw_rectangle(blob.rect()) # rect
                #用矩形标记出目标颜色区域
                img.draw_cross(blob[5], blob[6]) # cx, cy
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r(), color = (0, 255, 0))
                img.draw_circle(max_circle.x(), max_circle.y(), max_circle.r() + 1, color = (0, 255, 0))
                #uart.write(ubinascii.hexlify(stop))
                uart.write(ustruct.pack("b",0xA5))
                uart.write(ustruct.pack("b",0x5A))
                uart.write(ustruct.pack("b",0x04))
                uart.write(ustruct.pack("b",0xB5))
                uart.write(ustruct.pack("b",0xB9))
                uart.write(ustruct.pack("b",0xAA))
                #uart.write("A55A04B5B9AA")    #停车
                print("红灯")


    #lcd.display(img)

