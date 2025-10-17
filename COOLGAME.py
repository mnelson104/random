import os
import time
import sys

text1 = "It smelled of filth, it smelled of disease, it smelled of death. " * 3 # Repeat the text to make it long
text2 = "Quèdate quieta, cariño. Tu cabeza hermosa serà enviada a tu padre. " * 2 #same as before
text3 = "Only the Revelator does not fear the monsters in the dark, and I am HIM. "
screen_width = 80 # Standard console width

#while True:
os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
for i in range(len(text1) + screen_width):
    start = i - screen_width
    end = i
    print(text1[max(0, start):end].rjust(screen_width))
    time.sleep(0.02)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for i in range(len(text2) + screen_width):
    start = i - screen_width
    end = i
    print(text2[max(0, start):end].rjust(screen_width))
    time.sleep(0.02)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for n in range(5):
    print(text3)
    time.sleep(0.25)
time.sleep(1.0)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
print("You shouldn't be here...")
time.sleep(1.0)
print(" You have 30 seconds to find another person, or you will die!")
time.sleep(1.0)
os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for x in range(30,0,-1):
    print(str(x) + "...\n")
    time.sleep(0.75)
os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
answer = input("If you survived, click Y: ")
print("Oh no! The ghost is still with you! On Halloween, the curse will be broken - but ONLY after a year of fear!")
time.sleep(5.0)
sys.exit(0)