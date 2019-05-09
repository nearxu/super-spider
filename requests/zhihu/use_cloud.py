
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 绘制图像的模块
import jieba  # jieba分词

f = open('test.txt', 'r', encoding='utf-8').read()

cut_text = ' '.join(jieba.cut(f))

wordCloud = WordCloud(
    # set font
    font_path="C:/Windows/Fonts/simfang.ttf",
    background_color='white', width=1000, height=800
).generate(cut_text)

plt.imshow(wordCloud, interpolation='bilinear')

plt.axis('off')
plt.show()
