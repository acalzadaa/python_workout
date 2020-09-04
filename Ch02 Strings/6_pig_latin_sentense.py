def sentence(phrase):
    output = []
    for word in phrase.split():
        if word[0] in 'aeiou':
            output.append(f'{word[1:]}{word[0]}way'.title())
        else:
            output.append(f'{word[1:]}{word[0]}ay'.title())
    return ' '.join(output)

print(sentence('The comming of the sentense in a phrase all around'))