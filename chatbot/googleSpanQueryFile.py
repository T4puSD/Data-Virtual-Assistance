import requests
from bs4 import BeautifulSoup

spanList = []

def urlAppend(st):
    google = 'https://www.google.co.in/search?q='
    st1 = st.replace(' ','+')
    return google + st1

def readTextFile():
    f = open('recognizedtext.txt','r')
    fileText = f.read()
    f.close()
    return fileText
def scraper(x):
    queryUrl = urlAppend(x)
    #print (queryUrl)
    #print('\n')
    page = requests.get(queryUrl)
    #print(page)
    soup = BeautifulSoup(page.text,'html.parser')
    #x = soup.find_all('span',{'class':'ILfuVd'}) #st
    x = soup.find_all('span')
    #spanList = x
    length = len(x)

    f = open('googleReply.txt','w')
    
    for i in range(length):
        if(x[i].text ==''):
            continue
        else:
            #print(x[i].text,)
            #spanList.append(x[i])
            f.write(x[i].text)
            break
    #print(spanList[2].text)
    #f = open('googleReply.txt','w')
    #f.write(spanList[1].text)
    f.close()

#x = input('enter word:')
query = readTextFile()
query = query.lower()
reply = scraper(query)
#print(reply)
#lr_dct_sf_sens
