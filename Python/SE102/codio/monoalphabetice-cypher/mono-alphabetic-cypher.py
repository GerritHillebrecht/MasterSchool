import re
from collections import Counter
import itertools
import nltk
from nltk.corpus import words

# Download des englischen Wörterbuchs (nur beim ersten Mal nötig)
nltk.download('words')

# Englisches Wörterbuch
english_words = set(words.words())

# Häufigste Buchstaben und Bigramme im Englischen
common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
common_bigrams = ['th', 'he', 'in', 'er', 'an', 're', 'on', 'at', 'en', 'nd']

def get_bigrams(text):
    return [''.join(b) for b in zip(text[:-1], text[1:])]

def score_plaintext(plaintext):
    words = re.findall(r'\b\w+\b', plaintext.lower())
    return sum(1 for word in words if word in english_words)

def decrypt_monoalphabetic(ciphertext):
    ciphertext = ciphertext.lower()
    freq = Counter(ciphertext)
    bigram_freq = Counter(get_bigrams(ciphertext))
    
    # Erstelle initiale Zuordnung basierend auf Einzelbuchstaben-Häufigkeit
    mapping = {}
    for c, l in zip(sorted(freq, key=freq.get, reverse=True), common_letters):
        mapping[c] = l
    
    # Verfeinere Zuordnung basierend auf Bigrammen
    for _ in range(10):  # Mehrere Iterationen zur Verfeinerung
        bigram_mapping = {}
        for (c1, c2), l in zip(sorted(bigram_freq, key=bigram_freq.get, reverse=True), common_bigrams):
            if c1 in mapping and c2 in mapping:
                bigram_mapping[mapping[c1] + mapping[c2]] = l
        
        # Aktualisiere Mapping basierend auf Bigrammen
        for c1, c2 in itertools.permutations(mapping, 2):
            if mapping[c1] + mapping[c2] in bigram_mapping:
                l1, l2 = bigram_mapping[mapping[c1] + mapping[c2]]
                mapping[c1], mapping[c2] = l1, l2
    
    # Entschlüssele Text
    plaintext = ''.join(mapping.get(c, c) for c in ciphertext)
    
    # Optimiere durch Vertauschen von Paaren
    best_score = score_plaintext(plaintext)
    best_plaintext = plaintext
    for c1, c2 in itertools.combinations(mapping, 2):
        new_mapping = mapping.copy()
        new_mapping[c1], new_mapping[c2] = new_mapping[c2], new_mapping[c1]
        new_plaintext = ''.join(new_mapping.get(c, c) for c in ciphertext)
        score = score_plaintext(new_plaintext)
        if score > best_score:
            best_score = score
            best_plaintext = new_plaintext
            mapping = new_mapping
    
    return best_plaintext

# Beispiel
ciphertext = "MXCCG PXCR ZSR XZD YXDOPCEXDDXCR"
print(decrypt_monoalphabetic(ciphertext))