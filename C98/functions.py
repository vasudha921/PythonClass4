def greet(name):
    print('Hello '+ name + '. How are you?' )

#greet("Medha")

def countwordfromfile():
    filename = input("Enter filename")
    files = open(filename, "r")
    numberofwords = 0
    for line in files:
        words = line.split()
        numberofwords = numberofwords + len(words)
       
    print(numberofwords)
countwordfromfile()

