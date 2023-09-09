def generate_output_text(word, amount):
    output_text = []
    for i in range(amount):
        modified_word = f"{word}_{i}"
        output_text.append(modified_word)
    return "\n".join(output_text)

while True:
    word = input("Enter a word (or press Enter to quit): ")
    if not word:
        break

    try:
        amount = int(input("Enter the amount of strings to generate: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    output_text = generate_output_text(word, amount)

    with open('Nicks.txt', 'w') as output_file:
        output_file.write(output_text)

    print("Output saved to Nicks ")
