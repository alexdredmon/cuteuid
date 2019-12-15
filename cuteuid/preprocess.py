from collections import defaultdict
import json
from urllib.request import urlopen

from core.converters import to_leet, to_hex_leet

WORDLIST_URL = "https://raw.githubusercontent.com/bevacqua/correcthorse/master/wordlist.json"
OUTPUT_FILE = "./data/words.json"

all_words = defaultdict(list)
hex_leet_words = defaultdict(list)
leet_words = defaultdict(list)

with urlopen(WORDLIST_URL) as url:
    data = json.loads(url.read().decode())
    for datum in data:
        # Group words by number of characters
        all_words[len(datum)].append(datum.lower())

    for word_length, grouping in all_words.items():
        for word in grouping:
            leet = to_leet(word)
            leet_words[word_length].append(leet)
            if "ea" in word:    # 1337 sp34k ea->ee dupes
                leet = to_leet(word.replace("ea", "ee"))
                leet_words[len(leet)].append(leet)
            hex_leet = to_hex_leet(word)
            if " " not in hex_leet:
                hex_leet_words[len(leet)].append(hex_leet)
    words = {
        "all": all_words,
        "hex_leet": hex_leet_words,
        "leet": leet_words,
    }
    with open(OUTPUT_FILE, 'w+') as file:
        file.write(json.dumps(words))
