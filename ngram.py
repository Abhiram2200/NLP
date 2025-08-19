# Vocabulary from the matrix
vocab = ['i', 'want', 'to', 'eat', 'chinese', 'food', 'lunch', 'spend']

# Bigram frequency matrix as a nested dictionary
bigram_counts = {
    'i':        {'i': 5, 'want': 827, 'to': 0, 'eat': 9, 'chinese': 0, 'food': 0, 'lunch': 0, 'spend': 2},
    'want':     {'i': 2, 'want': 0, 'to': 608, 'eat': 1, 'chinese': 6, 'food': 6, 'lunch': 5, 'spend': 1},
    'to':       {'i': 2, 'want': 0, 'to': 4, 'eat': 686, 'chinese': 2, 'food': 0, 'lunch': 6, 'spend': 211},
    'eat':      {'i': 0, 'want': 0, 'to': 2, 'eat': 0, 'chinese': 16, 'food': 2, 'lunch': 42, 'spend': 0},
    'chinese':  {'i': 1, 'want': 0, 'to': 0, 'eat': 0, 'chinese': 0, 'food': 82, 'lunch': 1, 'spend': 0},
    'food':     {'i': 15, 'want': 0, 'to': 15, 'eat': 0, 'chinese': 1, 'food': 4, 'lunch': 0, 'spend': 0},
    'lunch':    {'i': 2, 'want': 0, 'to': 0, 'eat': 0, 'chinese': 0, 'food': 1, 'lunch': 0, 'spend': 0},
    'spend':    {'i': 1, 'want': 0, 'to': 1, 'eat': 0, 'chinese': 0, 'food': 0, 'lunch': 0, 'spend': 0},
}

# Step 1: Compute unigram counts (row sums)
unigram_counts = {}
for row_word in vocab:
    unigram_counts[row_word] = sum(bigram_counts[row_word].values())

# Step 2: Compute bigram probabilities
bigram_probs = {}

for w1 in vocab:
    bigram_probs[w1] = {}
    row_total = unigram_counts[w1]
    for w2 in vocab:
        count = bigram_counts[w1][w2]
        if row_total > 0:
            prob = count / row_total
        else:
            prob = 0
        bigram_probs[w1][w2] = round(prob, 4)  # rounded for better display

# Step 3: Display
print("Unigram Counts:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

print("\nBigram Probabilities:")
print(f"{'From\\To':<10}" + "".join([f"{w:<10}" for w in vocab]))
for w1 in vocab:
    row = f"{w1:<10}"
    for w2 in vocab:
        row += f"{bigram_probs[w1][w2]:<10}"
    print(row)
