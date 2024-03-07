from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
win=Tk()

win.geometry('1000x800')
win.title('MED PHARMA')

# Frames, Labels, Buttons 

frames=[]
labels=[]
btns=[]
values=[]
add_to_cart_inc=[]
add_to_cart_dec=[]
quantity=[]
g=0
no_items=0
total=0
times=0
# Top Level

tp=Toplevel(win)
tp.title("CART")
tp.geometry('500x500')
desc=[]
desc1=[]

def inc(a,d):
    
    def cart(i,j,k,l):
        global tp
        global total
        global g
        global label4
        global label5
        global desc
        global desc1
        global no_items
        global label6
        global label7
        global times
        
        if j>1:
            len3=len(desc)
            for o in range(len3):
                
                if desc[o].cget('text')==i:
                   text2= 'Rs '+ str(k) + '*'+str(j)
                   desc1[o].config(text=text2)
                   total=total+k
                   label7.config(text='Rs '+str(round(total,2)))
        else:
            
            label4=Label(tp,text=i)
            label4.grid(row=0+g,column=0)
            desc.append(label4)
            text1= 'Rs '+ str(k) + '*'+str(j)
        
            label5=Label(tp,text=text1)
            label5.grid(row=0+g,column=1)
            desc1.append(label5)
            no_items+=1
            total=total+k     
            
            label6=Label(tp,text=str(no_items))
            label6.grid(row=20,column=0)
            
            if times==0:
                label7=Label(tp,text='',fg='red')
                label7.grid(row=22,column=1)
            label7.config(text='Rs '+str(round(total,2)))
            g=g+1
            times+=1
            
   
    val_inc=int(quantity[a].cget('text'))
    
    val_inc+=1
    
    
    quantity[a].config(text=str(val_inc))
    
    cart(d,int(quantity[a].cget('text')),prices1[a],a)
    
    
    
    
    
def dec(b,m):
    def cart(i,j,k,l):
       
        global tp
        global total
        global g
        global label7
        global label4
        global label5
        global label6
        global desc
        global desc1
        global no_items
        temp1=int(j)
        if j >=1: 
           
            len1=len(desc)
            for f in range(len1):
                               
                if desc[f].cget('text')==i:
                   text3= 'Rs '+ str(k) + '*'+str(j)
                   desc1[f].config(text=text3)
                   total=total-k
                   label7.config(text='Rs '+str(round(total,2)))
                   break
                else:
                    print("False")
                    pass
               
        else:
            len2=len(desc)
            for s in range(len2):
                
                if desc[s].cget('text')==i:
                    total=total-k
                    
                    label7.config(text='Rs '+str(round(total,2)))
                    desc[s].config(text='')
                    desc1[s].config(text='')
                    desc[s].destroy()
                    desc1[s].destroy()
                    del desc[s]
                    del desc1[s]
                                     
                    
                    no_items-=1
                    label6.config(text=str(no_items))
                    break
                else:
                    pass

  
    val_dec=int(quantity[b].cget('text'))
    if val_dec>0:
     
        val_dec-=1
     
     
        quantity[b].config(text=str(val_dec))
        
        cart(m,int(quantity[b].cget('text')),prices1[b],b)
     
    else:
        pass                    
        
# Description

list1=['Strepsils Lozenges - Ginger & Lemon', 'Crocin 650mg', 'Dolo 650 Tablet 15S','Thyronorm 50mcg']
prices1=[510.00,33.50,30.80,140.50]
# Images 

image=Image.open('strepsils.jpg')
img=image.resize((400, 150))
my_img=ImageTk.PhotoImage(img,master=win)

image1=Image.open('crocin.jpg')
img1=image1.resize((400,150))
my_img1=ImageTk.PhotoImage(img1,master=win)

image2=Image.open('dolo.jpg')
img2=image2.resize((400,150))
my_img2=ImageTk.PhotoImage(img2,master=win)

image3=Image.open('thyronorm.jpg')
img3=image3.resize((400,150))
my_img3=ImageTk.PhotoImage(img3,master=win)

# List of Images
images1=[my_img,my_img1,my_img2,my_img3]

#Dynamically create frames and add all the widgets
z=0
for i in range(4):
    frame1=Frame(win,bg='white',width=800,height=150)
    frame1.place(x=10,y=10+z)
    
    label1=Label(frame1,image=images1[i],height=100,width=200)
    label1.place(x=10,y=10)
    
    btn1=Button(frame1,text=list1[i],activebackground='white',bd=0,cursor='hand2',bg='white',fg='black',font=("Arial",15))
    btn1.place(x=250,y=10)
     
    cost='Rs '+str(prices1[i])
    label2=Label(frame1,text=cost,bg='white',fg='black')
    label2.place(x=250,y=85)
    
    btn_dec=Button(frame1,text='-')
    btn_dec.place(x=700,y=105)
    
    label3=Label(frame1,text='0',bg='white',fg='black')
    label3.place(x=725,y=105)
    
    btn_inc=Button(frame1,text='+')
    btn_inc.place(x=750,y=105)
    
   # *************************************************************
    
    frames.append(frame1)
    labels.append(label1)
    btns.append(btn1)
    values.append(label2)
    add_to_cart_dec.append(btn_dec)
    add_to_cart_inc.append(btn_inc)
    quantity.append(label3)
    z+=175
    
    if btn_inc.cget('text')=='+' and btn1.cget('text')==list1[0]:
        btn_inc.config(command=lambda:inc(0,list1[0]))
    
    if btn_inc.cget('text')=='+' and btn1.cget('text')==list1[1]:
        btn_inc.config(command=lambda:inc(1,list1[1]))
        
    if btn_inc.cget('text')=='+' and btn1.cget('text')==list1[2]:
        btn_inc.config(command=lambda:inc(2,list1[2]))
    
    if btn_inc.cget('text')=='+' and btn1.cget('text')==list1[3]:
        btn_inc.config(command=lambda:inc(3,list1[3]))    
    
    
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[0]:
        btn_dec.config(command=lambda :dec(0,list1[0]))
    
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[1]:
        btn_dec.config(command=lambda: dec(1,list1[1]))
        
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[2]:
        btn_dec.config(command=lambda :dec(2,list1[2]))
    
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[3]:
        btn_dec.config(command=lambda: dec(3,list1[3]))
    

win.mainloop()
