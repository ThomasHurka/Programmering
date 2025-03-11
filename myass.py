letters  = ["a","b","c", "d", "e", "f"]

word = input("Input Here Ambre; ")


for x in word: 
    for y in letters: 
        if y == x: 
            letters.remove(y)
     
    
print(letters)




