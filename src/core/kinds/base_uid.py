import json
import random


def rand(max):
    return random.randrange(max) + 1


class BaseUid:
    data_file = "./data/words.json"
    delimeter = "-"

    def __init__(self):
        with open(self.data_file, encoding='utf-8') as json_file:
            self.data = json.load(json_file)

    @property
    def words(self):
        return self.data["all"]

    @property
    def word_length(self, maximum=12):
        return rand(maximum)

    def generate_section(self, length):
        section = ""
        while len(section) < length:
            remaining_length = length - len(section)
            word = self.generate_word(length=rand(remaining_length))
            section = f"{section}{word}"
        return section

    def generate_word(self, length):
        if str(length) not in self.words:
            return ""
        return random.choice(self.words[str(length)])

    def generate(self):
        sections = [
            self.generate_section(length=8),
            self.generate_section(length=4),
            self.generate_section(length=4),
            self.generate_section(length=12),
        ]
        return self.delimeter.join(sections)
