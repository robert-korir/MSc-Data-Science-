#Korir Robert
def maraneno(kitabu, letters):
    file = open("text1aa.txt", "w")  
    file.write("ADAM\n")
    file.write("Yonder comes my master, your brother.\n")
    file.write("ORLANDO\n")
    file.write("Go apart, Adam, and thou shalt hear how he will shake me up.\n")
    file.close()
# writing newline character
    file = open("text1aa.txt", "a") 
    inp = input(f"Add your text here: ")
    file.write(''+inp)
    print('The content of the files are: \n')
    
    file = open("text1aa.txt", "r")
    print(file.read())

    # print('\nThe number count of letter a is:')

    file = open(kitabu, "r")
    text = file.read()
    count = 0
    for c in text:
        if c == letters:
            count += 1
    return count
    
print(maraneno('text1aa.txt', 'a'))