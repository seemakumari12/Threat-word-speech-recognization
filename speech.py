import speech_recognition as sr
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
r = sr.Recognizer()
flag=0
with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio)
print(text)
fil=open("aud_txt","w")
fil.write(text)
fil.close()

print (text)
stw=set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_sentence = [w for w in word_tokens if not w in stw]
print(word_tokens) 
print(filtered_sentence)
direc ="repo/"
files=os.listdir(direc)
file=[direc + dt for dt in files]
temp=[]
for i in file:
	f=open(i)
	a=f.read().splitlines()
	temp.append(a)
#print ("out")
for i in temp:
	for j in i:
		if j in filtered_sentence:
			flag=1
			print("threat",j)

if flag==0:
	print("NOT A THREAT")
