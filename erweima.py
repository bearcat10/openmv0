import sensor, image, time
from pyb import UART

uart = UART(3, 115200)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # QQVGA为QVGA的1/4屏，分辨率为120*160
sensor.skip_frames(30)#设置跳帧
sensor.set_auto_gain(False) # 关闭白平衡
while(True):
    img = sensor.snapshot()
    img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
    for code in img.find_qrcodes():
        print(code)
        FH= bytearray([0xb3,0xb3])
        uart.write(FH)
        uart.write(code.payload())
        FH = bytearray([0x0d,0x0a])#回车换行做结尾
        uart.write(FH)
        time.sleep_ms(1000)
