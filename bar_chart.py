#How to create a bar chart with #Matplotlib and #Python

import matplotlib.pyplot as plt


def bar_chart(numbers, labels, pos):
    fig = plt.figure(figsize=(5, 8))
    plt.bar(pos, numbers, color='red')
    plt.xticks(ticks=pos, labels=labels)
    plt.show()


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    pos = range(len(numbers))
    bar_chart(numbers, lables, pos)

