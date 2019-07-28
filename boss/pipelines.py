# coding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from os import path
# from wordcloud import WordCloud
# import jieba

class BossPipeline(object):
    def process_item(self, item, spider):
        text = ''.join(item['job_desc'])
        d = path.dirname(__file__)
        # stopwords = [line.strip() for line in open(path.join(d, 'ban.txt'), 'r').readlines()]
        # wordlist = jieba.cut(text)
        # outstr = ''
        # for word in wordlist:
        #     if word not in stopwords:
        #         if word != '\t':
        #             outstr += word
        #             outstr += " "
        with open(path.join(d, 'zhipin.txt'), 'a', encoding='utf-8') as f:
            f.write(text)
        # with open(path.join(d, 'zhipin.txt'), encoding='utf-8') as f:
        #     text = f.read()
        # wordcloud = WordCloud(background_color="black", max_words=200, font_path='HYQiHeiY4-95W.otf').generate(text)
        # wordcloud.to_file(path.join(d, "cloud_word.png"))
        return item
