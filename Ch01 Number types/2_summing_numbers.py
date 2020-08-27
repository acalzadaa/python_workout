def summing(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(summing(1,2,3,4,5,6))