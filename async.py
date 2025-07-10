import asyncio
words_with_delays = [
    ("Привет", 1.0),
    ("gggg", 0.5),
    ("bjhjjh", 2.0),
    ("iygu", 0.3),
    ("ghyti", 1.5),
    ("uifr", 0.7),
    ("ujoui", 1.2),
    ("gyuь", 0.9),
    ("hj", 1.8),
    ("huh", 0.4),
]

async def print_words():
    for word, delay in words_with_delays:
        print(word)
        await asyncio.sleep(delay)

asyncio.run(print_words())
