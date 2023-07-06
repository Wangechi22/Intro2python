#Using for loop print valus for the dictionary below:
# my_dic= {"Apple:2.99", "Banana":1.50, "Orange':0.99", "Grape":3.50, "Waterlemon":5.99, "Pineapple":4.99}

my_dic = {"Apple":2.99, "Banana":1.50,"Orange":0.99, "Grape":3.50, "Waterlemon":5.99, "Pineapple":4.99}
for fruit, price in my_dic.items():
    print(fruit,price)