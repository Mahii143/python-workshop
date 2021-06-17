'''
Give the significance of with keyword. Write a function display_oddLines()
to display odd number lines from the text file. Consider above file as friends.txt.{}
'''

f = open("friends.txt","r")
lines = []
for i in f:
    lines.append(i)

    
def display_oddLines(L):
    for i in range(0,len(L),2):
        print(L[i])
display_oddLines(lines)



 


