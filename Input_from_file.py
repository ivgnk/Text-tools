with open('Rus_5letters_words.txt','r') as f:
    s = f.read()
print(s)

with open('Rus_5letters_words_NEW.txt','w') as f:
    f.write(s)