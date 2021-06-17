f = open("input.txt","w")
f.writelines("Hi my name is mahir")
f.close()
f = open("input.txt","r")
print(f.readline())
f.close()

#import os
#os.remove("input.txt")

f = open("input1.txt","w")
f.writelines("Hi my name is mahir. How is it going? Do u have any special item left in the shop right now?")
f.close()
f = open("input1.txt","r")
print(f.readline())
f.close()

#import os
#os.remove("input1.txt")

f = open("input2.txt","w")
f.writelines('''Hi my name is mahir. How is it going? Do u have any special item left in the shop right now? cause i need some good products. So try to understand. Get me a good product. ''')
f.close()
f = open("input2.txt","r")
print(f.readline())
f.close()

import os
os.remove("input2.txt")

f = open("friends.txt","w")
lines = ["Mahir: Hi my name is mahir. What is your sweet name? \n",
         "Aseem: My name is Aseem.\n" , "Mahir: how are you? \n",
         "Aseem: I am fine. what about you?\n","Mahir: fine thanks.\n",
         "Aseem: How ya doing ?\n", "Mahir: I am alright.\n"]
f.writelines(lines)
#f.write(lines)
f.close()
f = open("friends.txt","r")
line = f.readlines()
print(line)
f.close()

#import os
#os.remove("friends.txt")
