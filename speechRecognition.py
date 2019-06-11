import sys, os, pyglet,time
import speech_recognition as sr
from gtts import gTTS as ts
from nltk.corpus import wordnet as wn
import requests
from bs4 import BeautifulSoup

r = sr.Recognizer()
mp3file = __file__[:-3]+".mp3"

#defining the work
def mywork(wordlist):
    works=['convert currency from indian to international and vice versa','tell you definition','show you time','show you date','tell you latest news']
    for i in works:
        text_to_speech("i can "+i)

#geting latest news
def news(wordlist):
    url = 'https://twitter.com/i/moments?category_id=1'

    response=requests.get(url)
    source_code=response
    plain_text= source_code.text
#    print(plain_text)
    soup= BeautifulSoup(plain_text,'html.parser')
    titl=''
    for link in soup.findAll('a',{"class":"MomentCapsuleSummary-title"}):
        href=link.get('href')
        if href=="/about":
            break
        titl=link.string
#        print(href)
        if titl:
            print(titl,href)
            text_to_speech(titl)

def Time(wordlist):
    wordlist = None                             # will update later using pytz module
    if not wordlist:
        Time = time.localtime()
        sys.stdout.write(time.strftime("%X",Time))

def Date(wordlist):
    wordlist = None                             # will update later using pytz module
    if not wordlist:
        Date = time.localtime()
        sys.stdout.write(time.strftime("%x",Date))


def define(wordlist):
    word = wordlist[-1]
    syn = wn.synsets(word)
    string = syn[0].lemmas()[0].name() + '(' + syn[0].lexname().split('.')[0] + ')'
    string += syn[0].definition()
    string += '\n'
    string += 'Examples:' if syn[0].examples() else ''
    for eg in syn[0].examples():
        string += eg +','
    text_to_speech(string)
    sys.stdout.write("\n" + string)

def text_to_speech(text):

    objct = ts(text=text,lang = 'en',slow = False)
    objct.save(mp3file)
    sound = pyglet.media.load(mp3file)
    sound.play()
    time.sleep(sound.duration)

def voice_input():

    with sr.Microphone() as source:
        #sys.stdout.write('Speak Now')
        text_to_speech('Speak Now')
        sys.stdout.write("\n>")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        a = r.recognize_google(audio)
        sys.stdout.write(a)
        #text_to_speech(a)

        f = open('recognizedtext.txt','w')
        f.write(a)
        f.close()

        return a.lower()
    except sr.UnknownValueError:
        deaf = "i can't hear you"
        sys.stdout.write(deaf)
        text_to_speech(deaf)
    except sr.RequestError as e:
        error= "could not request result : {e}".format(e)
        sys.stdout.write(error)
        text_to_sppech(error)
    return


#handling the web
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
    spanList = []
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

    for i in range(length):
        if(x[i].text ==''):
            continue
        else:
            spanList.append(x[i])
            
    '''For debugging we can write the reply of the list in a file
    f = open('googleReply.txt','w')
    print(len(spanList))
    for item in spanList:
        result = '{}\n'.format(item.text)
        f.write(result)
    f.close()'''

    
    for i in range(len(spanList)):
        if (len(spanList[i].text)>10):
            #print(x[i].text,)
            #spanList.append(x[i])
            return spanList[i].text
            break



commandslist = {'time':Time,'date':Date,'define':define,
                'meaning':define,'mean':define,
                'work':mywork,'news':news}


#if __name__ == '__main__':
def main():
    while True:
        flag = False
        i=0
        try:
            getinput = voice_input().split()
            if getinput == None:
                raise
        except:
            continue
        stt=" ".join(getinput)
        if len(stt)>2:
            text_to_speech(stt)

        '''voice_input()
        f = open('googleReply.txt','r')
        fileText = f.read()
        f.close()'''
        for word in getinput:
            i += 1
            if word in ['exit','terminate','end','bye']:
                flag = True
                text = "terminating the program, good bye"
                text_to_speech(text)
                break
            if word in commandslist:
                commandslist[word](getinput[i:])
                break
            else:
                query = readTextFile()
                query = query.lower()
                replyText = scraper(query)
                '''f = open('googleReply.txt','r')
                replyText = f.read()
                f.close()'''
                sys.stdout.write('\n --')
                sys.stdout.write(replyText)
                text_to_speech(replyText)
                break
        if flag:
            break
        time.sleep(1)
if __name__ == '__main__':
    main()
