def words_count(s):
    return len(s.split())

def chars_count(s):
    counters = {}
    for ch in list(s):
        if not ch.isalpha():
            continue
        if ch not in counters:
            counters[ch] = 0
        counters[ch] += 1
    return counters

with open("books/frankenstein.txt") as f:
    print("--- Begin report of books/frankenstein.txt ---")
    s = f.read().lower()
    print(f"{words_count(s)} words found in the document")
    print()
    counters = sorted(chars_count(s).items(), key = lambda x: x[1], reverse = True)
    print(counters)
    for (ch, count) in counters:
        print(f"The '{ch}' character was found {count} times")
    print("--- End report ---")
