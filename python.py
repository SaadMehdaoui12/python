from PyQt5 import QtGui,QtWidgets
import sys

import requests
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from bs4 import BeautifulSoup

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
    # html = sou.prettify("utf-8")
    # with open("output1.html", "wb") as file:
    #     file.write(html)
    prix = sou.find_all("div", {"class":"prc"})
    titre = sou.find_all("h3", {"class":"name"})

    titres = []
    h=[]
    num=[]
    r=[]

    for i in range(len(titre)):
        titres.append(titre[i].text)
        h.append(prix[i].text)
        print(titres[i])
        print(h[i])

    print("\n Number of products: ", len(titre))

    for i in h:
        p=i.split()
        for a in p[:1]: 
          num.append(a)

    for i in range(len(num)) :
        """convert to float without comma"""
        num_nocomma = num[i].replace(",", "")
        r.append(float(num_nocomma))

    """Min function"""
    print(min(r))
    print(titres[r.index(min(r))])

btn1.clicked.connect(trai)
btn2.clicked.connect(fon)
w.show()
app.exec_()
