import random

from core.kinds.base_uid import BaseUid


class LeetUid(BaseUid):
    data_file = "./data/words.json"

    def __init__(self, hex_only=False):
        super().__init__()
        self.hex_only = hex_only

    @property
    def words(self):
        if self.hex_only:
            return self.data["hex_leet"]
        else:
            return self.data["leet"]

    @property
    def word_length(self, maximum=12):
        return random.randrange(maximum - 3) + 3

    def generate_section(self, length):
        if (length == 4):
            return self.generate_word(4)
        return super().generate_section(length=length)
