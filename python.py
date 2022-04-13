from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
from turtle import exitonclick
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
app= QtWidgets.QApplication(sys.argv)
w=QtWidgets.QWidget()
w.resize(700,600)
w.setWindowTitle(" Scraping")
#w.setStyleSheet('background-color:black;')
w.setWindowIcon(QtGui.QIcon("C:/Users/hp/Desktop/thh.jpg"))
photo=QtWidgets.QLabel(w)
p=QPixmap("C:/Users/hp/Desktop/bg.jpg").scaled(700,600)
photo.setPixmap(p)
btn1=QtWidgets.QPushButton('Rechercher', w)
btn1.setToolTip('Rechercher')
btn1.resize(150,50)
btn1.move(500,100)
btn1.setStyleSheet(' font-size:20px;')
btn2=QtWidgets.QPushButton('Quite', w)
btn2.setToolTip('Quite')
btn2.resize(150,50)
btn2.move(500,155)
btn2.setStyleSheet('font-family:italic;background-color:red;font-size:20px;font-family:italic;')
lb1=QtWidgets.QLabel('<i> ENTRER LE NOM DE PRODUIT   :  </i>',w)
lb1.setStyleSheet('font-family:italic;font-size:20px; border:5px solid white;border-radius:10px;color:white;')
lb1.resize(350,50)
lb1.move(10,50)
inp=QtWidgets.QLineEdit(w)
inp.resize(300,40)
inp.move(380,56)
inp.setStyleSheet('font-size:18px;border:5px solid white;border-radius:10px;font-family:Merriweather;')
inp.setToolTip('text')
def fon() :
  msg=QtWidgets.QMessageBox.question(w,'Exit Programme','Are You Sure')
  if msg == QtWidgets.QMessageBox.Yes:
    exit(exit)

def trai() :
    res = requests.get(f"https://www.jumia.ma/catalog/?q={inp.text()}")
    src = res.content
    sou = BeautifulSoup(src,"lxml")
    prix = sou.find_all("div", {"class":"prc"})
    titre = sou.find_all("h3", {"class":"name"}) 
    titres = []
    p = []
    h=[]
    num=[]
    r=[] 
    j=0  
    t=0
    o=[]
    for i in range(len(titre)):
      titres.append(titre[i].text)
    for i in range(len(prix)):
      h.append(prix[i].text)  
    for i in h:
        p=i.split()
        for a in p[:1]: 
          num.append(a)
    for i in range(len(num)) :
        r.append(float(num[i])) 
    i=0 
    j=r[i]  
    while i  < len(r)-1:
      if j < r[i+1] :
           t=i
      else  :
          j=r[i+1]
          t=i+1
      i+=1   
    print(j)  
    print(titres[t])  
btn1.clicked.connect(trai)
btn2.clicked.connect(fon)
w.show()
app.exec_()
