from tkinter import *
from tkinter import messagebox
import random

billNumber = random.randint(500, 5000)


# functions
def total():
    bathSoap = int(bathSoapEntry.get()) * 20
    faceCream = int(faceCreamEntry.get()) * 20
    faceWash = int(faceWashEntry.get()) * 20
    hairSpray = int(hairSprayEntry.get()) * 20
    hairGel = int(hairGelEntry.get()) * 20
    bodyLotion = int(bodyLotionEntry.get()) * 20

    totalCosmeticsPrice = (
        bathSoap + faceCream + faceWash + bodyLotion + hairGel + hairSpray
    )
    cosmeticsPriceEntry.delete(0, END)
    cosmeticsPriceEntry.insert(0, totalCosmeticsPrice)

    cosmeticsTaxEntry.delete(0, END)
    cosmeticsTaxEntry.insert(0, totalCosmeticsPrice * 0.12)

    rice = int(riceEntry.get()) * 20
    oil = int(oilEntry.get()) * 20
    daal = int(daalEntry.get()) * 20
    wheat = int(wheatEntry.get()) * 20
    sugar = int(sugarEntry.get()) * 20
    tea = int(teaEntry.get()) * 20

    totalGroceryPrice = rice + oil + daal + wheat + sugar + tea
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0, totalGroceryPrice)

    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, totalGroceryPrice * 0.15)

    maaza = int(maazaEntry.get()) * 20
    pepsi = int(pepsiEntry.get()) * 20
    sprite = int(spriteEntry.get()) * 20
    dew = int(dewEntry.get()) * 20
    frooti = int(frootiEntry.get()) * 20
    cocacola = int(cocalcolaEntry.get()) * 20

    totalDrinksPrice = maaza + pepsi + sprite + dew + frooti + cocacola
    drinksPriceEntry.delete(0, END)
    drinksPriceEntry.insert(0, totalDrinksPrice)

    drinksTaxEntry.delete(0, END)
    drinksTaxEntry.insert(0, totalDrinksPrice * 0.15)

    pass


def bill_area():
    if nameEntry.get() == "" or phoneEntry.get() == "":
        messagebox.showerror("Errors", "Please Provide details")
    elif (
        cosmeticsPriceEntry.get() == ""
        or groceryPriceEntry.get() == ""
        or drinksPriceEntry.get() == ""
    ):
        messagebox.showerror("Errors", "Please select products")
    elif (
        cosmeticsPriceEntry.get() == 0
        and groceryPriceEntry.get() == 0
        and drinksPriceEntry.get() == 0
    ):
        messagebox.showerror("Errors", "Please select products")
    else:
        textArea.insert(END, "---Welcome Customer--\n")
        textArea.insert(END, f"Bill Number : {billNumber}\n")
        textArea.insert(END, f"Customer Name: {nameEntry.get()}\n")
        textArea.insert(END, f"Customer Phone No.: {phoneEntry.get()}\n")

        textArea.insert(END, "---------------------------------------\n")
        textArea.insert(END, "Product\t\tQTY\t\tPrice\n")
        textArea.insert(END, "---------------------------------------\n")

        
    pass


# Root
root = Tk()
root.title("Retail Billing System")
root.geometry("1478x685")
root.iconbitmap("bill.ico")

# Widgets
""" 
The Top Level: Here will be a top title. 
the next row will contain the name, phone and bill number
"""
headingLabel = Label(
    root,
    text="Retail Billing System",
    font=("times new roman", 30, "bold"),
    bg="gray20",
    fg="gold",
    bd=12,
    relief="groove",
)
headingLabel.pack(fill=X)

customerDetailsFrame = LabelFrame(
    root,
    text="Customer Details",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
customerDetailsFrame.pack(fill=X)


# Name Entry
nameLabel = Label(
    customerDetailsFrame,
    text="Name:",
    font=("times new roman", 15, "bold"),
    fg="white",
    bg="gray20",
)
nameLabel.grid(row=0, column=0, padx=20, pady=2)

nameEntry = Entry(customerDetailsFrame, font=("arial", 14), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)


# phoneLabel Entry
phoneLabel = Label(
    customerDetailsFrame,
    text="Phone:",
    font=("times new roman", 15, "bold"),
    fg="white",
    bg="gray20",
)
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customerDetailsFrame, font=("arial", 14), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)


# Bill No. Entry
billNumberLabel = Label(
    customerDetailsFrame,
    text="Bill No.:",
    font=("times new roman", 15, "bold"),
    fg="white",
    bg="gray20",
)
billNumberLabel.grid(row=0, column=4, padx=20, pady=2)

billNumberEntry = Entry(customerDetailsFrame, font=("arial", 14), bd=7, width=18)
billNumberEntry.grid(row=0, column=5, padx=8)

# Search BUtton
searchButton = Button(
    customerDetailsFrame, text="Search", font=("arial", 14, "bold"), bd=7, width=10
)
searchButton.grid(row=0, column=6, padx=20, pady=8)


""" 
Mid level. Here will be 4 containers inside a parent frame which will be inside the root.
"""
productsFrame = Frame(root)
productsFrame.pack()

# Cosmetics
cosmeticsFrame = LabelFrame(
    productsFrame,
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
cosmeticsFrame.grid(row=0, column=0, sticky="w")

bathSoapLabel = Label(
    cosmeticsFrame,
    text="Bath Soap :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bathSoapLabel.grid(row=0, column=0, padx=10, sticky="w")
bathSoapEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
bathSoapEntry.grid(row=0, column=1, padx=10)
bathSoapEntry.insert(0, 0)

faceCreamLabel = Label(
    cosmeticsFrame,
    text="Face Cream :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceCreamLabel.grid(row=1, column=0, padx=10, sticky="w")
faceCreamEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
faceCreamEntry.grid(row=1, column=1, padx=10)
faceCreamEntry.insert(0, 0)

faceWashLabel = Label(
    cosmeticsFrame,
    text="Face Wash :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceWashLabel.grid(row=2, column=0, padx=10, sticky="w")
faceWashEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
faceWashEntry.grid(row=2, column=1, padx=10)
faceWashEntry.insert(0, 0)

hairSprayLabel = Label(
    cosmeticsFrame,
    text="Hair Spray :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairSprayLabel.grid(row=3, column=0, padx=10, sticky="w")
hairSprayEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
hairSprayEntry.grid(row=3, column=1, padx=10)
hairSprayEntry.insert(0, 0)

hairGelLabel = Label(
    cosmeticsFrame,
    text="Hair Gel :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairGelLabel.grid(row=4, column=0, padx=10, sticky="w")
hairGelEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
hairGelEntry.grid(row=4, column=1, padx=10)
hairGelEntry.insert(0, 0)

bodyLotionLabel = Label(
    cosmeticsFrame,
    text="Body Lotion :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bodyLotionLabel.grid(row=4, column=0, padx=10, sticky="w")
bodyLotionEntry = Entry(cosmeticsFrame, font=("arial", 14), bd=7, width=18)
bodyLotionEntry.grid(row=4, column=1, padx=10)
bodyLotionEntry.insert(0, 0)

# Groceries
groceryFrame = LabelFrame(
    productsFrame,
    text="Groceries",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
groceryFrame.grid(row=0, column=1, sticky="w")

riceLabel = Label(
    groceryFrame,
    text="Rice :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
riceLabel.grid(row=0, column=0, padx=10, sticky="w")
riceEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
riceEntry.grid(row=0, column=1, padx=10)
riceEntry.insert(0, 0)

oilLabel = Label(
    groceryFrame,
    text="Oil :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
oilLabel.grid(row=1, column=0, padx=10, sticky="w")
oilEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
oilEntry.grid(row=1, column=1, padx=10)
oilEntry.insert(0, 0)

daalLabel = Label(
    groceryFrame,
    text="Daal :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
daalLabel.grid(row=2, column=0, padx=10, sticky="w")
daalEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
daalEntry.grid(row=2, column=1, padx=10)
daalEntry.insert(0, 0)

wheatLabel = Label(
    groceryFrame,
    text="wheat :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
wheatLabel.grid(row=3, column=0, padx=10, sticky="w")
wheatEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
wheatEntry.grid(row=3, column=1, padx=10)
wheatEntry.insert(0, 0)

sugarLabel = Label(
    groceryFrame,
    text="sugar :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
sugarLabel.grid(row=4, column=0, padx=10, sticky="w")
sugarEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
sugarEntry.grid(row=4, column=1, padx=10)
sugarEntry.insert(0, 0)

teaLabel = Label(
    groceryFrame,
    text="Tea:",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
teaLabel.grid(row=4, column=0, padx=10, sticky="w")
teaEntry = Entry(groceryFrame, font=("arial", 14), bd=7, width=18)
teaEntry.grid(row=4, column=1, padx=10)
teaEntry.insert(0, 0)

# Drinks
drinksFrame = LabelFrame(
    productsFrame,
    text="Drinks",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
drinksFrame.grid(row=0, column=2, sticky="w")


maazaLabel = Label(
    drinksFrame,
    text="Maaza :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
maazaLabel.grid(row=0, column=0, padx=10, sticky="w")
maazaEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
maazaEntry.grid(row=0, column=1, padx=10)
maazaEntry.insert(0, 0)

pepsiLabel = Label(
    drinksFrame,
    text="Pepsi:",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
pepsiLabel.grid(row=1, column=0, padx=10, sticky="w")
pepsiEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
pepsiEntry.grid(row=1, column=1, padx=10)
pepsiEntry.insert(0, 0)

spriteLabel = Label(
    drinksFrame,
    text="Sprite:",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
spriteLabel.grid(row=2, column=0, padx=10, sticky="w")
spriteEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
spriteEntry.grid(row=2, column=1, padx=10)
spriteEntry.insert(0, 0)

dewLabel = Label(
    drinksFrame,
    text="Dew :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
dewLabel.grid(row=3, column=0, padx=10, sticky="w")
dewEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
dewEntry.grid(row=3, column=1, padx=10)
dewEntry.insert(0, 0)

frootiLabel = Label(
    drinksFrame,
    text="Frooti :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
frootiLabel.grid(row=4, column=0, padx=10, sticky="w")
frootiEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
frootiEntry.grid(row=4, column=1, padx=10)
frootiEntry.insert(0, 0)

cocalcolaLabel = Label(
    drinksFrame,
    text="Coca Cloa:",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cocalcolaLabel.grid(row=4, column=0, padx=10, sticky="w")
cocalcolaEntry = Entry(drinksFrame, font=("arial", 14), bd=7, width=18)
cocalcolaEntry.grid(row=4, column=1, padx=10)
cocalcolaEntry.insert(0, 0)

# Bill Area
billFrame = Frame(productsFrame)
billFrame.grid(row=0, column=3)

billAreaLabel = Label(
    billFrame,
    text="Bill Area:",
    font=("times new roman", 15, "bold"),
    bd=7,
    relief="groove",
)
billAreaLabel.pack(fill="x")

srcollbar = Scrollbar(billFrame, orient="vertical")
srcollbar.pack(side="right", fill="y")

textArea = Text(billFrame, height=11, width=45, yscrollcommand=srcollbar.set)
textArea.pack()

srcollbar.config(command=textArea.yview)

# Prices #taxes
pricesFrame = LabelFrame(
    productsFrame,
    text="Prices",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
pricesFrame.grid(row=1, columnspan=8, column=0, sticky="w")

buttonFrame = Frame(pricesFrame, bg="gray20", bd=8, relief="groove")
buttonFrame.grid(row=0, rowspan=3, column=4, columnspan=3, sticky="wens")

#
cosmeticsLabel = Label(
    pricesFrame,
    text="Cosmetics Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cosmeticsLabel.grid(row=0, column=0, padx=10, sticky="w")
cosmeticsPriceEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
cosmeticsPriceEntry.grid(row=0, column=1, padx=10)
cosmeticsPriceEntry.insert(0, 0)

groceryLabel = Label(
    pricesFrame,
    text="Grocery Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
groceryLabel.grid(row=1, column=0, padx=10, sticky="w")
groceryPriceEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
groceryPriceEntry.grid(row=1, column=1, padx=10)
groceryPriceEntry.insert(0, 0)

drinksLabel = Label(
    pricesFrame,
    text="Drinks Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
drinksLabel.grid(row=2, column=0, padx=10, sticky="w")
drinksPriceEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
drinksPriceEntry.grid(row=2, column=1, padx=10)
drinksPriceEntry.insert(0, 0)


# taxes
cosmeticsTaxLabel = Label(
    pricesFrame,
    text="Cosmetics Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cosmeticsTaxLabel.grid(row=0, column=2, padx=10, sticky="w")
cosmeticsTaxEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
cosmeticsTaxEntry.grid(row=0, column=3, padx=10)
cosmeticsTaxEntry.insert(0, 0)

groceryTaxLabel = Label(
    pricesFrame,
    text="Grocery Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
groceryTaxLabel.grid(row=1, column=2, padx=10, sticky="w")
groceryTaxEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
groceryTaxEntry.grid(row=1, column=3, padx=10)
groceryTaxEntry.insert(0, 0)

drinksTaxLabel = Label(
    pricesFrame,
    text="Drinks Price :",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
drinksTaxLabel.grid(row=2, column=2, padx=10, sticky="w")
drinksTaxEntry = Entry(pricesFrame, font=("arial", 14), bd=7, width=15)
drinksTaxEntry.grid(row=2, column=3, padx=10)
drinksTaxEntry.insert(0, 0)

# buttons
totalButton = Button(
    buttonFrame,
    text="Total",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=8,
    relief="groove",
    command=total,
)
totalButton.grid(row=0, column=0, padx=5, pady=20, sticky="wens")

billButton = Button(
    buttonFrame,
    text="Bill",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=8,
    relief="groove",
    command=bill_area,
)
billButton.grid(row=0, column=1, padx=5, pady=20, sticky="wens")

emailButton = Button(
    buttonFrame,
    text="Email",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=8,
    relief="groove",
)
emailButton.grid(row=0, column=2, padx=5, pady=20, sticky="wens")

printButton = Button(
    buttonFrame,
    text="Print",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=8,
    relief="groove",
)
printButton.grid(row=0, column=3, padx=5, pady=20, sticky="wens")


clearButton = Button(
    buttonFrame,
    text="Clear",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=8,
    relief="groove",
)
clearButton.grid(row=0, column=4, padx=5, pady=20, sticky="wens")


root.mainloop()
