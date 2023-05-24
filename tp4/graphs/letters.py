import itertools
import string
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_letter_plot(letter, ax, cmap='Blues'):
    p = sns.heatmap(letter, ax=ax, annot=False, cbar=False, cmap=cmap,square=True, linewidth=2, linecolor='black')
    p.xaxis.set_visible(False)
    p.yaxis.set_visible(False)
    return p
def print_letters_line(letters, cmap='Blues', cmaps=[]):
    fig, ax = plt.subplots(1, len(letters))
    fig.set_dpi(360)
    if not cmaps:
        cmaps = [cmap]*len(letters)
    if len(cmaps) != len(letters):
        raise Exception('cmap list should be the same length as letters')
    for i, subplot in enumerate(ax):
        create_letter_plot(letters[i].reshape(5,5), ax=subplot, cmap=cmaps[i])
    plt.show()

def parse_and_test_letters():
    with open("../datasets/letters.txt") as fp:
        letters = {}
        current = np.ones((5,5))*-1
        idx = 0
        for line in fp:
            if line[0] == '=':
                letters[string.ascii_uppercase[len(letters)]] = current
                current = np.ones((5,5))*-1
                idx = 0
            else:
                for i, c in enumerate(line.strip('\n')):
                    current[idx][i] = 1 if c == '*' else -1
                idx += 1
    n = 6
    letters_list = list(letters.values())
    #fill with empty letters
    letters_list += [np.ones((5,5))*-1]*(n - len(letters_list) % n)

    #iterate as groups of n
    for letter_group in [letters_list[ i * n:( i + 1) *n] for i in range(len(letters_list) // n)]:
        print_letters_line(letter_group)
