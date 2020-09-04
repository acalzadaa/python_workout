def pigsay(word):
    if word[0].lower() in 'aeiou':
        return f'{word}way'.title()
    return f'{word[1:]}{word[0]}ay'.title()

print(pigsay("elements"))