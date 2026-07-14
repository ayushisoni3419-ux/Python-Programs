word=input("enter a word:")
with open("file.txt","r") as file:
    data =file.read()
if word in data:
    print("word is present")
else:
    print("word is not present")
