# HELP - Commands

## Chapter 01 - Number Types

| Name            | Description                                | Symbol                        | Example                             |
| --------------- | ------------------------------------------ | ----------------------------- | ----------------------------------- |
|                 |                                            | except Exception as variable: | except ValueError as val:           |
| Format          | Format numbers                             | print(f"{variable.2f}")       | print(f"{average.2f}")              |
| Random          | Calculate random numbers from start to end | random.randint(start, end)    | random.randint(1,100)               |
| Splat Operator  | Receive multiple elements                  | def method(\*arg)             | def summing(\*numbers):             |
| Walrus Operator | Evaluation and Assignment                  | :=                            | while x := input("enter a number"): |
| try/catch       | find out exceptions                        | try: variable = operation     | try: time = int(ans)                |

## Chapter 02 - String Types

| Name                 | Description                                            | Example                                                  |
| -------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Iterating over files | Opens a file and iterates over its lines one at a time | for one_line in open(filename):                          |
| Slice                | Retrieves a subset of elements from a sequence         | # returns 'bdf' 'abcdefg'[1:7:2]                         |
| in                   | Operator for Searching in a sequence                   | 'a' in 'abcd'                                            |
| list.append          | Adds an element to a list                              | mylist.append('hello')                                   |
| sorted               | Returns a sorted list, based on an input sequence      | # returns [10, 20, 30] sorted([10, 30, 20])              |
| str.join             | Combines strings to create a new one                   | # returns 'abc*def*ghi' '\*'.join(['abc', 'def', 'ghi']) |
| str.split            | Breaks strings apart, returning a list                 | # returns ['abc', 'def', 'ghi'] 'abc def ghi'.split()    |
