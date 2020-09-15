

s = 'abcd'
try:
    print(f"{s[5]}")
except IndexError:
    print("ups... trouble!")

try: 
    print(f"{s[3:100]}")
except IndexError:
    print("wut!?")
finally:
    print("made it!")

# print the first and the last letter word='abcd -> ['a', 'd']

#bad example!

def bad_first_and_last(word):
    return word[0] + word[-1]

print(bad_first_and_last('abcd'))

print(bad_first_and_last([1,2,3,4]))

def first_and_last(word):
    return word[:1] + word[-1:]

print(first_and_last("abcd"))

# Exercises

