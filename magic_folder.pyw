import os
from time import sleep

prtime = 0


def vicechief(dir):
    i = 1
    vcfiles = os.listdir('E:/MAGIC PROJECT')
    for item in vcfiles:
        fname = item.split('.')
        if fname[0].startswith(fname[0][0]) and fname[0].endswith(fname[0][0]) and int(fname[0]) == int(i):
            if fname[1] == 'jpg' or fname[1] == 'png' or fname[1] == 'bmp':
                print(dir + "/" + item)
                # pfname = int(fname[0]) + 1
                os.rename(dir + "/" + item, dir + "/" + str(i) + '.' + fname[1])
                i = i + 1
                # pfname = pfname + 1

            elif fname[1] == 'txt' or fname[1] == 'docs' or fname[1] == 'xlsx' or fname[1] == 'xml':
                print("TEXT FILE DETECTED in Delete func :- " + item)

            elif fname[1] == 'html' or fname[1] == 'cpp' or fname[1] == 'py' or fname[1] == 'exe':
                print("TEXT FILE DETECTED in delete func:- " + item)

            elif fname[1] == '':
                print("no extension file :-", item)
            else:
                print("ERROR 001 :- ", item)

        elif fname[1] == 'txt' or fname[1] == 'docs' or fname[1] == 'xlsx' or fname[1] == 'xml':
            print("TEXT FILE DETECTED :- " + item)

        elif fname[1] == 'html' or fname[1] == 'cpp' or fname[1] == 'py' or fname[1] == 'exe':
            print("TEXT FILE DETECTED :- " + item)

        elif fname[1] == '':
            print("no extension file :-", item)
        elif fname[1] == 'jpg' or fname[1] == 'png' or fname[1] == 'bmp':
            os.rename(dir + "/" + item, dir + "/" + str(i) + '.' + fname[1])
            i = i + 1
        else:
            print("ERROR 002:- ", item)


def chief(dir):
    cfiles = os.listdir(dir)
    i = 0
    pfname = i
    for item in cfiles:
        print("Running", i, "time")
        fname = item.split('.')
        try:
            if fname[0].startswith(fname[0][0]) and fname[0].endswith(fname[0][0]) and int(fname[0]) == int(pfname):
                if fname[1] == 'jpg' or fname[1] == 'png' or fname[1] == 'bmp':
                    print(dir + "/" + item)
                    pfname = int(fname[0]) + 1
                    os.rename(dir + "/" + item, dir + "/" + str(pfname) + '.' + fname[1])
                    i = i + 1
                    pfname = pfname + 1

                elif fname[1] == 'txt' or fname[1] == 'docs' or fname[1] == 'xlsx' or fname[1] == 'xml':
                    print("TEXT FILE DETECTED :- " + item)

                elif fname[1] == 'html' or fname[1] == 'cpp' or fname[1] == 'py' or fname[1] == 'exe':
                    print("TEXT FILE DETECTED :- " + item)

                elif fname[1] == '':
                    print("no extension file :-", item)
                else:
                    print("ERROR 001 :- ", item)

            elif fname[1] == 'txt' or fname[1] == 'docs' or fname[1] == 'xlsx' or fname[1] == 'xml':
                print("TEXT FILE DETECTED :- " + item)

            elif fname[1] == 'html' or fname[1] == 'cpp' or fname[1] == 'py' or fname[1] == 'exe':
                print("TEXT FILE DETECTED :- " + item)

            elif fname[1] == '':
                print("no extension file :-", item)
            elif fname[1] == 'jpg' or fname[1] == 'png' or fname[1] == 'bmp':
              try:
                os.rename(dir + "/" + item, dir + "/" + str(pfname + 1) + '.' + fname[1])
              except PermissionError:
                  sleep(2)
                  os.rename(dir + "/" + item, dir + "/" + str(pfname + 1) + '.' + fname[1])
              i = i + 1
              pfname = pfname + 1
            else:
                print("ERROR 002:- ", item)
        except FileNotFoundError:
            pass


files = os.listdir('E:/MAGIC PROJECT').__len__()
while True:
    sleep(2)
    prtime = prtime + 1
    print("background process #", prtime)

##--------------------------------------------------------------------------------------------------------By Pratyaksh soni || pratyakshsoni2004@gmail.com    

    if os.listdir('E:/MAGIC PROJECT').__len__() < files:
        vicechief('E:/MAGIC PROJECT')
        sleep(3)

    else:
        try:
            chief('E:/MAGIC PROJECT')
        except PermissionError:
            sleep(5)
            chief('E:/MAGIC PROJECT')

    files = os.listdir('E:/MAGIC PROJECT').__len__()



##By Pratyaksh soni || pratyakshsoni2004@gmail.com
