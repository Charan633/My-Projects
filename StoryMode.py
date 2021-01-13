answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
sword = 0
flower = 0
required = ("\nUse only A, B, or C\n") 
def intro():
  print ("After a late night party with your friends, you find a thick, dank forest on your way back home. Head aching and feeling very sleepy,"
  "you stand and stare into the darkness of the unfamiliar setting. The peace quickly fades when you hear a gruesome voice coming from behind you."
  "A mysterious and quite huge creature is running towards you. You will:")
  print ("""  A. Grab a nearby rock and throw it at the creature
  B. Lie down and wait to be mauled
  C. Run""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()
def option_rock(): 
  print ("\nThe monster is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "creature's head. You missed. \n\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()
def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "creepy. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1
  else:
    sword = 0
  print ("\nWhat do you do next?")
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "they can see very well in the dark because...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the monster, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As it "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: 
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As it enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the creature turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the monster's "
  "speed is too great. You will:")
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
          print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for it. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:

    
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a demolished building, waiting for it to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending monster")
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop it. It does! It was apparently looking "
    "for friendship. "
    "\n\nThis got weird, but you survived!")
  else: 
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")
intro()
