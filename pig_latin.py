def pig_latin_word_converter(word):
    vowels = "aeiouAEIOU"
    punctuation = ",.!?;"
    end_punctuation = None

    if word[-1] in punctuation:
        end_punctuation = word[-1]
        word = word[:-1]

    if word[0] in vowels:
        pig_latin_word = word + "way"
    else:
#       return word[1:] + word[0] + "ay"
        for index, letter in enumerate(word):
            if letter in vowels:
                pig_latin_word = word[index:] + word[:index] + "ay"
                break
        else:
            pig_latin_word = word + "ay"

    if word[0].isupper():
        pig_latin_word = pig_latin_word.capitalize()

    if end_punctuation:
        pig_latin_word += end_punctuation

    return pig_latin_word
    
def pig_latin_sentence_converter(sentence):
    words = sentence.split()
    output = []

    for word in words:
        output.append(pig_latin_word_converter(word))
    
    return " ".join(output)
    
def main():
    while True:
        word = input("Enter a sentence to transalte to pig latin: ")
        print(f"Pig Latin translation: {pig_latin_sentence_converter(sentence)}")

main()