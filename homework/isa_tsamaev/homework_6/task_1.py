text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
    " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

split_words = text.split()
new_text = []

for word in split_words:
    if word.endswith((",", ".")):
        punctuation = word[-1]
        word = word[:-1] + "ing" + punctuation
    else:
        word += "ing"

    new_text.append(word)

print(' '.join(new_text))
