import matplotlib.pyplot as plt
import numpy as np





sales_data = [
    {"Hamburger": 150, "French_Fries": 200, "Soda": 180, "Milkshake": 40, "Salads": 30, "McNuggets": 100},
    {"Hamburger": 170, "French_Fries": 220, "Soda": 190, "Milkshake": 50, "Salads": 35, "McNuggets": 105},
    {"Hamburger": 160, "French_Fries": 210, "Soda": 185, "Milkshake": 45, "Salads": 33, "McNuggets": 110},
    {"Hamburger": 180, "French_Fries": 230, "Soda": 200, "Milkshake": 55, "Salads": 40, "McNuggets": 115},
    {"Hamburger": 170, "French_Fries": 220, "Soda": 195, "Milkshake": 50, "Salads": 38, "McNuggets": 120},
    {"Hamburger": 190, "French_Fries": 240, "Soda": 210, "Milkshake": 60, "Salads": 42, "McNuggets": 125},
    {"Hamburger": 185, "French_Fries": 235, "Soda": 205, "Milkshake": 58, "Salads": 40, "McNuggets": 130},
    {"Hamburger": 175, "French_Fries": 225, "Soda": 190, "Milkshake": 52, "Salads": 36, "McNuggets": 120},
    {"Hamburger": 165, "French_Fries": 215, "Soda": 185, "Milkshake": 48, "Salads": 34, "McNuggets": 110},
    {"Hamburger": 180, "French_Fries": 230, "Soda": 200, "Milkshake": 55, "Salads": 39, "McNuggets": 115}
]
sales_profit = {"Hamburger": 50, "French_Fries": 25, "Soda": 20, "Milkshake": 30, "Salads": 45, "McNuggets": 35}
diagram = []


daynum = 0 
lengthoflist = 0 


for sales_data in sales_data:
    daynum += 1 
    

    totalsales = sales_data["Hamburger"] * sales_profit["Hamburger"]
    totalsales += sales_data["French_Fries"] * sales_profit["French_Fries"]
    totalsales += sales_data["Soda"] * sales_profit["Soda"]
    totalsales += sales_data["Milkshake"] * sales_profit["Milkshake"]
    totalsales += sales_data["Salads"] * sales_profit["Salads"]
    totalsales += sales_data["McNuggets"] * sales_profit["McNuggets"]
    diagram.append(totalsales)
    print(f'Days: {daynum}, Money Earned: {totalsales}')
    
   




ypoints = np.array(diagram)
xpoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.plot(ypoints, xpoints, marker = 'D')
plt.show()


    




    


