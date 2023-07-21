def print_first_seven_words(character):
    with open('dictionary.txt', 'r') as file:
        count = 0
        for line in file:
            word = line.strip()
            if word.startswith(character):
                print(word)
                count += 1
                if count == 7:
                    break

character = input("Enter a character: ")
print(f"First 7 words starting with '{character}':")
print_first_seven_words(character)
