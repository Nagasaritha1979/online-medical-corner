from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

win=Tk()
win.geometry('1000x800')
win.title('MED PHARMA')



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
no_of_times=0
label_details=[]
label_details_1=[]

# CART
tp=Toplevel(win)

tp.title("CART")

tp.geometry("500x500")


def inc(number,medicine):

    def cart(med,quant,price,num):
        
        global tp,total,g,cart_desc,cart_cal,label_details,label_details_1,no_items,no_of_times,total_price,no_of_items
        
        if quant>1:
            length=len(label_details)
            
            for o in range(length):
                
                if label_details[o].cget('text')==med:
                    text2="Rs "+str(price)+'*'+str(quant)
                    
                    label_details_1[o].config(text=text2)
                    
                    total=total+price
                    total_price.config(text='Rs '+str(round(total,2)))
                    
            
              
            
            
        else:
            
            cart_desc=Label(tp,text=med)
            cart_desc.grid(row=0+g,column=0)
            
            label_details.append(cart_desc)
            
            
            text1='Rs ' +str(price) +'*'+str(quant)
            
            cart_cal=Label(tp,text=text1)
            cart_cal.grid(row=0+g,column=1)
            
            label_details_1.append(cart_cal)
            
            no_items+=1
            
            total=total+price

            no_of_items=Label(tp,text=str(no_items)) 
            no_of_items.grid(row=20,column=0)
            
            if no_of_times==0:
                
                total_price=Label(tp, text='',fg='red')                                  
                total_price.grid(row=22,column=1)
                
                
            total_price.config(text="Rs "+str(round(total,2)))  
            g=g+1
            no_of_times+=1

    val_inc=int(quantity[number].cget('text'))
    val_inc+=1

    quantity[number].config(text=str(val_inc))
    
    cart(medicine,int(quantity[number].cget('text')), prices1[number],number)


def dec(number1,medicine1):
    
    def cart(med,quant,price,num):
        global tp,total,g,cart_desc,cart_cal,label_details,label_details_1,no_items,no_of_times,total_price,no_of_items
        
        if quant>=1:
            
            len1=len(label_details)
            
            for f in range(len1):
                
                if label_details[f].cget('text')==med:
                    
                    text3='Rs '+str(price)+'*'+str(quant)
                    
                    label_details_1[f].config(text=text3)
        
                    total=total-price
                    
                    total_price.config(text='Rs ' +str(round(total,2)))
                    
                    break
                else:
                    pass
                
                
        else:
            
            len2=len(label_details)
            
            for s in range(len2):
                
                if label_details[s].cget('text')==med:
                    
                    total=total-price
                    total_price.config(text='Rs '+str(round(total,2)))
    
                    label_details[s].config(text='')
                    label_details_1[s].config(text='')
                    
                    label_details[s].destroy()
                    label_details_1[s].destroy()
                    
                    
                    del label_details[s]
                    del label_details_1[s]

                    no_items-=1
                    no_of_items.config(text=str(no_items))
                    break
                
                else:
                    pass

                    
                    
                    
                    
    val_dec=int(quantity[number1].cget('text'))
    if val_dec >0:
        
        val_dec-=1
        quantity[number1].config(text=str(val_dec))
        
        cart(medicine1,int(quantity[number1].cget('text')),prices1[number1],number1)

# Description

list1=['Strepsils Lozenges','Crocin 650mg','Dolo 650','Thyronorm 50mcg']
prices1=[510.00,33.50,30.80,140.50]


# Images


image=Image.open('strepsils.jpg')
img=image.resize((400,150))
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

#List of Images

images1=[my_img,my_img1,my_img2,my_img3]

z=0

for i in range(4):
    
    frame1=Frame(win,bg='white',width=800,height=150)
    frame1.place(x=10,y=10+z)
    
    label1=Label(frame1,image=images1[i],height=100,width=200)
    label1.place(x=10,y=10)

    btn1=Button(frame1,text=list1[i],activebackground='white',bg='white',fg='black',bd=0,cursor='hand2',font=("Arial",15))
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
        btn_dec.config(command=lambda:dec(0,list1[0]))
        
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[1]:
        btn_dec.config(command=lambda:dec(1,list1[1]))

    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[2]:
        btn_dec.config(command=lambda:dec(2,list1[2]))
        
        
    if btn_dec.cget('text')=='-' and btn1.cget('text')==list1[3]:
        btn_dec.config(command=lambda:dec(3,list1[3]))
    
        

win.mainloop()
