def pigsay(word):
    if word[0].lower() in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

print(pigsay("samuel"))