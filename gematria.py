words = []

# чтение входных данных
while True:
    word = input()
    if word == "":
        break
    words.append(word.upper())

# вычисление гематрии для каждого слова
for i in range(len(words)):
    gematria = 0
    for letter in words[i]:
        gematria += ord(letter) - ord('A') + 1
    words[i] = (words[i], gematria)

# сортировка списка по гематрии и алфавиту
words.sort(key=lambda x: (x[1], x[0]))

# вывод результатов
for word, _ in words:
    print(word)
