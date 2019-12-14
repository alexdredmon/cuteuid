from core.kinds import emoji_uid, leet_uid


def generate_cuteuid(
    emoji=False,
    flags_only=False,
    hex_only=False,
    smileys_only=False,
):
    if emoji:
        uid = emoji_uid.EmojiUid(
            flags_only=flags_only,
            smileys_only=smileys_only
        )
    else:
        uid = leet_uid.LeetUid(hex_only=hex_only)

    return uid.generate()
