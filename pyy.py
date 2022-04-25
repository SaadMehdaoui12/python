from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui,QtWidgets
import sys
import requests
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
import webbrowser


app= QtWidgets.QApplication(sys.argv)
w=QtWidgets.QWidget()
w.resize(700,600)
w.setWindowTitle(" Scraping")
#w.setStyleSheet('background-color:black;')
w.setWindowIcon(QtGui.QIcon("C:/Users/hp/Desktop/k.jpg"))
# photo=QtWidgets.QLabel(w)
# p=QPixmap("C:/Users/hp/Desktop/d.jpg").scaled(700,600)
# photo.setPixmap(p)
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
lb1.setStyleSheet('font-family:italic;font-size:20px; border:5px solid white;border-radius:10px;color:black;')
lb1.resize(350,50)
lb1.move(10,50)
inp=QtWidgets.QLineEdit(w)
inp.resize(300,40)
inp.move(380,56)
inp.setStyleSheet('font-size:18px;border:5px solid white;border-radius:10px;font-family:Merriweather;')
inp.setToolTip('text')
image = QtWidgets.QLabel("",w)
link_btn = QtWidgets.QPushButton("link",w)
link_btn.resize(150,50)
link_btn.move(500,250)
link_btn.hide()


def link():
    # print(trai())
    webbrowser.open(trai())


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
    link = sou.find_all("article", {"class":"prd _fb col c-prd"})
    titres = []
    img=[]
    p = []
    h=[]
    num=[]
    r=[]
    links = []
    for i in range(len(link)):
      links.append(link[i].find("a",{"class":"core"}).attrs['href'])
      titres.append(link[i].find("a",{"class":"core"}).attrs['data-name'])
      img.append(link[i].find("img",{"class":"img"}).attrs['data-src'])
      h.append(prix[i].text)
    # print("\n Number of products: ", len(titres))
    # print(img[0])
    for i in h:
        p=i.split()
        for a in p[:1]:
          num.append(a)
    for i in range(len(num)):
        """convert to float without comma"""
        num_nocomma = num[i].replace(",", "")
        r.append(float(num_nocomma))
    response = requests.get(img[r.index(min(r))])
    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()
    pixmap = QPixmap("sample_image.png")
    image.setScaledContents(True)

    image.setPixmap(pixmap)
    image.move(10, 200)
    final_link = QtWidgets.QLabel(str(links[r.index(min(r))]))
    final_link.setOpenExternalLinks(True)

    link_btn.show()
    return str(f"www.jumia.ma{links[r.index(min(r))]}")
   #
   #  """Min function"""
   #  QtWidgets.QMessageBox.about(w,'Produit',f" Le Prix De Produit Est : {min(r)}" f"<br> Le Nom de Produit Est : {titres[r.index(min(r))]}"
   # f"<br> Le Site Web de Produit Est : jumia.ma{links[r.index(min(r))]}")
btn1.clicked.connect(trai)
btn2.clicked.connect(fon)
link_btn.clicked.connect(link)


w.show()
app.exec_()
