from PIL import Image as im
import os
import time
import webbrowser as wb

a = 0
while True:
    with open('user.txt', 'r') as us:
        usr = us.readlines()
    if usr == ['User 1']:
        if a == 0:
            pg = 0
            us1 = im.open(r'files\hp-hz.png')
            us1.show()
            a +=1
        with open('gst.txt', 'r') as gus:
            gst = gus.readlines()
        if pg == 0:
            if gst == ['0']:
                time.sleep(1)
                a = 0
            if gst == ['1']:
                os.system(r'files\ch1.pdf')
                time.sleep(1)
                pg = 1
            if gst == ['2']:
                wb.open('http://ict.dunesinternationalschool.com/RPSM/')
                time.sleep(1)
                pg = 2
            if gst == ['3']:
                wb.open('https://cbseacademic.nic.in/')
                time.sleep(1)
                pg = 3
            if gst == ['4']:
                os.system(r'files\TT.pdf')
                time.sleep(1)
                pg = 4
