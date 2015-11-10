#!/usr/bin/python3
import random

Distance = 10000

h = "hp"
s = "shields"
a = "armor"
e = "engine"
r = "reactor"
m = "missiles"
gd = "gunDamage"
gr = "gunRange"
md = "missileDamage"
mr = "missileRange"
xn = "actorName"
yn = "acteeName"

all_ships = {
  "Yours":      { h: 1250, s: 1500, a:  0, e: 50, r: 50, m:  5, gd: 200, gr: 5000, md: 150, mr: 9000 },
  "Freighter":  { h:  500, s:  200, a:  0, e: 20, r: 50, m:  0, gd: 100, gr: 2500, md:   0, mr:    0 }, 
  "Slipstream": { h: 1000, s: 1000, a: 10, e: 60, r: 50, m: 20, gd: 200, gr: 4000, md: 175, mr: 9500 },
  "Nemisis":    { h: 1000, s: 1250, a: 10, e: 60, r: 50, m: 50, gd: 190, gr: 5000, md: 180, mr: 9100 },
  "Avenger":    { h: 1250, s: 1000, a: 10, e: 25, r:100, m:  0, gd: 210, gr: 5100, md: 150, mr: 8900 },
  "Bastion":    { h: 2000, s: 1500, a: 25, e: 20, r: 50, m: 25, gd: 200, gr: 5000, md: 150, mr: 9000 },
  "Legion":     { h: 1500, s: 2000, a: 17, e: 25, r: 50, m: 10, gd: 200, gr: 5000, md: 150, mr: 9000 },
}
enemy_ships=["Freighter", "Slipstream", "Nemisis", "Avenger", "Bastion", "Legion"]
you = dict(all_ships["Yours"])
you[xn] = "You"
you[yn] = "your"
you["score"] = 0
foe = dict(all_ships[enemy_ships[random.randint(0, len(enemy_ships))]])
foe[xn] = "They"
foe[yn] = "their"
foe["score"] = 0

def do_damage(x, y, dam):
    if y[s] > 0:
        if dam > y[s]:
            dam -= y[s]
            y[s] = 0
        else:
           y[s] -= dam
        print(x[xn], "hit", ship[yn], " shields.")
    dam -= y[a]
    if dam > 0:
        y[h] -= dam
        x["score"] += 1
        print( x[xn], "damaged", y[yn], "hull.")

def fire_guns(x, y):
    if Distance > x[gr]:
        print(x[xn], "fire guns and miss.")
    else:
        do_damage(you, foe, you[gd])

def fire_missiles(x, y):
    if x[m] > 0:
        x[m] -= 1
        if Distance <= x[mr]:
           do_damage(x, y, x[md])
        else:
            print(x[xn], "fire missiles and miss.")
    else:
        print(x[xn], "are out of missiles.")

def advance(x, y):
    global Distance
    if Distance > x[e]:
        Distance =- x[e]
        print(x[xn], "have advanced.")
    else:
        Distance = 0
        print (x[xn], "have rammed.")
    
def retreat(x, y):
    global Distance
    Distance += x[e]
    print(x[xn], "have retreated.")

def quit(x, y):
    x[h] = 0

commands = {
  "fire_guns": fire_guns,
  "fire_missiles": fire_missiles,
  "advance": advance,
  "retreat": retreat,
  "quit": quit
}

while you[h] > 0 and foe[h] > 0:
    action = input("There is a ship. What do you do?")
    if action in commands:
        commands[action](you, foe)

    if Distance > (foe[mr] if foe[m] > 0 else foe[gr]):
        advance(foe, you)
    elif distance <= foe[gr]:
        fire_guns(foe, you)
    elif foe[m] > 0 and distance <= foe[mr]:
        fire_missiles(foe, you)

if you[h] < 1:
    print("You have lost")
    print("Your score is ", str(you["score"]), ".", sep = "")
elif foe[h] < 1:
    print ("You have won")



