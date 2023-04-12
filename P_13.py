count = 0
letters = 0
while True:
    word = input("enter the word:")
    if word == "quit":
        break
    letters += len(word)
    count += 1    
average = letters / count
print("average letters",count, "is", average)