# cuteuid
Generate cute UIDs, i.e. unique(ish) identifiers that are similar(ish) in appearance to increasingly ubiquitous [UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier).

## Usage
```python
from cuteuid import generate_cuteuid

generate_cuteuid()                  # 1337 UID
# 3xampl3a-boy1-goa1-5ucc33dd3p7h
# d1v151on-5ho3-1w31-d1571ngu15ha
# 7ak351h3-k33p-175a-5ympa7h371c1

generate_cuteuid(hex_only=True)     # 1337 UID (hex only)
# 10adca9a-4057-5a13-901171ca1136
# 0ff1c1a1-50f7-f33d-43517a73b3d1
# ad01053a-9057-7311-c411d400da50

generate_cuteuid(emoji=True)        # EmojiUID
# ⛹‍♂️🧜‍♂️⬜️3️⃣📏🧹🤴🗾➖🇵🇰📔💹🌳➖🇮🇴🐅🛂🇹🇱➖🇧🇱🗾🕣💿👱‍♀️💞❗️👷🇸🇪🤤🏄‍♂️🍲
# 🏅🧫🏋‍♂️🇹🇱👫🇦🇱🇹🇩🇪🇺➖😚🤽‍♂️👂💮➖👩‍🔬😨👭🇦🇩➖🦏🔷🇵🇦🎁😓🥗🥵🤾‍♀️🧗‍♀️😽🛵🗺
# 👅🏧🙅‍♂️🚇📘🚕👭⛹️‍♀️➖🤽‍♀️🕵️‍♂️🏌‍♀️🦘➖🏄‍♂️👨‍💻🈴🎗➖💕💂‍♂️🏳️🧐😥🇬🇳💀🤕🔻🙆🍟🇵🇼

generate_cuteuid(                   # EmojiUID (flags only)
    emoji=True,
    flags_only=True
)
# 🇱🇧🇼🇸🇮🇹🇲🇳🇬🇹🇦🇲🇬🇶🇬🇾➖🇸🇧🇲🇺🇧🇬🇸🇱➖🇮🇸🏁🇪🇺🇱🇻➖🇿🇲🏴󠁧󠁢󠁳󠁣󠁴󠁿🇸🇸🇵🇲🇬🇶🇧🇬🇳🇮🇲🇰🇿🇼🇸🇭🇬🇶🇮🇴
# 🇱🇮🇮🇸🇼🇫🇹🇩🇵🇫🚩🇧🇫🇬🇶➖🇨🇰🇲🇪🇫🇯🇿🇦➖🇬🇱🇹🇬🇶🇦🇳🇨➖🇿🇼🇲🇬🇸🇮🇬🇭🇺🇬🇧🇦🏴󠁧󠁢󠁥󠁮󠁧󠁿🇹🇹🇻🇺🇳🇴🇧🇶🇹🇻
# 🇲🇦🇬🇶🇧🇱🏴󠁧󠁢󠁳󠁣󠁴󠁿🇹🇻🇱🇷🇻🇳🇲🇾➖🇪🇬🇸🇦🇧🇫🇨🇺➖🇨🇻🇻🇨🇺🇿🇫🇷➖🇹🇩🇲🇷🇸🇰🏴‍☠️🇷🇸🎌🇰🇪🇹🇲🇨🇲🇨🇴🇬🇸🏁

generate_cuteuid(                   # EmojiUID (smileys only)
    emoji=True,
    smileys_only=True
)
# 😇😠😲😢😚😐😝😌➖🙁🤮😣🙁➖🥰😑🤡🤥➖🙁😞😐🤢🤢🤬😂😒🤢😚😰😍
# 😥🤫😨🤢😔😧😩😶➖😰😙🥴😄➖😑😨😲🥴➖😰😲🥳😭🙁😟😚😀😶🤠🤥😄
# 😬🤢🤓🤠🤢😥😪😑➖🥴🙄😠😢➖🙃😆😊🤥➖🤯😒😢🥶😨😌😧🙁😮😣🤭😔
```

## Preprocess
To rerun 1337 preprocesing, update `preprocess.py` to point `WORDLIST_URL` to a URL containing a valid JSON list of words and run:

```bash
python3 src/preprocess.py
```

### Disclaimer
This project is intended for entertainment purposes only - it is *not* recommended for use in your production or intended as a replacement to existing UUID generation mechanisms.  It *might* be a fun thing to include in your non-mission critical personal project(s), provided you're the right kind of weird.
