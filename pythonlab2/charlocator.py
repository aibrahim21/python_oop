sentence = input("please enter a sentence")
character = input("pleaase enter a character to search for ")


print(sentence, character)
indexes=[]
for index, cha in enumerate(sentence) :
    if cha == character: 
        indexes.append(index)

if indexes:
    print(indexes) 
else:
    print("this character doesn't exist inside this sentence")
         