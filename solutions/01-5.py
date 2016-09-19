text = 'It was the Best of Times It was the Worst of Times'
words = text.split()
count = 0
capwords = []
for word in words:
    if word.istitle():
        count += 1 # same as count = count + 1
        if word not in capwords:
            capwords.append(word)

print('Number of Capitalalized Words =', count)
print('Capitalized Word List = ', capwords)