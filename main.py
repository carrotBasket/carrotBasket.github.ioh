import tkinter as tk
import random
import time

root = tk.Tk()
root.title('RPG game display')
root.geometry('600x500')
root.config(bg='teal')

Health = 100
Money = 500
xp = 0
level = 0
weapon = 'Pistol'
battle = ""  # Initialize the variable

def see_stats():
    print("----------------", "\n", "Health: ", Health, "\n", "Money: ", Money, "\n", "xp: ", xp, "\n", "Level: ", level, "\n", "----------------",)

def attack_or_heal():
    global battle
    # Create the dialog within the function so we can pass it to wait_window
    battle_dialog = tk.Toplevel(root)
    battle_dialog.title("Attack or Heal")
    battle_dialog.geometry('300x100')
    tk.Label(battle_dialog, text="Would you like to attack or heal? A/H: ").pack()
    battle_input = tk.Entry(battle_dialog)
    battle_input.pack()

    def submit_battle():
        global battle
        battle = battle_input.get()
        print(f"Submitted battle choice: {battle}")  # Debugging line
        battle_dialog.destroy()

    tk.Button(battle_dialog, text="Submit", command=submit_battle).pack()
    return battle_dialog  # Return the dialog window so it can be passed to wait_window

def widgets():
    tk.Button(root, text='Press to continue', command=root.withdraw, height=2, width=13, bg='light blue', fg='black').grid(padx=255, pady=50)
    tk.Button(root, text='See Stats', command=see_stats, height=2, width=10, bg='light blue', fg='black').grid(padx=255, pady=0.1)
    tk.Label(root, text='Do not press close tab button').grid(padx=255, pady=3)

widgets()

def play():
    print('W', end="")
    time.sleep(0.3)
    print('e', end="")
    time.sleep(0.3)
    print('l', end="")
    time.sleep(0.3)
    print('c', end="")
    time.sleep(0.3)
    print('o', end="")
    time.sleep(0.3)
    print('m', end="")
    time.sleep(0.3)
    print('e')
    time.sleep(1)
    print("It is the year 3000. Earth is currently in war with an alien species. Your ship crashed in the middle of nowhere. You need to find another ship to get back home.")
    first_action = input("Would you like to find food or water? F/W: ")

    if first_action.lower() == 'f':
        print("While searching for food, you died of dehydration.")
        Health = 0
        see_stats()
        print("GAME OVER")
        print("Rerun Program to Restart")

    elif first_action.lower() == 'w':
        print("You found a nearby spring with plenty of water to drink.")
        global Health, Money, xp, level
        xp += 10
        if xp % 10 == 0:
            level += 1
        see_stats()
        root.withdraw()
        print("Now that you have a source of water, you need food.")
        food_1 = input("You have two choices. Either fight an animal or scavenge for food. F/S: ")
        if food_1.lower() == 'f':
            print("You spot a wolf lying in the shade. You approach it with your pistol that you had with you when the plane crashed. Suddenly, the wolf leaps at you.")
            root.update_idletasks()
            root.deiconify()
            Health -= random.randint(30,50)
            see_stats()
            battle_dialog = attack_or_heal()
            root.wait_window(battle_dialog)  # Wait for the dialog to close before proceeding
            if battle.lower() == 'a':
                enemy_health = random.randint(15, 30)
                enemy_health -= random.randint(5, 10)
                print("Enemy Health ", enemy_health)
                print("Your Health ", Health)
            elif battle.lower() == 'h':
                Health += random.randint(40, 60)
                print('Health ', Health)
play()
root.mainloop()

