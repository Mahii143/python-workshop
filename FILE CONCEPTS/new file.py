#with open("test1.txt","w+") as file1:
#    file1.write("Hi")
'''with open("test1.txt","a+") as file1:
    file1.write("Hello")
    file1.write("How are you?")
    file1.close()
'''

#with open("test3.txt","w") as file1:
 #   file1.write("Hi")
    #file1.write("\nHello")
    #file1.write("\nHow are u?")
    #line = file1.readline()
    #words = line.split()
    #print(words)
    #for i in file1:
      #  print(file1.readline())
    #
#file1.close()

with open("test3.txt","r") as file1:
    line = file1.readline()
    words = line.split()
    print(words)
file1.close()
