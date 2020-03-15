import itertools
from math import factorial
from collections import Counter

def next_train(train_speeds):
    train_speeds = train_speeds[::-1]
    output = []
    running_number = train_speeds[0]
    for i in range(len(train_speeds[1:])):
        if train_speeds[i + 1] > running_number:
            output.append(running_number)
        running_number = train_speeds[i + 1]
    output.append(running_number)
    return output[::-1]

def promys_ten(*speeds):
    speeds = next_train(speeds)
    while (new := next_train(speeds)) != speeds:
        speeds = new
    return len(speeds)

def avg_ten(number):
    temp = [promys_ten(*q) for q in itertools.permutations(range(1, number + 1))]
    return (Counter(temp), sum(temp), factorial(number))
