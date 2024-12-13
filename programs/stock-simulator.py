# this is the first real big project i've tried to make, it's kind of a game

import random
money = 1500

owned_nvidia = 0
owned_ftx = 0
owned_apple = 0

nvidia_price = 130
ftx_price = 210
apple_price = 500

def stocknvidia():
    global money, owned_nvidia, nvidia_price
    x = nvidia_price
    if money > x:
        owned_nvidia += 1
        money -= x
    else:
        print("too broke")
    ran = random.randint(10, 25)
    if ran >= 16:
            x += ran%(x)
    else:
            x-= ran%(x)
    nvidia_price = x
    


def stockftx():
    global money, owned_ftx, ftx_price
    x = ftx_price
    if money > x:
        owned_ftx += 1
        money -= x
    else:
        print("too broke")
    ran = random.randint(10, 100)
    if ran >= 55:
            x += ran%(x)
    else:
            x-= ran%(x)
    ftx_price = x
    

def stockapple():
    global money, owned_apple, apple_price
    x = apple_price
    if money > x:
        owned_apple += 1
        money -= x
    else:
        print("too broke")
    ran = random.randint(5, 15)
    if ran >= 7.5:
            x += ran%(x)
    else:
            x-= ran%(x)
    apple_price = x
    

def sellmenu():
    global money, nvidia_price, ftx_price, apple_price, owned_apple, owned_nvidia, owned_ftx
    selection = int(input("Please select your stock to sell 1 to sell nvidia, 2 to sell ftx, 3 to sell apple. "))
    if selection == 1:
        if owned_nvidia >= 1:
            money += nvidia_price
            x = nvidia_price
            ran = random.randint(10, 25)
            if ran >= 16:
                x += ran%(x)
            else:
                x-= ran%(x)
            nvidia_price = x
            owned_nvidia -= 1
        else:
             print("Nothing to sell!")
        buymenu()
    if selection == 2:
        if owned_ftx >=1:
            money += ftx_price
            x = ftx_price
            ran = random.randint(10, 25)
            if ran >= 16:
                x += ran%(x)
            else:
                x-= ran%(x)
            ftx_price = x
            owned_ftx -= 1
        else: print("Nothing to sell!")
        buymenu()
    if selection == 3:
        if owned_apple >= 1:
            money += apple_price
            x = apple_price
            ran = random.randint(10, 25)
            if ran >= 16:
                x += ran%(x)
            else:
                x-= ran%(x)
            apple_price = x
            owned_apple -= 1
        else: print("Nothing to sell!")
        buymenu()
    if selection >= 4 or selection <= 0:
        print("Invalid input, please retry.")
        buymenu()

def buymenu():
    selection = int(input(
    "Please select your stock to buy, or check currently owned stocks. "
    "1 to buy Nvidia, 2 to buy FTX, 3 to buy Apple, 4 to check currently owned, "
    "5 to check prices, and 6 to open sell menu. "
    f"You currently have {money} money: "
    ))
    if selection == 1:
        stocknvidia()
        buymenu()
    if selection == 2:
        stockftx()
        buymenu()
    if selection == 3:
        stockapple()
        buymenu()
    if selection == 4:
        print("You own",str(owned_nvidia), "Nvidia,", str(owned_ftx), "FTX,","and", str(owned_apple),"Apple.")
        buymenu()
    if selection == 5:
        print("Nvidia", str(nvidia_price), "FTX", str(ftx_price), "Apple", str(apple_price))
        buymenu()
    if selection == 6:
        sellmenu()
    if selection >= 7 or selection <= 0:
        print("Invalid input, retry.")
        buymenu()
    
    
buymenu()
