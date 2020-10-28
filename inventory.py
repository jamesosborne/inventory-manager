#Importing Modules
import time
from tkinter import *
import csv
import sys


#Creating Item class
class Item:
    def __init__(self, name, price, itemid, quantity):
        self.name = name
        self.price = price
        self.itemid = itemid
        self.quantity = quantity


#Creating Inventory class
class Inventory(Item):
    def __init__(self,root):
        self.root = root
        self.root.title("Inventory Manager")
        self.root.geometry("600x500+0+0")
        self.root.configure(background="powder blue")
        self.root.resizable(0, 0)
        self.photo = PhotoImage(file = "icon.png")
        self.root.iconphoto(False, self.photo)
        self.items = []
        

        #----------------------------------FRAMES--------------------------------------------------------------#

        MainFrame = Frame(self.root , bd=20, width=600, height=700, bg="cadet blue", relief=RIDGE)
        MainFrame.grid()

        appFrame = Frame(MainFrame , bd=10, width=560, height=600, bg="powder blue", padx=10, relief=RIDGE)
        appFrame.pack(side=LEFT)
        

        #-----------------------Frames for: Text, Labels, Entry Widget-----------------------------------------#


        appFrame0 = Frame(appFrame , bd=5, width=522, height=200, bg="powder blue", padx=5, relief=RIDGE)
        appFrame0.grid(row=0, column=0)

        appFrame1 = Frame(appFrame , bd=5, width=522, height=280, bg="powder blue", padx=5, relief=RIDGE)
        appFrame1.grid(row=1, column=0)
        

        appFrame2 = Frame(appFrame , bd=5, width=522, height=95, bg="powder blue", padx=5, relief=RIDGE)
        appFrame2.grid(row=3, column=0)

        appFrame3 = Frame(appFrame , bd=5, width=522, height=95, bg="powder blue", padx=5, relief=RIDGE)
        appFrame3.grid(row=4, column=0)
        

         
        #-----------------------Text, Labels, Entry Widget-----------------------------------------------------#
 
        self.console = Text(appFrame1, height=20, width=71, font=('arial', 9, 'bold'))
        self.console.grid(row=0, column=0)

        self.lblConsole = Label(appFrame0, font=('arial', 18, 'bold'), text="Inventory Console:", padx=2, pady=2,
                                bg="powder blue")
        self.lblConsole.grid(row=0, column=0, sticky=W)

        self.lblValue = Label(appFrame3, font=('arial', 18, 'bold'), text="Inventory Value:", padx=2, pady=2,
                               bg="powder blue")
        self.lblValue.grid(row=0, column=0)

        self.lblValue1 = Label(appFrame3, font=('arial', 18, 'bold'), text="", padx=2, pady=2,
                               bg="powder blue")
        self.lblValue1.grid(row=0, column=1)
        

        #---------------------------------Buttons--------------------------------------------------------------#

        self.btnValue = Button(appFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'), width=9,
                               bg="powder blue", text="Calculate Value", command=self.calculate_value, state=NORMAL).grid(row=0, column=0)

        self.btnInventory = Button(appFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'), width=9,
                               bg="powder blue", text="Inventory", command=self.display_inventory, state=NORMAL).grid(row=0, column=1)

        self.btnReset = Button(appFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'), width=9,
                               bg="powder blue", text="Reset", command=self.reset, state=NORMAL).grid(row=0, column=2)

        self.btnExit = Button(appFrame2, padx=18, pady=2, bd=4, fg="black", font=('arial', 9, 'bold'), width=9,
                               bg="powder blue", text="Exit", command=exit).grid(row=0, column=3)

               
    def reset(self):
        self.console.delete(0.0, END)

    #Adds item to inventory item list
    def add_item(self, item):
        self.items.append(item)

    def load_items(self, file_to_load):
        with open(file_to_load, 'r', encoding='utf-8', errors='ignore') as f:
            f.readline()
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                self.items.append(Item(row[0],row[1],row[2],row[3]))
        


  
        
    #Removes item from inventory item list
    def remove_item(self, item):
        time.sleep(1.5)
        print("Removing item...")
        time.sleep(1.5)
        print("Item succesfully removed.")
        self.items.remove(item)
        
    #Shows items in inventory
    def display_inventory(self):
        for item in self.items:
            temp = "ID:" + str(item.itemid) + "  Item name: " + str(item.name) + "  Price: £" + str(item.price) + "  Quantity: " + str(item.quantity)+ "\n"
            self.console.insert(0.0, temp)
            

    #Calculates value of inventory
    def calculate_value(self):
        value = 0
        for item in self.items:
            temp = int(item.price) * int(item.quantity)
            value = value + temp
        valuetext = "£" + str(value)
        self.lblValue1['text'] = valuetext
        
  
        

    #Checks that item is in stock
    def in_stock(self, item):
        if item.quantity >= 1:
            return True
        else:
            return False

    def exit(self):
        sys.exit()



if __name__== '__main__':
    root = Tk()
    application = Inventory(root)
    application.load_items('items.csv')
    root.mainloop()

    




 
