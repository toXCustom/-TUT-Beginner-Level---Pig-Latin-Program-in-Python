def pig_latin_word_converter(word):
    vowels = "aeiou"

    if word[0] in vowels:
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"
    
while True:
    word = input("Enter a word to transalte to pig latin: ")
    print(f"Pig Latin translation: {pig_latin_word_converter(word)}")