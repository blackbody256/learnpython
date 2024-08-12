book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
#this is one way of counting words in a string
for word in book_title:
    if word not in word_counter:
        word_counter[word]=1
    else:
        word_counter[word] +=1

print(word_counter)
print("\n\n\n")

#Second method 
word_counter2 = {}

for word in book_title:
    word_counter2[word] = word_counter2.get(word,0)+1

#if the word is got for the 1st time, the get method will return 0 and then 1 is add to it 
#so that the value of that key is now 1
#if the same word is got for a 2nd or 3rd time or more, the get method will return it's current value and then add 1 to the value

print(word_counter2)
