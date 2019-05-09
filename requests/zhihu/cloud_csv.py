import re

import csv
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np


def wordCount():
    import jieba.analyse

    word_list = []

    with open('user.csv', encoding='utf_8_sig', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            try:
                tags = jieba.analyse.extract_tags(row[0])
                for t in tags:
                    word_list.append(t)
            except Exception as e:
                print(row)
                print(e)

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


def wordCloud(wordList):
    my_word = WordCloud(
        font_path="C:/Windows/Fonts/simfang.ttf",
        background_color='white',
        width=1000,
        height=800
    ).generate_from_frequencies(wordList)

    plt.imshow(my_word, interpolation='bilinear')

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    wordList = wordCount()
    wordCloud(wordList)
