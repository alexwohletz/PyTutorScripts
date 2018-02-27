#Get the vowel count in a sentence

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

character_count = 0
sentence = input("enter a sentence")
sent_list = list(sentence.lower())
for letter in sent_list:
    
    if letter in vowels.keys():
        vowels[letter]+=1
        
for key, value in vowels.items():
    print(key, value)