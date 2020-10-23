word = input()
consonant = []
vowel = []
vowels = "aeiouy"
for i in range(len(word)):
    c = word[i:len(word)]
    lenght = len(word)
    if word[i] in vowels or word[i] in vowels.upper():
        for _ in range(len(c)):
            vowel.append(word[i:lenght])
            lenght -= 1
    else:
        for _ in range(len(c)):
            consonant.append(word[i:lenght])
            lenght -= 1
vowel_dict = {}
consonant_dict = {}
for el in vowel:
    vowel_dict[el] = vowel.count(el)
for elem in consonant:
    consonant_dict[elem] = consonant.count(elem)
print(vowel_dict, consonant_dict, sep="\n")


