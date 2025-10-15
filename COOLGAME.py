import os
import time

text1 = "It smelled of filth, it smelled of disease, it smelled of deatrh. " * 3 # Repeat the text to make it long
text2 = "Quedate quieta, carino. Tu cabeza hermosa sera enviada a tu padre. " * 3 #same as before
text3 = "Only the Revelator does not fear the monsters in the dark, and I am HIM. "
screen_width = 80 # Standard console width

#while True:
os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
for i in range(len(text1) + screen_width):
    start = i - screen_width
    end = i
    print(text1[max(0, start):end].rjust(screen_width))
    time.sleep(0.05)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for i in range(len(text2) + screen_width):
    start = i - screen_width
    end = i
    print(text2[max(0, start):end].rjust(screen_width))
    time.sleep(0.05)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for n in range(5):
    print(text3)
    time.sleep(0.05)
time.sleep(1.0)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
print("You shouldn't be here...")
time.sleep(2.0)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
for x in range(30,0,-1):
    print(str(x) + "...\n")
    time.sleep(1.0)
os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen again
print("I am going to get you now!")