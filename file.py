""" Imports """
import glob
import os
import csv
import time
from faceapi import get_attributes

BASE_DIR = os.getcwd() + '\\data'

DIRECTORIES = [BASE_DIR + '\\' + d for d in os.listdir(BASE_DIR)]

fcsv = open("base.csv", "w+",newline="\n")
f = csv.writer(fcsv,delimiter=';')
i = 0
for dir in DIRECTORIES:
    for file in glob.glob(dir + "\\*.*"):
        if(i == 14):
            print("Pausa de 1 min, devido a API só permitir 20 requisições por minuto")
            print("Aguarde a continuação...")
            time.sleep(60)
            i=0
        attr = get_attributes(file)
        i = i + 1
        print(file)
        if(attr != ""):
                f.writerow([str(attr["faceId"]),
                attr["faceRectangle"]["top"],
                attr["faceRectangle"]["left"],
                attr["faceRectangle"]["width"],
                attr["faceRectangle"]["height"],
                attr["faceLandmarks"]["pupilLeft"]["x"],
                attr["faceLandmarks"]["pupilLeft"]["y"],
                attr["faceLandmarks"]["pupilRight"]["x"],
                attr["faceLandmarks"]["pupilRight"]["y"],
                attr["faceLandmarks"]["noseTip"]["x"],
                attr["faceLandmarks"]["noseTip"]["y"],
                attr["faceLandmarks"]["mouthLeft"]["x"],
                attr["faceLandmarks"]["mouthLeft"]["y"],
                attr["faceLandmarks"]["mouthRight"]["x"],
                attr["faceLandmarks"]["mouthRight"]["y"],
                attr["faceLandmarks"]["eyebrowLeftOuter"]["x"],
                attr["faceLandmarks"]["eyebrowLeftOuter"]["y"],
                attr["faceLandmarks"]["eyebrowLeftInner"]["x"],
                attr["faceLandmarks"]["eyebrowLeftInner"]["y"],
                attr["faceLandmarks"]["eyeLeftOuter"]["x"],
                attr["faceLandmarks"]["eyeLeftOuter"]["y"],
                attr["faceLandmarks"]["eyeLeftTop"]["x"],
                attr["faceLandmarks"]["eyeLeftTop"]["y"],
                attr["faceLandmarks"]["eyeLeftBottom"]["x"],
                attr["faceLandmarks"]["eyeLeftBottom"]["y"],
                attr["faceLandmarks"]["eyeLeftInner"]["x"],
                attr["faceLandmarks"]["eyeLeftInner"]["y"],
                attr["faceLandmarks"]["eyebrowRightInner"]["x"],
                attr["faceLandmarks"]["eyebrowRightInner"]["y"],
                attr["faceLandmarks"]["eyebrowRightOuter"]["x"],
                attr["faceLandmarks"]["eyebrowRightOuter"]["y"],
                attr["faceLandmarks"]["eyeRightInner"]["x"],
                attr["faceLandmarks"]["eyeRightInner"]["y"],
                attr["faceLandmarks"]["eyeRightTop"]["x"],
                attr["faceLandmarks"]["eyeRightTop"]["y"],
                attr["faceLandmarks"]["eyeRightBottom"]["x"],
                attr["faceLandmarks"]["eyeRightBottom"]["y"],
                attr["faceLandmarks"]["eyeRightOuter"]["x"],
                attr["faceLandmarks"]["eyeRightOuter"]["y"],
                attr["faceLandmarks"]["noseRootLeft"]["x"],
                attr["faceLandmarks"]["noseRootLeft"]["y"],
                attr["faceLandmarks"]["noseRootRight"]["x"],
                attr["faceLandmarks"]["noseRootRight"]["y"],
                attr["faceLandmarks"]["noseLeftAlarTop"]["x"],
                attr["faceLandmarks"]["noseLeftAlarTop"]["y"],
                attr["faceLandmarks"]["noseRightAlarTop"]["x"],
                attr["faceLandmarks"]["noseRightAlarTop"]["y"],
                attr["faceLandmarks"]["noseLeftAlarOutTip"]["x"],
                attr["faceLandmarks"]["noseLeftAlarOutTip"]["y"],
                attr["faceLandmarks"]["noseRightAlarOutTip"]["x"],
                attr["faceLandmarks"]["noseRightAlarOutTip"]["y"],
                attr["faceLandmarks"]["upperLipTop"]["x"],
                attr["faceLandmarks"]["upperLipTop"]["y"],
                attr["faceLandmarks"]["upperLipBottom"]["x"],
                attr["faceLandmarks"]["upperLipBottom"]["y"],
                attr["faceLandmarks"]["underLipTop"]["x"],
                attr["faceLandmarks"]["underLipTop"]["y"],
                attr["faceLandmarks"]["underLipBottom"]["x"],
                attr["faceLandmarks"]["underLipBottom"]["y"],
                attr["faceAttributes"]["gender"],
                os.path.basename(dir)])
                print("Sucesso...")


print("########## Extração concluida ###########################")
fcsv.close()