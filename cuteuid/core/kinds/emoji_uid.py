import random

from .base_uid import BaseUid


class EmojiUid(BaseUid):
    data_file = "data/emojis.json"
    delimeter = "➖"

    def __init__(self, flags_only=False, smileys_only=False):
        super().__init__()
        self.flags_only = flags_only
        self.smileys_only = smileys_only

    @property
    def words(self):
        if self.flags_only:
            return self.data["flags"]
        elif self.smileys_only:
            return self.data["smileys"]
        return self.data["all"]

    def generate_section(self, length):
        section = []
        for i in range(0, length):
            section.append(self.random_emoji())
        return "".join(section)

    def random_emoji(self):
        return random.choice(self.words)
