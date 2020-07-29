from flask import Flask , render_template , request, redirect, url_for
from bs4 import BeautifulSoup
import urllib.request
import random
import time
import csv
import binascii

app = Flask(__name__)

questiondict = {"How Many Weekdays Are There In A Week?" : 5, "How Many Weekends Are There In A Week ?":2 ,"How Many Letters Does the Word 'Cat' Have ?":3
,"How many colors are there in the traffic signals?":3,"How many sides are there in a square?":4
,"How many tires does a car have?":4



}
qlist = list(questiondict.keys())

wordscsv = csv.reader(open('words.csv', 'r'))

words = []
for i in wordscsv:
    for j in i:
        words.append(j.strip().lower())

def rwords():
    Rwords = []
    while(len(Rwords) < 7):
        x=random.choice(words)
        if x not in Rwords and x != '':
            Rwords.append(x)
    return Rwords

@app.route("/",methods = ['GET','POST'])
def hi():
    if request.method == 'POST':
        
        s = request.form['text']
        if 'a' in request.args:
            a = request.args['a']
        x = a[2:-1]

        result = "Success" if s.strip()== bytearray.fromhex(x).decode().strip() else "Failed"

        return render_template('cap.html',title = "Result",result = result)


    logicq = random.choice(qlist)
    wordq = rwords()
    x= wordq[questiondict[logicq]-1].encode(encoding='ascii')
    lqa=binascii.hexlify(x)
    return render_template('cap.html',title = "CAPTCHA verification",wordq=wordq,logicq = logicq,val = "yes",lqa= lqa)



if __name__ == "__main__":

    app.run(debug = True)
