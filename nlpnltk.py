from pandas.io import html
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import urllib.request

respuesta = urllib.request.urlopen('https://amazon.com')
html = respuesta.read()
#print(html)

lim = BeautifulSoup(html,"html.parser")
#print(lim)
limp_strip = lim.get_text(strip=True)
#print(limp_strip)

tok = [x for x in limp_strip.split()]
#print(tok)

frecuente = nltk.FreqDist(tok)

#for k,v in frecuente.items():
#    print(str(k), str(v))

#frecuente.plot(15, cumulative=False)

stw = stopwords.words("english")
stw.append('&')
stw.append('-')

#print(stw)
for t in tok:
    try:
        #if t in stw: 
        ts = str.casefold(t)
        if ts in stw:
            #print("match",ts)
            tok.remove(t)
    except:
        pass

frecuente = nltk.FreqDist(tok)
frecuente.plot(30, cumulative=False)