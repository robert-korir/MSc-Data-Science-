"""
Create a file named text4w.txt.
Write the following lines in the file:
OLIVER
Know you where your are, sir?
ORLANDO
O, sir, very well; here in your orchard.
Close the file.
Reopen the file and add a line of text. Ask the user for this text from standard input.
Write the entire contents of the file to standard output.
Count the number of letters 'w' in the file. Print the result.

"""
f = open('text4w.txt', 'a')
f.write('OLIVER\n')
f.write('Do you know you are, sir?\n')
f.write('OLANDO\n')
f.write('O, sir, very well; here in your orchard.\n')
f.close()
f= open('text4w.txt', 'a')
text = input("Kindly enter details here : ")
f.write(f'{text} \n')
f = open('text4w.txt','r') 
print(f.read())

