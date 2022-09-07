
from tkinter import *
from turtle import left, width
from PIL import ImageTk,Image
import tkinter.ttk
import bs4
import urllib.request as url
import cv2
import numpy as np
import os

#input

def input_web():
    product=name_input1.get()
    product = product.split()
    product = "+".join(product)
    path = "https://www.flipkart.com/search?q="
    http = url.urlopen(path + product)
    page = bs4.BeautifulSoup(http,features="html.parser")
    
    prod_name = page.find("div", class_="_4rR01T").text
    
 
    price = page.find("div", class_="_30jeq3").text
    #print(price)
    details = page.find("ul", class_="_1xgFaf")
    details = details.find_all("li")
    det = []
    for detail in details:
    
      det.append(detail.text)
    j=0
    

        #print(i)
    #print(det)
    y=Message(root1,text=prod_name,fg='red',bg='black',aspect= 900,justify=LEFT,relief=RAISED)
    y.place(x=10,y=210)
    y.config(font=('arial',12))
    y1=Label(root1,text=price,fg='red',bg='black')
    y1.place(x=10,y=260)
    y1.config(font=('arial',12))
    for i in det:
         
         y2=Message(root1,text=i,fg='red',bg='black',aspect= 900,justify=LEFT,relief=RAISED)
         y2.place(x=10,y=300+j)
         y2.config(font=('arial',12))
         j=j+51
    images = page.find('div',{'class':'CXW8mj'})
    #print(images)
    z=str(images).index('src')
    a=str(images)
    path=a[z+5:-9]
    #print(path)
    resp=url.urlopen(path)
    image=np.asarray(bytearray(resp.read()),dtype="uint8")
    #print(image)
    image=cv2.imdecode(image,cv2.IMREAD_COLOR)
    #print(image)
    filename='savedImages.png'
    cv2.imwrite(filename,image) 
    image14=Image.open('savedImages.png')

# Resize the image in the given (width, height)
    img=image14.resize((300, 190))

# Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)

# Display the image with label
    label=Label(root1, image=my_img)
    label.image = my_img
    label.place(x=130,y=0)
    
    #product 2
    product1=name_input2.get()
    product1 = product1.split()
    product1 = "+".join(product1)
    path = "https://www.flipkart.com/search?q="
    http1 = url.urlopen(path+ product1)
    page = bs4.BeautifulSoup(http1,features="html.parser")
    prod_name1 = page.find("div", class_="_4rR01T").text
    #print(prod_name1)
    price1 = page.find("div", class_="_30jeq3").text
    #print(price1)
    details1 = page.find("ul", class_="_1xgFaf")
    details1 = details1.find_all("li")
    det1 = []
    for detail1 in details1:
       det1.append(detail1.text)
    #print(det1)
    x=Message(root1,text=prod_name1,fg='red',bg='black',aspect=950,relief=RAISED)
    x.place(x=615,y=210)
    x.config(font=('arial',12))
    x1=Label(root1,text=price1,fg='red',bg='black')
    x1.place(x=615,y=260)
    x1.config(font=('arial',12))
    v=0
    for i in det:
        x2=Message(root1,text=i,fg='red',bg='black',aspect= 900,justify=LEFT,relief=RAISED)
        x2.place(x=615,y=300+v)
        x2.config(font=('arial',12))
        v=v+51
    images1 = page.find('div',{'class':'CXW8mj'})
#print(images)
    z1=str(images1).index('src')
    a1=str(images1)
    path=a1[z1+5:-9]
    #print(path)
    resp1=url.urlopen(path)
    image1=np.asarray(bytearray(resp1.read()),dtype="uint8")
    #print(image)
    
    #print(image)
    filename1='savedImages2.png'
    image1=cv2.imdecode(image1,cv2.IMREAD_COLOR)
    cv2.imwrite(filename1,image1)
    #second_img=ImageTk.PhotoImage(Image.open('savedImages2.png'))
    image24=Image.open('savedImages2.png')

    img24=image24.resize((300, 190))

# Conver the image in TkImage
    my_img24=ImageTk.PhotoImage(img24)

# Display the image with label
    label24=Label(root1, image=my_img24)
    label24.image = my_img24
    label24.place(x=730,y=0)
    '''
    img_label21=Label(root1,image=second_img)
    img_label21.image = second_img
    img_label21.place(x=600,y=10)
   '''

#second screeen data
    
def second_screen():
    global root1
    root1=Tk()
    root1.title("COMPARE HUB")

    #root.iconbitmap("icon.png")
    root1.minsize(1200,600)
    bg=PhotoImage(file="bg1.png")

    my_label=Label(root1,image=bg,bg='black')  
    my_label.place(x=0,y=0)
    
    #product1
    x=Label(root1,text='Search for Product 1',fg='red',bg='black')
    x.place(x=60,y=10)
    x.config(font=('Nunito',24))
    global name_input1
    global name_input2
    name_input1=Entry(root1,width=40,insertwidth=2)
    name_input1.place(x=80,y=110,height=30)
    
    
    #seperator
    
    vertical =Frame(root1, bg='black', height=700,width=10)
    vertical.place(x=590, y=0)
    hor =Frame(root1, bg='black', height=10,width=1200)
    hor.place(x=0, y=200)


    def funca():
        input_web()
    def funcb():
        login_btn2.destroy()
    def funcc():
        x.destroy()
        name_input1.destroy()
        y.destroy()
        name_input2.destroy()

    

    
    #product2
    y=Label(root1,text='Search for Product 2',fg='red',bg='black')
    y.place(x=829,y=10)
    y.config(font=('Nunito',24))
    name_input2=Entry(root1,width=40)
    name_input2.place(x=850,y=110,height=30)
    #compare button
    login_btn2=Button(root1,text='COMPARE',bg='black',fg='red',bd=5,command=lambda:[funca(),funcb(),funcc()])
    login_btn2.place(x=530,y=210)
    login_btn2.config(font=('Nunito',18))
    

    #inputread
           
        

    root1.mainloop()

    
    

root=Tk()
root.title("COMPARE HUB")

#root.iconbitmap('title_icon.png')
#screen size
root.minsize(1200,600)
#background
#root.configure(background='black')
bg=PhotoImage(file="bg1.png")


my_label=Label(root,image=bg,bg='black')
my_label.place(x=0,y=0)



#text_label=Label(root,text='WELCOME  TO',fg='#FDF5E6',bg='black')
#text_label.place(x=200,y=20)
#text_label.config(font=('Nunito',55,'bold'))
img11=ImageTk.PhotoImage(Image.open('logo.png'))
img_label11=Label(root,image=img11,bg='black')
img_label11.place(x=300,y=5)
#enter instruction

name_lable=Label(root,text='PLEASE CLICK PROCEED TO CONTINUE : ',fg='red',bg='black')
name_lable.place(x=50,y=500)
name_lable.config(font=('verdana',19))



#login button
def funca():
    root.destroy()

def funcb():
    second_screen()
    
#submit
login_btn=Button(root,text='CONTINUE',bg='#303030',fg='red',bd=5,command=lambda:[funca(),funcb()])
login_btn.place(x=590,y=500)
login_btn.config(font=('Nunito BOLD 10',15))





root.mainloop()
