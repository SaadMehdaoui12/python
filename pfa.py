import webbrowser
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
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
w.setWindowIcon(QtGui.QIcon("C:/Users/hp/Desktop/k.jpg"))
photo=QtWidgets.QLabel(w)
p=QPixmap("C:/Users/hp/Desktop/ww.jpg").scaled(700,600)
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
btn2.setStyleSheet('font-family:italic;background-color:red;font-size:20px;')
lb1=QtWidgets.QLabel('<i> ENTRER LE NOM DE PRODUIT   :  </i>',w)
lb1.setStyleSheet('font-family:italic;font-size:20px; border:5px solid white;border-radius:10px;color:white;')
lb1.resize(350,50)
lb1.move(10,50)
inp=QtWidgets.QLineEdit(w)
inp.resize(300,40)
inp.move(380,56)
inp.setStyleSheet('font-size:18px;border:5px solid white;border-radius:10px;font-family:Merriweather;')
inp.setToolTip('text')
im= QtWidgets.QLabel(w)
im.resize(221,221)
te= QtWidgets.QLabel(w)
te.setStyleSheet('font-family:italic;font-size:20px;color:white;')
te.resize(600,50)
te.move(50,430)
b_link=QtWidgets.QPushButton("OPEN WEB",w)
b_link.setToolTip('OPEN')
b_link.setStyleSheet('font-family:italic;background-color:LightBlue;font-size:20px;')
b_link.resize(150,50)
b_link.move(280,480)
b_link.hide()
def openweb() :
      webbrowser.open(trai())
def fon() :
  msg=QtWidgets.QMessageBox.question(w,'Exit Programme','Are You Sure')
  if msg == QtWidgets.QMessageBox.Yes:
    exit(exit)
def trai() :
    if inp.text()=="":
      QtWidgets.QMessageBox.warning(w,'WARNING','AUCUN PRODUIT SPECIFIER')
    else:
      #----------------ALIBABA.com---------------------
      res = requests.get(f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={inp.text()}")
      sou = BeautifulSoup(res.content,'lxml')
      prix_alibaba = sou.find_all("span", {"class":"elements-offer-price-normal__promotion"})
      titre_alibaba = sou.find_all("p", {"class":"elements-title-normal__content large"})
      link_alibaba = sou.find_all("div", {"class":"list-no-v2-left"})
      img_alibaba = sou.find_all("div", {"class":"seb-img-switcher J-img-switcher"})
      imgs_alibaba=[]
      tab_alibaba=[]
      links_alibaba=[]
      num_alibaba=[]
      tab1_alibaba=[]
      titres_alibaba=[]
      for i in range(len(prix_alibaba)):
        tab_alibaba.append(prix_alibaba[i].text)  
        titres_alibaba.append(titre_alibaba[i].text)
        links_alibaba.append(link_alibaba[i].find("a").attrs['href'])
        imgs_alibaba.append(img_alibaba[i].find("div",{"class":"seb-img-switcher__imgs"}).attrs['data-image'])
      for i in tab_alibaba:
            num_alibaba.append(i.split('$')[1])  
      for i in range(len(num_alibaba)):
          """convert to float without comma"""
          num_nocomma = num_alibaba[i].replace(",", "")
          tab1_alibaba.append(float(num_nocomma))
      for i in range(len(tab1_alibaba)):
        num_alibaba[i]= tab1_alibaba[i]*10


      #----------------JUMIA.com---------------------
      res = requests.get(f"https://www.jumia.ma/catalog/?q={inp.text()}")
      src = res.content
      sou = BeautifulSoup(src,"lxml")
      # html = sou.prettify("utf-8")
      # with open("output1.html", "wb") as file:
      #     file.write(html)
      prix = sou.find_all("div", {"class":"prc"})
      link = sou.find_all("article", {"class":"prd _fb col c-prd"})
      links = []
      r=[]
      titres = []
      img=[]
      p = []
      h=[]
      num=[]  
      for i in range(len(link)):
        links.append(link[i].find("a",{"class":"core"}).attrs['href'])
        titres.append(link[i].find("a",{"class":"core"}).attrs['data-name'])
        img.append(link[i].find("img",{"class":"img"}).attrs['data-src'])
        h.append(prix[i].text)  
      for i in h:
          p=i.split()
          for a in p[:1]: 
            num.append(a)  
      for i in range(len(num)):
          """convert to float without comma"""
          num_nocomma = num[i].replace(",", "")
          r.append(float(num_nocomma))
      
      #------------traitment comparison entre les deux site---------------
      test_jumia=min(r)
      test_alibaba=min(num_alibaba)
      if(test_jumia <  test_alibaba ):
        response = requests.get(img[r.index(min(r))])
        file = open("image.png", "wb")
        file.write(response.content)
        file.close()
        pixmap = QPixmap("image.png")
        im.setScaledContents(True)
        im.setPixmap(pixmap)
        im.move(250,200)  
        te.setText(f"{titres[r.index(min(r))]}")
      #final_link = QtWidgets.QLabel(str(links[r.index(min(r))]))
      #final_link.setOpenExternalLinks(True)
        b_link.show()
        return str(f"www.jumia.ma{links[r.index(min(r))]}")
      else :
        response = requests.get(f"https:{imgs_alibaba[num_alibaba.index(min(num_alibaba))]}")
        file = open("image.png", "wb")
        file.write(response.content)
        file.close()
        pixmap = QPixmap("image.png")
        im.setScaledContents(True)
        im.setPixmap(pixmap)
        im.move(250,200)  
        te.setText(f"{titres_alibaba[num_alibaba.index(min(num_alibaba))]}")
        #final_link = QtWidgets.QLabel(str(links[r.index(min(r))]))
        #final_link.setOpenExternalLinks(True)
        b_link.show()
        return str(f"https:{links_alibaba[num_alibaba.index(min(num_alibaba))]}") 
      """Min function"""
    # QtWidgets.QMessageBox.about(w,'Produit',f" Le Prix De Produit Est : {min(r)}" f"<br> Le Nom de Produit Est : {titres[r.index(min(r))]}"
    #f"<br> Le Site Web de Produit Est : jumia.ma{links[r.index(min(r))]}")
btn1.clicked.connect(trai)
btn2.clicked.connect(fon)
b_link.clicked.connect(openweb)
w.show()
app.exec_()
