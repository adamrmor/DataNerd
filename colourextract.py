import pandas as pd
from pandas import DataFrame
import csv
import urllib
import sys
import Image
import pprint
import cooperhewitt.roboteyes.shannon as shannon
import cooperhewitt.roboteyes.colors.palette as palette
from roygbiv import *
import urllib
import json
import csv
import cooperhewitt.swatchbook as sb



input ="errorredo.csv"
df = pd.read_csv(input)

r=open("errorredoout.csv","ab")
rr=csv.writer(r)
headings = [['id','image','entropy','c1','c2','c3','c4','c5','C11','C22','C33','C44','C55']]
rr.writerows(headings)


for index, row in df.iterrows():
    try:
        pic = row['image']
        Id = row['id']
        urllib.urlretrieve(pic,'1.jpg')
        im = Image.open('1.jpg')
        roy = Roygbiv(im)
        entropy = shannon.entropy(im)
        ref = 'naturalcolorsystem'
        rsp = palette.extract_roygbiv(im, ref)
        parsed_json = json.loads(json.dumps(rsp))
        print rsp
        
        
        
        A1 = parsed_json['palette'][0]['color']
        C1 = sb.closest('css3', A1)
        C11 = sb.closest('naturalcolorsystem', A1)
               
        #A2 = parsed_json['palette'][1]['color']
        #C2 = sb.closest('css3', A2)
        #C22 = sb.closest('naturalcolorsystem', A2)
                
        #A3 = parsed_json['palette'][2]['color']
        #C3 = sb.closest('css3', A3)
        #C33 = sb.closest('naturalcolorsystem', A3)
                
        #A4 = parsed_json['palette'][3]['color']
        #C4 = sb.closest('css3', A4)
        #C44 = sb.closest('naturalcolorsystem', A4)
                
        #A5 = parsed_json['palette'][4]['color']
        #C5 = sb.closest('css3', A5)
        #C55 = sb.closest('naturalcolorsystem', A5)
                
        data  = [[Id,pic,entropy,C1]]
        #C4,C5,C11,C22,C33,C44,C55]]
       #print data
        rr.writerows(data)

    except IndexError:
        print("<5 colours")
        data =[[Id,pic,'error']]
        rr.writerows(data)

        
    except ValueError:
        print("value error")
        data =[[Id,pic,' Value error']]
        rr.writerows(data)
 
    except IOError:
        print("IO image error")
        data =[[Id,pic,'IO image error']]
        rr.writerows(data)  
        
rr.close() 
