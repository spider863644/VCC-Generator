import random
import os
import time as t
os.system("apt install figlet")
os.system("clear")
print("\033[5;31;4mDisclaimer: Use this script only for educational purposes only and testing purposes\nWe won't be held for any fucken shit\n\nYou can't use this card for carting")
t.sleep(6)
os.system("clear")
print("""\033[0;32;40mContributors:
Spider Anongreyhat
AnonyminHack5""")
t.sleep(4)
os.system("clear")
def loop():
    os.system("clear")
    #colors
    red = "\033[1;31;40m"
    yellow = "\033[1;33;40m"
    global green
    green = "\033[1;32;40m"
    global white
    white = "\033[0;37;40m"
    #BG colors
    global redd
    redd = "\033[0;33;41m"
    print(yellow)
    os.system("figlet VCC-Generator")
    print(white)
    print(green + """
    [+] Tool Name: Valid Credit Card Generator
    [+] Creator: AnonyminHack5 & Spider Anongreyhat
    [+] Team: TermuxHackz Society
    [+] Github: https://github.com/spider863644
    [+] Team Github: https://github.com/TermuxHackz
    [+] WhatsApp: +2349052863644
    """ + white)
    print(redd + "≠≠≠≠≠≠≠≠≠≠≠≠CHOOSE A CREDIT CARD NETWORK TO GENERATE≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠" + white)
    print(green + """
    [1]Visa
    [2]Mastercard
    [3]American Express(Unavailable)
    """ + white)
    print(red + "===================================================" + white)
    print(green + """[00]Update Script  [J]Join my WhatsApp group""" + white)
    print(red + "===================================================" + white)
    cc = input(yellow + "$ " + white)
    if cc == "1":
        print(green +"Generating card info..." + white)
        t.sleep(5)
        #Credit Card Random Bin for Visa
        rand1 = 4
        rand2 = random.randrange(1, 8) 
        rand3 = random.randrange(2, 8) 
        rand4 = random.randrange(3, 8)
        rand5 = random.randrange(0, 8)
        rand6 = random.randrange (1, 8)
       #Random Credit Card Account Number
        acc1 = random.randrange(1, 4)
        acc2 = random.randrange(5, 7)
        acc3 = random.randrange(0, 6)
        acc4 = random.randrange(2, 5)
        acc5 = random.randrange(7, 8)
        acc6 = random.randrange(6, 8)
        acc7 = random.randrange(1, 5)
        acc8 = random.randrange(3, 7)
        acc9 = random.randrange(4, 6)
       #Doubling Even position
        aa = ((rand1 * 2)%9) 
        bb = ((rand3 * 2)%9)
        cc = ((rand5 *2)%9)
        a = ((acc1 * 2 )% 9) 
        b = ((acc3 * 2 )% 9) 
        c = ((acc5 * 2) % 9) 
        d = ((acc7 * 2) % 9) 
        e = ((acc9 * 2)% 9)
       #Sum digits
        Rand1 = aa
        Rand2 = rand2
        Rand3 = bb
        Rand4 = rand4
        Rand5 = cc
        Rand6 = rand6
        Acc1 = a
        A = acc2
        Acc3 = b
        B = acc4
        Acc5 = c
        C = acc6
        Acc7 = d
        D = acc8
        Acc9 = e
        #add sum digit to get check number
        acc = Rand1 + Rand2 + Rand3 + Rand4 + Rand5 + Rand6 + Acc1 + A + Acc3 + B +Acc5 + C + Acc7 + D + Acc9
        checkSum = ((acc * 9)% 10)
        #Converting all Data to string
        ran1 = str(rand1)
        ran2 = str(rand2)
        ran3 = str(rand3) 
        ran4 = str(rand4) 
        ran5 = str(rand5) 
        ran6 = str(rand6)
        za = str(acc1)
        za1 = str(acc2)
        za2 = str(acc3)
        za3 = str(acc4)
        za4 = str(acc5)
        za5 = str(acc6)
        za6 = str(acc7)
        za7 = str(acc8)
        za8 = str(acc9)
        check = str(checkSum)
        #Joining all cc number together
        ccnumber = ran1 + ran2 + ran3 + ran4 + ran5 + ran6 + za + za1 + za2 + za3 + za4 + za5 + za6 + za7 + za8 + check
        global cvv
        cvv = random.randrange(354, 958)
        global mm
        mm = random.randrange(1, 12)
        global yy
        yy = random.randrange(22, 25)
        print(yellow + """
       §§§§§§§§§§§§§§§§§§§Card Details§§§§§§§§§§§§§§§§§§§
        Card number: """, ccnumber, """
        CVV: """, cvv, """
        Expiry Date: MM:""", mm, """ YY:""",yy,  white)
    elif cc == "2":
        #Credit Card bin for MasterCard
        bin1 = 5
        bin2 = random.randrange (0, 5) 
        bin3 = random.randrange(1, 8)
        bin4 = random.randrange (3, 7) 
        bin5 = random.randrange(0, 4)
        bin6 = random.randrange (1, 6)
        #Account Number for MasterCard
        acc1 = random.randrange(1, 9)
        acc2 = random.randrange(2, 4)
        acc3 = random.randrange(3, 6)
        acc4 = random.randrange(4, 8)
        acc5 = random.randrange(2, 9)
        acc6 = random.randrange(4, 9)
        acc7 = random.randrange(6, 9)
        acc8 = random.randrange(3, 7)
        acc9 = random.randrange(2, 6)
        #Doubling all even positions
        aa = ((bin1 * 2)%9)
        bb = ((bin3 * 2)%9)
        cc = ((bin5 * 2)%9)
        dd = ((acc1 * 2)%9)
        ee = ((acc3 * 2)%9)
        ff = ((acc5 *2)%9)
        gg = ((acc7 * 2)%9)
        hh = ((acc9 * 2)%9)
        #sum digit
        RAND1 = aa
        RAND2 = bin2
        RAND3 = bb
        RAND4 = bin4
        RAND5 = cc
        RAND6 = bin6
        RAND7 = dd
        RAND8 = acc2
        RAND9 = ee
        RAND10 = acc4
        RAND11 = ff
        RAND12 = acc6
        RAND13 = gg
        RAND14 = acc8
        RAND15 = hh
        #add sum digit to check digit
        acc = RAND1 + RAND2 + RAND3 + RAND4 + RAND5 + RAND6 + RAND7 + RAND8 + RAND9 + RAND10 + RAND11 + RAND12 + RAND13 + RAND14 + RAND15
        CheckSum = ((acc * 9)% 10)
        #Converting data to stringtype
        RAND1 = str(bin1)
        RAND2 = str(bin2)
        RAND3 = str(bin3)
        RAND4 = str(bin4)
        RAND5 = str(bin5)
        RAND6 = str(bin6)
        RAND7 = str(acc1)
        RAND8 = str(acc2)
        RAND9 = str(acc3)
        RAND10 = str(acc4)
        RAND11 = str(acc5)
        RAND12 = str(acc6)
        RAND13 = str(acc7)
        RAND14 = str(acc8)
        RAND15 = str(acc9)
        CheckSum = str(CheckSum)
        #Joining all cc numbers together
        ccnumber = RAND1 + RAND2 + RAND3 + RAND4 + RAND5 + RAND6 + RAND7 + RAND8 + RAND9 + RAND10 + RAND11 + RAND12 + RAND13 + RAND14 + RAND15 + CheckSum
        cvv = random.randrange(316, 790)
        yy = random.randrange(23, 30)
        mm = random.randrange(1, 12)
        dd = random.randrange(1, 31) 
        print(green + "Generating card info...")
        t.sleep(4)
        print(yellow + "$$$$$$$$$$$$$$$$$$$$$$$$$$$$CARD DETAILS$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\nCard Number: ", ccnumber, "\nCVV: ", cvv, "\nExpiry Date: DD", dd, "MM: ", mm, "YY: ", yy, white)
    elif cc == "00":
        os.system("clear")
        print(redd + "Updating Script" + white)
        t.sleep(5)
        os.system("""
        cd
        rm -f -r VCC-Generator
        git clone https://github.com/spider863644/VCC-Generator
        clear""")
        print(yellow + """
        Now type the following commands
        cd $HOME
        cd VCC-Generator
        python3 VCC.py
        """ + white)
        exit()
        
    elif cc == "3":
        print(red + "Not available at the moment!" + white)
        t.sleep(3)
        loop()
    elif cc == "J" or cc == "j":
        os.system("xdg-open https://chat.whatsapp.com/BivW6pA9Emu9bDM2rZkaQy")
        exit()
    else:
        print (red + " invalid option" + white)
        t.sleep(3)
        loop()
    cont = input (redd + "Do you wanna continue?[y/n]? " + white)
    if cont == "y" or cont == "Y":
        loop()
    else:
        exit()
loop()