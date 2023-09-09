import turtle
import webbrowser


military_budget_aug31 = "12 Diamonds, two diamond chestplates, one diamond leggings, 2 iron boots, 1 chainmail boots, and one iron helmet."
military_budget_sep1 = "8 Diamonds, two diamond chestplates, one diamond leggings, 2 iron boots, 1 chainmail boots, and one iron helmet."
military_budget_sep2 = "8 Diamonds, two diamond chestplates, one diamond leggings, 2 iron boots, 1 chainmail boots, and one iron helmet"
military_budget_change_aug31_sep1 = "4 Diamonds Spent On Beds For Netherite Hunting"
military_mission_sep1_exports = "12 ancient debris"

architecture_budget_aug31 = "20 Diamonds"
architecture_budget_sep1 = "20 Diamonds"
architecture_budget_sep2 = "20 Diamonds"

diplomacy_budget_aug31 = "14 Iron"
diplomacy_budget_sep1 = "14 Iron"
diplomacy_budget_sep2 = "14 Iron"

def help():
    print("Military Abbreviation - Mil | ", "Architecture Abbreviation - Arc | ", "Diplomacy Abbreviation - Dip | ", "Mining Abbreviation - Mine.")
    print(" ")
    print("to find everything that happened in a certain month use the command 'find_events_(month)_(year)()'  example- 'find_events_august_2023()'  and it will show you dates of interest.")
    print(" ")
    print("to list everything that happened in a day use the command 'list_events_(month)_(day)_(year)'  example- 'list_events_august_31_2023()' and it will tell you everything that happened that date.")
    print(" ")



def find_events_august_2023():
    print(" ")
    print(" 'military_budget_aug31' ")
    print(" ")
    print(" 'military_budget_change_aug31_sep1")
    print(" ")
    print(" 'architecture_budget_aug31' ")
    print(" ")
    print(" 'diplomacy_budget_aug31' ")
    print(" ")


def find_events_september_2023():
    print(" ")
    print(" 'military_budget_sep1' ")
    print(" ")
    print(" 'military_budget_change_aug31_sep1")
    print(" ")
    print(" 'military_mission_sep1_exports' ")
    print(" ")
    print(" 'military_budget_sep2' ")
    print(" ")
    print(" 'architecture_budget_sep1' ")
    print(" ")
    print(" 'architecture_budget_sep2' ")
    print(" ")
    print(" 'diplomacy_budget_sep1' ")
    print(" ")
    print(" 'diplomacy_budget_sep2' ")
    print(" ")


def list_events_august_31_2023():
    print(" ")
    print("military_budget_aug31", "=", military_budget_aug31)
    print(" ")
    print("military_budget_change_aug31_sep1", "=", military_budget_change_aug31_sep1)
    print(" ")
    print("architecture_budget_aug31", "=", architecture_budget_aug31)
    print(" ")
    print("diplomacy_budget_aug31", "=", diplomacy_budget_aug31)
    print(" ")


def list_events_september_1_2023():
    print(" ")
    print("military_budget_sep1", "=", military_budget_sep1)
    print(" ")
    print("military_budget_change_aug31_sep1", "=", military_budget_change_aug31_sep1)
    print(" ")
    print("architecture_budget_sep1", "=", architecture_budget_sep1)
    print(" ")
    print("diplomacy_budget_sep1", "=", diplomacy_budget_sep1)
    print(" ")


def list_events_september_2_2023():
    print(" ")



#Netherite & Diamond Items (Must Be Logged Under All Circumstances)
aug31_netherite_items = "steve's netherite sword"
sep1_netherite_items = "steve's netherite sword, kasen's netherite pickaxe, kasen's netherite leggings, and kasen's netherite chestplate"


win = turtle.Screen()
win.title("Help")
win.bgcolor("white")
win.setup(width=600, height=400)
score = turtle.Turtle()
score.speed(0), score.color("black"), score.penup(), score.hideturtle(), score.goto(0, 170), score.write("To navigate the database use the command 'help()' ", align="center", font=("Arial", 15, "normal"))
turtle.Screen().exitonclick()

