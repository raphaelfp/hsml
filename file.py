""" Imports """
import glob
import os
import csv
import json
from faceapi import get_attributes

BASE_DIR = os.getcwd() + '\\data'

DIRECTORIES = [BASE_DIR + '\\' + d for d in os.listdir(BASE_DIR)]

for dir in DIRECTORIES:
    for file in glob.glob(dir + "\\*.*"):
        # attr = json.loads(get_attributes(file))
        # f = csv.writer(open("test.csv", "wb+"))
        # for x in attr:
        #     f.writerow([x["faceId"],
        #                 x["faceAttributes"]["gender"],
        #                 x["faceLandmarks"]["eyeLeftBottom"]["x"],
        #                 x["faceLandmarks"]["eyeLeftBottom"]["y"]])
