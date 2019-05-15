import pandas as pd
from pandas import DataFrame
import csv
import urllib
import sys
import Image
import pprint
from roygbiv import *
import urllib
import json
import csv


input ="AppliedArtsbags.csv"
df = pd.read_csv(input)

r=open("test1.csv","ab")
rr=csv.writer(r)

i=1
for index, row in df.iterrows():

    pic = row['image']
    Id = row['image']
    aa = str(i)+str(".jpg")
    print aa
    urllib.urlretrieve(pic,aa)
    im = Image.open(aa)
    i+=1
    print i
