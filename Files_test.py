f= open("text5w.txt", "w+")
print("OLIVER ")
print("Know you where your are, sir? ")
print("ORLANDO ")
print("O, sir, very well; here in your orchard. ")
fileName = str(input())
fileHandle = open('text5w.txt', "r")

while True:
    text = str(input())
    if len(text)>0:
        fileHandle.write("\n")
        fileHandle.write(text)
    else:
        break
fileHandle.close()