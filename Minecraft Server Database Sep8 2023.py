import turtle
import time
import math
import subprocess
import tkinter as tk
from tkinter import filedialog
import webbrowser


#this top part is a tutorial for myself lol
# print(len(example)) = print digit of how long the variable is
# print(example.find("example2")) finds where a letter is in a variable
# print(example.capitalize()) capitalizes the first letter in a variable
# print(example.upper()) capitalizes all letters in a variable
# print(example.lower()) lowercases all letters in a variable
# print(example.isdigit()) checks if variable is digit in a T/F statement
# print(example.isalpha()) checks if variable is only letters (doesnt include spaces so if spaces it will say no)
# print(example.count("example2,must be letter")) counts how many of one character are in variable
# print(example.replace("example2, must be letter,is one we replacing","example3, must be letter, is one we replacing other one with")) changes a specific letter of a variable
# print(example*example2, must be number) repeats variable as many times as you want

#STOCK MARKET HEHEHEHA

#Aug31st (stock market gets updated once every 3 days/1 taxxing period)
wool_aug31_inflation = "Wool Inflation, Wool is now worth 10 pieces of iron in the Rat Kingdom"
wool_aug31_dywk = "type the command 'wool_info_inflation_aug31()' to learn why inflation happened."
gunpowder_aug31_inflation = "Gunpowder Inflation, Gunpowder is now worth 3 pieces of iron in the Rat Kingdom"
gunpowder_aug31_dywk = "type the command 'gunpowder_info_inflation_aug31()' to learn why inflation happened."
tnt_aug31_inflation = "TNT Inflation, TNT is now worth 15 pieces of iron in the Rat Kingdom"
tnt_aug31_dywk = "type the command 'tnt_info_inflation_aug31()' to learn why inflation happened."
tnt_norm_price_aug31 = "For Example TNT is normally priced around 3-5 Iron Ingots In The Rat Kingdom, But You Must Have A Permit To Buy It."
gold_aug31_deflation = "Gold has deflated extremely with its normal price being 5 iron ingots, it is now 2 in the Rat Kingdom"
gold_aug31_dywk = "type the command 'gold_info_deflation_aug31()' to learn why deflation happened"
expansion_big_kasen_aug31 = "Kasen's Trading Shop has expanded greatly now being the #1 shop in the server, you can buy close to anything there."
expansion_kasen_aug31_dywk = "type the command 'k_expansion_aug13()' to learn what happened"

wool_aug31_inflate = "Due to a huge wool shortage wool is now worth 10 pieces of iron in the Rat Kingdom, this also means string is inflated too."

gunpowder_aug31_inflate = "Due to ancient debris hunting TNT and it's component gunpowder have now skyrocketed in price"

tnt_aug31_inflate = "Due to ancient debris hunting TNT and it's component gunpowder have now skyrocketed in price"

gold_aug31_deflate = "Due to Kasen's Trading Shop having more than 7 stacks of gold ingots, gold has deflated in price a lot"

def wool_info_inflation_aug31():
    print(wool_aug31_inflate)




def gunpowder_info_inflation_aug31():
    print(gunpowder_aug31_inflate)




def tnt_info_inflation_aug31():
    print(tnt_aug31_inflate)




def gold_info_deflation_aug31():
    print(gold_aug31_deflate) 




def inflated_aug31():
    print(wool_aug31_inflation)
    print(wool_aug31_dywk)
    print(gunpowder_aug31_inflation)
    print(gunpowder_aug31_dywk)
    print(tnt_aug31_inflation)
    print(tnt_aug31_inflation)
    print(tnt_norm_price_aug31)




def deflated_aug31():
    print(gold_aug31_deflation)
    print(gold_aug31_dywk)




Space = " "

Finley1 = "Finley Doiron"
Elle1 = "Elle Floyd"
Kasen1 = "Kasen Francis"
Hunter1 = "Hunter Hopper"
Tristan1 = "Tristan Johnson"
Aveen1 = "Aveen Nixon"
Alex1 = "Alex Ostendorf"
Cooper1 = "Cooper Rhinehart"
Tristen1 = "Tristen Roney"
Jada1 = "Jada Scapin"
Foster1 = "Foster Worley"




def member_list():
    print(Space)
    print(Finley1)
    print(Space)
    print(Elle1)
    print(Space)
    print(Kasen1)
    print(Space)
    print(Hunter1)
    print(Space)
    print(Tristan1)
    print(Space)
    print(Aveen1)
    print(Space)
    print(Alex1)
    print(Space)
    print(Cooper1)
    print(Space)
    print(Tristen1)
    print(Space)
    print(Jada1)
    print(Space)
    print(Foster1)




kasen_diamonds_aug31 = 115
kasen_gold_ingots_aug31 = 484
kasen_iron_ingots_aug31 = 204
kasen_copper_ingots_aug31 = 226
kasen_lapis_aug31 = 594
kasen_redstone_dust_aug31 = 1597
kasen_amethyst_aug31 = 184
kasen_netherite_scrap_aug31 = 3
kasen_netherite_ingot_aug31 = 0
kasen_netherite_pickaxe_crafted_aug31 = 1

news_sep5 = "The Rat Kingdom made a creeper farm and is now the number 1 producer of gunpowder in the world"

gunpowder_producer_sep2 = "There is no gunpowder producer in the world"
gunpowder_producer_sep3 = "There is no gunpowder producer in the world"
gunpowder_producer_sep4 = "There is no gunpowder producer in the world"
gunpowder_producer_sep5 = "The Rat Kingdom is the NO. 1 gunpowder producer in the world on September 5th"
gunpowder_producer_sep6 = "The Rat Kingdom is the NO. 1 gunpowder producer in the world on September 6th"
gunpowder_producer_sep7 = "The Rat Kingdom is the NO. 1 gunpowder producer in the world on September 7th" 
gunpowder_producer_sep8 = "The Rat Kingdom is the NO. 1 gunpowder producer in the world on September 8th" 

gunpowder_producer_sep1 = "There is no gunpowder producer in the world"
creeper_farm_sep_5 = "The Rat Kingdom Made A Creeper Farm On September 5 2023."
kasen_netherite_chestplate_crafted_sep3 = 1
kasen_netherite_leggings_crafted_sep3 = 1
kasen_netherite_helmet_crafted_sep4 = 1
kasen_netherte_helmet_crafted_sep4 = 1

news_sep6_2023_continued = "Kasen Foster Trading co. is the number 1 producer of mending and sharpness books in the world"

news_sep6_2023_ = "Foster and Kasen have merged trading companies to form ‘Kasen Foster trading co.’"

def news_sep6_2023():
	print(" ")
	print(news_sep6_2023_)
	print(" ")
	print(news_sep6_2023_continued)




def sep6_2023_news():
	print(" ")
	print(news_sep6_2023_)
	print(" ")
	print(news_sep6_2023_continued)



def gunpowder_producer_records():	
    print(" ")
    print(gunpowder_producer_sep1)
    print(" ")
    print(gunpowder_producer_sep2)
    print(" ")
    print(gunpowder_producer_sep3)
    print(" ")
    print(gunpowder_producer_sep4)
    print(" ")




aug31_diamond = "kasen_diamonds_aug31 = 115"
aug31_gold = "kasen_gold_ingots_aug31 = 484"
aug31_iron = "kasen_iron_ingots_aug31 = 204"
aug31_copper = "kasen_copper_ingots_aug31 = 226"
aug31_lapis = "kasen_lapis_aug31 = 594"
aug31_redstone = "kasen_redstone_dust_aug31 = 1597"
aug31_amethyst = "kasen_amethyst_aug31 = 184"
aug31_netherite_scrap = "kasen_netherite_scrap_aug31 = 3"
aug31_netherite_ingot = "kasen_netherite_ingot_aug31 = 0"
aug31_netherite_pickaxe = "kasen_netherite_pickaxe_crafted_aug31 = 1"

foster_taxes_aug31 = "Foster Paid 9 Diamonds Worth Of Taxes On August 31"
tristan_taxes_aug31 = "Tristan Paid No Taxes On August 31"
hunter_taxes_aug31 = "Hunter Paid 11 Diamonds Worth Of Taxes On August 31"
aveen_taxes_aug31 = "Aveen Paid No Taxes On August 31"
tristen_taxes_aug31 = "Tristen Paid No Taxes On August 31"

foster_diamonds_aug31 = "Foster's Diamonds - 132"
foster_diamonds_sep1 = "Foster's Diamonds - 132"
foster_diamonds_sep2 = "Foster's Diamonds - 132"
foster_diamonds_sep3 = "Foster's Diamonds - 130"

foster_iron_tab_aug31 = "Foster's Tab (Iron) - 0"
foster_iron_tab_sep1 = "Foster's Tab (Iron) - 0"
foster_iron_tab_sep2 = "Foster's Tab (Iron) - 0" 
foster_iron_tab_sep3 = "Foster's Tab (Iron) - 12"

foster_diamonds_tab_aug31 = "Foster's Tab (Diamonds) - 0"
foster_diamonds_tab_sep1 = "Foster's Tab (Diamonds) - 0"
foster_diamonds_tab_sep2 = "Foster's Tab (Diamonds) - 0"
foster_diamonds_tab_sep3 = "Foster's Tab (Diamonds) - 2, Was Paid Same Day."

aveen_taxes_owe_aug31 = "Aveen Owes No Taxes On August 31"
aveen_tax_evasion_strikes_aug31 = "Aveen Has 0 Out Of 3 Strikes Against Tax Evasion On August 31"
tristan_taxes_owe_aug31 = "Tristan Owes Taxes On August 31"
tristan_tax_evasion_strikes_aug31 = "Tristan Has 1 Out Of 3 Strikes Against Tax Evasion On August 31"
tristen_taxes_owe_aug31 = "Tristen Owes No Taxes On August 31"
tristen_tax_evasion_strikes_aug31 = "Tristen Has 0 Out Of 3 Strikes Against Tax Evasion On August 31"
foster_taxes_owe_aug31 = "Foster Owes No Taxes On August 31"
foster_tax_evasion_strikes_aug31 = "Foster Has 0 Out Of 3 Strikes Against Tax Evasion On August 31"
hunter_taxes_owe_aug31 = "Hunter Owes No Taxes On August 31"
hunter_tax_evasion_strikes_aug31 = "Hunter Has 0 Out Of 3 Strikes Against Tax Evasion On August 31"

def taxes_aug31 ():
    print(aveen_taxes_owe_aug31)
    print(aveen_tax_evasion_strikes_aug31)
    print(tristan_taxes_owe_aug31)
    print(tristan_tax_evasion_strikes_aug31)
    print(tristen_taxes_owe_aug31)
    print(tristen_tax_evasion_strikes_aug31)
    print(foster_taxes_owe_aug31)
    print(foster_tax_evasion_strikes_aug31)
    print(hunter_taxes_owe_aug31)
    print(hunter_tax_evasion_strikes_aug31)



mining_budget_aug31 = ("Mining Budget - 0")
military_budget_aug31 = "Military Budget - 12 diamonds 2 diamond chestplates 1 diamond legging 2 iron boots 1 chainmail boots"

cactus_aug31 = "Cacti - Roughly 425/Day Since September 1st"
kasen_cactus_aug31 = "Kasen Cacti Production Per Day - 425"

war1 = "Rat Kingdom VS Dirt Kingdom, August 2023"
def wars():
    print(war1) 

cactus_farm_produce_per_hour_aug31 = "cactus production - roughly 425 per day"

def kasen_aug31():
    print(aug31_netherite_ingot)
    print(aug31_netherite_scrap)
    print(aug31_netherite_pickaxe)
    print(aug31_diamond)
    print(aug31_amethyst)
    print(aug31_gold)
    print(aug31_redstone)
    print(aug31_lapis)
    print(aug31_iron)
    print(aug31_copper)

def server_news_web():
    webbrowser.open('https://thefatherlands.godaddysites.com/')

def test_aug31():
    print(cactus_farm_produce_per_hour_aug31)
    print(war1)
    print(kasen_cactus_aug31)
    print(cactus_aug31)
    print(military_budget_aug31)
    print(mining_budget_aug31)
    print(aveen_taxes_owe_aug31)
    print(aveen_tax_evasion_strikes_aug31)
    print(tristan_taxes_owe_aug31)
    print(tristan_tax_evasion_strikes_aug31)
    print(tristen_taxes_owe_aug31)
    print(tristen_tax_evasion_strikes_aug31)
    print(foster_taxes_owe_aug31)
    print(foster_tax_evasion_strikes_aug31)
    print(hunter_taxes_owe_aug31)
    print(hunter_tax_evasion_strikes_aug31)
    print(foster_diamonds_aug31)
    print(tristen_taxes_aug31)
    print(aveen_taxes_aug31)
    print(hunter_taxes_aug31)
    print(tristan_taxes_aug31)
    print(foster_taxes_aug31)
    print(aug31_amethyst)
    print(aug31_diamond)
    print(aug31_redstone)
    print(aug31_netherite_scrap)
    print(aug31_lapis)
    print(aug31_iron)
    print(aug31_netherite_ingot)
    print(aug31_netherite_pickaxe)
    print(aug31_gold)
    print(aug31_copper)
    print(wool_aug31_inflation)
    print(wool_aug31_dywk)
    print(gunpowder_aug31_inflation)
    print(gunpowder_aug31_dywk)
    print(tnt_aug31_inflation)
    print(tnt_aug31_inflation)
    print(tnt_norm_price_aug31)
    print(gold_aug31_deflation)
    print(gold_aug31_dywk)
    print(wool_aug31_inflate)
    print(gunpowder_aug31_inflate)
    print(tnt_aug31_inflate)
    print(gold_aug31_deflate)


test0001 = 0
testfailsafe0001 = 1
outdated = 0

def test_sep7():
    wars




def test_outdate1():
    if test0001 == 0:
        if testfailsafe0001 == 0:
            print("hi")
        else:
            print("this command is only availiable for administrators")




test0002 = 0
testfailsafe0002 = 1

def test_authorization():
    if test0002 == 0:
        if testfailsafe0002 == 0:
            test0002_2 = input("test lol?")
            if test0002_2 == "a":
                print("SUCCESS")
        else:
            print("this command is only avaliable for administrators")





test0003 = 0
testfailsafe0003 = 1

def test_authorization1():
    if test0003 == 0:
        if testfailsafe0003 == 0:
            test0003_3 = input("test lol?")
            if test0003_3 == "a" or "A":
                print("SUCCESS")
        else:
            print("this command is only avaliable for administrators")


test0004 = 0
testfailsafe0004 = 1
outdated_test0001 = 1
outdated_test0002 = "This Python Script Might Be Outdated"

def test_outdate_nt():
    if test0004 == 0:
        if testfailsafe0004 == 0:
            if outdated_test0001 == 1:
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(outdated_test0002)
                print(" ")
        else:
            print("this command is only avaliable for administrators")



if outdated == 1:
    win = turtle.Screen()
    win.title("Outdated")
    win.bgcolor("white")
    win.setup(width=600, height=400)
    score = turtle.Turtle()
    score.speed(0)
    score.color("black")
    score.penup()
    score.hideturtle()
    score.goto(0, 170)
    score.write("This Python Script Is Most Likely Outdated.' ", align="center", font=("Arial", 15, "normal"))
    turtle.Screen().exitonclick()
