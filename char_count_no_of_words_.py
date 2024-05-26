def generate_words(char_counts):
    chars = list(char_counts.keys())
    counts = list(char_counts.values())

    words = []
    for i in range(3, sum(counts) + 1):
        for word in generate_words_helper(chars, counts, i, []):
            words.append("".join(word))

    return words

def generate_words_helper(chars, counts, length, word):
    if length == 0:
        return [word]

    words = []
    for i in range(len(chars)):
        if counts[i] > 0:
            word.append(chars[i])
            counts[i] -= 1
            words.extend(generate_words_helper(chars, counts, length - 1, word))
            counts[i] += 1
            word.pop()

    return words

# Example usage
char_counts = {"a": 2, "h": 4, "f": 1, "t": 3, "k": 6, "l": 1}
words = generate_words(char_counts)
print(len(words))
print(words)