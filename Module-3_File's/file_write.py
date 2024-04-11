fl=open('test.txt','r')


fl.write("Good Afternoon!")
fl.write("\nHello Students!")

if fl.writable(): #TRUE
    print("Yes...This is file is writable...")
else:
    print("Sorry! This file is not writable.")


