#A Project Based On Restaurant Billing Management System.
import mysql.connector
import datetime
from time import sleep
#Title....
def title():
    '''
    a='Welcome to \'Y-OUR RESTRAUNT\''.center(96)
    print(a)
    print()
    '''
    js='\u0332'.join("Welcome to \'Y-OUR RESTRAUNT\'")
    jel=js.center(124)
    print(jel)

# Profile....
def profile():
    global nm
    nm=input('Please enter your name. ')
    global pswd
    pswd=input('Please enter your sql password. ')
    print('Thank You....')
# quick....
def quick(dct):
    dct_ch=dct
    print()
    print()
    print()
    print('Please enter the SNo. of the dish you would like to have.')
    allow="Y"
    while allow=='Y' or allow=='y':
        ch=int(input("What do you like to have ~ "))
        h=dct_ch[ch]
        l=len(h)
        g=1
        if l==3:
            [a,b,c]=dct_ch[ch]
            print('Please enter 1 for half plate. ')
            print('please enter 2 for full plate. ')
            plate=int(input("Which quantity of plate do you want? "))
            if plate==1:
                d="Half"
                item=[a,b,d,g]
                current_item(item)
                Sum.append(b)
                allow=input('Would you like to have more items...[Y/N]')   
            elif plate==2:
                e='Full'
                item=[a,c,e,g]
                current_item(item)
                Sum.append(c)
                allow=input('Would you like to have more items...[Y/N]')
            elif plate!=1 and plate!=2:
                print('Wrong choice....')
                print('Please enter again....')
                pass
        elif l==2:
            h='Normal'
            [a,b]=dct_ch[ch]
            item=[a,b,h,g]
            current_item(item)
            Sum.append(b)
            allow=input('Would you like to have more items...[Y/N]')
# Ease....
def ease():
    cont=input("If you want to see the menu please click [Y/N]").upper()
    if cont=='Y':
        pass
    elif cont=='N':
        global start
        start="F"
    else:
        print("Wrong choice.")
        choice=13
# Tools....
def current_item(item):
    global s
    s=s+1
    global current
    current.update({s:item})
    return(current)
def show_current():
    print('\u0332'.join('Your current order ~ '))
    print()
    head=f"{'SNO.':4s}{gap}{'Food':34s}{gap}{'Plate':7s}{gap}{'Price':4s}{gap}{'Quantity':4s}"
    print(head)
    for i in current.keys():
        [d,e,f,g]=current[i]
        test1=f"{i:4d}{gap}{d:34s}{gap}{f:7s}{gap}{e:4d}{gap}{g:4d}"
        print(test1)    
def edit():
    dc=show_current()
    ed=int(input("Please enter the SNo. of the item that you want to remove. "))
    current.pop(ed)
    print('your order is edited. ')
    print()
    print()
    print('Now you order will be ~')
    show_current()
#SQL....
# Bill.... 
def bill():
    ls=[]
    sv=mysql.connector.connect(
    host='localhost',           # Replace with your host
    user='root',       # Replace with your username
    password='Root@123',   # Replace with your password
)
    cr=sv.cursor()
    cr.execute('create database restraunt;')
    cr.execute('use restraunt;')
    cr.execute('create table bil(plate varchar(7),food varchar(50),price int,Quantity int);')
    for i in current.keys():
        [d,e,f,g]=current[i]
        ls=[f,d,e,g]
        cm="insert into bil (plate,food,price,Quantity) values(%s,%s,%s,%s)"
        cr.execute(cm,ls)
        sv.commit()
# Layout....
    mk="-"*95
    print(mk)
    ret="RETAIL INVOICE".center(96)
    print(ret)
    rst='Y-OUR RESTRAUNT'.center(96)
    print(rst)
    adr='XYZ market , New Delhi 110035'.center(96)
    print(adr)
    mob='Mobile No.~ 701XXXXXX8'.center(96)
    print(mob)
    gst="GST No.~ O7AYXYACBAD1"
    print(gap,gst)
#Base....    
    mk="-"*89
    print('   ',mk,'   ')
    print(gap,"Name: ",nm)
    mk="-"*89
    print('   ',mk,'   ')
    dt=datetime.datetime.now()
    yr=dt.strftime("%Y")
    mn=dt.strftime("%m")
    day=dt.strftime("%d")
    today= day +"/"+ mn +"/"+ yr
    print(gap,"Date: ",today,'                      Dine Ln=1 ')
    print(gap,"Cashier: Biller                         Bill NO.=7 ")
    print(gap,"Token No.: 17")
    mk="-"*89
    print('   ',mk,'   ')
# bill orders.....
    ls=["Item","Plate","Quantity","Amount"]
    [x,y,z,a]=ls
    sp="      "
    test1=f"{gap}{x:34s}{gap}{y:8s}{gap}{z:4s}{gap}{a:4s}{gap}"
    print(test1)
    j5="select distinct plate,food,price,quantity from bil;"
    cr.execute(j5)
    j8=cr.fetchall()
    ls1=list(j8)
    cr.execute('create database restra;')
    cr.execute('use restra;')
    cr.execute('create table bill(plate varchar(7),food varchar(50),price int,Quantity int);')
    for i in current.keys():
        [d,e,f,g]=current[i]
        ls=[f,d,e,g]
        cm="insert into bill (plate,food,price,Quantity) values(%s,%s,%s,%s)"
        cr.execute(cm,ls)
        sv.commit()
    for J in j8:
        (a,b,c,d)=J
        ls=[]
        ls.append(b)
        sp="          "
        if a=="Half":
            hb='select distinct food from bill;'
            cr.execute(hb)
            ha=cr.fetchall()
            cr.execute('use restra;')
            fqs1='select sum(quantity) from bill where food=%s and plate="Half";'
            cr.execute(fqs1,ls)
            fsm1=cr.fetchone()
            fas1='select sum(price) from bill where food=%s and plate="Half";'
            cr.execute(fas1,ls)
            fam1=cr.fetchone()
            test2=f"{gap}{b:34s}{gap}{a:7s}{gap}{fsm1[0]:4f}{sp}{fam1[0]:4f}{gap}"
            print(test2)
        elif a=="Full":
            hb='select distinct food from bill;'
            cr.execute(hb)
            ha=cr.fetchall()
            cr.execute('use restra;')
            fqs1='select sum(quantity) from bill where food=%s and plate="Full";'
            cr.execute(fqs1,ls)
            fsm1=cr.fetchone()
            fas1='select sum(price) from bill where food=%s and plate="Full";'
            cr.execute(fas1,ls)
            fam1=cr.fetchone()
            test2=f"{gap}{b:34s}{gap}{a:7s}{gap}{fsm1[0]:4f}{sp}{fam1[0]:4f}{gap}"
            print(test2)
        elif a=='Normal':
            hb='select distinct food from bill;'
            cr.execute(hb)
            ha=cr.fetchall()
            cr.execute('use restra;')
            half=[J,"Half"]
            fqs1='select sum(quantity) from bill where food=%s and plate="Normal";'
            cr.execute(fqs1,ls)
            fsm1=cr.fetchone()
            fas1='select sum(price) from bill where food=%s and plate="Normal";'
            cr.execute(fas1,ls)
            fam1=cr.fetchone()
            test2=f"{gap}{b:34s}{gap}{a:7s}{gap}{fsm1[0]:4f}{sp}{fam1[0]:4f}{gap}"
            print(test2)
    mk="-"*89
    print('   ',mk,'   ')
    sv.commit()
#SUM....
    cr.execute('select sum(price) from bill;')
    sm=cr.fetchone()
    mk="-"*89
    print('   ',mk,'   ')
    sm=sm[0]
    space="                                             "
    print(space,"Sub Total:         ",sm)
    ST=sum(Sum)
    servcr=ST*0.1
    vat=ST*0.2
    servtx=ST*0.05
    GT=ST+servcr+vat+servtx
    print(space,"Service charge:    ",servcr)
    print(space,"VAT(20%):          ",vat)
    print(space,"Service Tax:       ",servtx)
    print(space,"Grand Total:       ",GT)
    mk="-"*89
    print('   ',mk,'   ')
    z='FSSAI Lic No. 133114XXXXXX80'
    j1=z.center(96)
    print(j1)
    t="Thanks For Your Visit."
    j2=t.center(96)
    print(j2)
    sv.commit()
    mk="-"*95
    print(mk)
    cr.execute("drop database restra;")
    cr.execute("drop database restraunt;")        
    cr.close()    
#Dishes....
def chaat():
    print()
    print()
    dct_ch={1:['Paani Puri\(6 pcs\)',45,90],2:['Bhalla Papri Chaat',90,180],3:['Dahi Bhalla',80,160],4:['Papri Chaat',70,140],5:['Raj Kachori',90,180],6:['Aloo Tikki',60,120],7:['Dahi Puri',60,120],8:['Sev Puri',70,140],9:['Bhelpuri',75,150],10:['Lacha Tokri Chaat',90,180]}
    print('Chaat=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
def snacks():
    print()
    print()
    dct_ch={1:['French Fries',90,180],2:['Margherita Pizza',180,360],3:['Onion Capsicum Pizza',170,340],4:['Pepperoni Pizza',190,380],5:['Farmhouse Pizza',180,360],6:['Golden Corn Pizza',170,340],7:['White Sauce Pasta',180,360],8:['Red Sauce Pasta',160,320],9:['Veg Grilled Sandwich',140,280],10:['Grilled Paneer Tikka Sandwhich',170,340],11:['Chole Bhature',90,180],12:['Matar Kulcha',90,180],13:['Pav Bhaji',90,180],14:['Moong Dal Laddoo',40,80],15:['Kachuri',15,30],16:['Samosa',15,30],17:['Paneer Pakoda',30,60],18:['Bread Pakoda',20,40],19:['Paneer Bread Pakoda',30,60],20:['Dhokla',200,400],21:['Khandvi',300,600]}
    print('Snacks=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
def south_indian():
    print()
    print()
    dct_ch={1:['Idli Sambhar',80,160],2:['Sambhar Vada',80,160],3:['Plain Dosa',80,160],4:['Masala Dosa',110,220],5:['Plain Rawa Dosa',130,260],6:['Uttpam',130,260],7:['Rawa Masala Dhosa',150,300],8:['Paneer Dosa',150,300],9:['Annakoot Special Dosa',180,360]}
    print('South Indian=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
def chin():
    print()
    print()
    dct_ch={1:['Fried Rice',90,180],2:['Hakka Noodles',100,200],3:['Manchurian',90,180],4:['Chilli Paneer',110,220],5:['Chilli Potato',120,240],6:['Spring Roll',100,200],7:['Noodles',100,200],8:['chowmein',110,220]}
    print('Chinese dishes=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
def north_indian():
    print()
    print("North Indian Dishes")
    print("Please enter. ")
    print("1 for Sabzi. ")
    print("2 for Tandoori Roti. ")
    ch=int(input("What do you like to have ~ "))
    if ch==1:
        sabzi()
    if ch==2:
        tandoori_se()
    per=input("Would you like have anything else from North Indian Dishes[Y/N]. ").upper()
    if per=='Y':
        north_indian()
        
def sabzi():
    print()
    print()
    dct_ch={1:['Dal Makhni',220,440],2:['Shahi Paneer',250,500],3:['Chana Masala',220,440],4:['Tandoori Aloo',220,440],5:['Peas Pulao',150,300],6:['Raita',100,200],7:['Salad',90,180]}
    print('North Indian=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
def tandoori_se():
    print()
    print()
    dct_ch={1:['Plain Roti',10],2:['Rumali Roti',15],3:['Missi Roti',20],4:['Plain Naan',20],5:['Butter Naan',25],6:['Soya Naan',40]}
    print('Tandoori Roti=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Price':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}"
        print(test1)
    quick(dct_ch)    
def thaali_combo():
    print()
    print()
    dct_ch={1:['Dal Makhni with Rice & Raita',350],2:['Panner Makhni with Rice & Raita',370],3:['Chana Masala with Rice & Raita',350],4:['Annakoot Special Thali',400]}
    print('Thaali Combos=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Price':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}"
        print(test1)
    quick(dct_ch)
def beverages():
    print()
    print()
    dct_ch={1:['Areated Water',20],2:['Lassi',30],3:['Kesar Badam Milk',35],4:['Expresso/Cold Coffee',80],5:['Fresh Lime Soda',60],6:['Chocolate Shake',100],7:['Oreo Shake',120],8:['Mango Shake',100],9:['Mixed Fruit Juice',90],10:['Orange Juice',90],11:['Sunrise',60],12:['Golden Gate',90],13:['Tropical Sunset',70],14:['Blue Ocean',70],15:['Tomato Soup',60],16:['Veg Sweet Corn Soup',60],17:['Veg Hot N sour soup',60],18:['Veg Manchow Soup',70]}
    print('Beverages=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Price':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}"
        print(test1)
    quick(dct_ch)
def dessert():
    print()
    print()
    dct_ch={1:['Rasgulla',30,60],2:['Gulab Jamun',40,80],3:['Ras Malai',70,140],4:['Plain Kulfi',50,100],5:['Faluda Kulfi',90,180],6:['Choco Lava Cake',100,200], 7:['Brownie',110,220],8:['Black Truffle',120,240]}
    print('Deserts=>')
    head=f"{'SNO.':4s}{gap}{'Food':34}{gap}{'Half':4s}{gap}{'Full':4s}{gap}"
    print(head)
    for key in dct_ch.keys():
        [x,y,z]=dct_ch[key]
        test1=f"{key:4d}{gap}{x:34s}{gap}{y:4d}{gap}{z:4d}{gap}"
        print(test1)
    quick(dct_ch)
                
# Main coding....
title()
profile()
gap='   '
s=0
Sum=[]
current={}
j16='\u0332'.join("Menu ")
j17=j16.center(96)
start="t"
while start=="t":
    sleep(1)
    print()
    print()
    print('\u0332'.join('what would you like to have ~'))
    print()
    print(j17)
    print()
    print("1 for Chaat. ")
    print("2 for Snacks. ")
    print("3 for South Indian Dish. ")
    print("4 for North Indian Dish. ")
    print("5 for Chinese Dish. ")
    print("6 for Thaali Combo. ")
    print("7 for beverages. ")
    print("8 for Dessert. ")
    print("9 to check your current orders. ")
    print("10 to edit your orders . ")
    print("11 for your bill. ")    
    print("12 to Quite. ")
    print()
    choice=int(input("Please enter your choice. "))
    if choice==1:
        sleep(0.5)
        chaat()        
    elif choice==2:
        sleep(0.5)
        snacks()
    elif choice==3:
        sleep(0.5)
        south_indian()        
    elif choice==4:
        sleep(0.5)
        north_indian()                
    elif choice==5:    
        sleep(0.5)
        chin()
    elif choice==6:
        sleep(0.5)
        thaali_combo()
    elif choice==7:
        sleep(0.5)
        beverages()
    elif choice==8:
        sleep(0.5)
        dessert()        
    elif choice==9:
        show_current()
        ease()
    elif choice==10:
        sleep(0.5)
        edit()
        ease()
    elif choice==11:
        sleep(0.5)
        bill()
        ease()
    elif choice==12:
        sleep(0.5)
        start="F"
        pass
if start=="F":
    print("Thank You for coming and keep coming back for such a delicious meal !")
