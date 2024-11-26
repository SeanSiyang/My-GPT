from collections import defaultdict, Counter

"""
defaultdict 是 Python 标准库中的一个字典子类，它与普通的 dict 相似，但在访问一个不存在的键时，它不会抛出 KeyError 异常，而是会自动为该键创建一个默认值。
Counter 是 Python 中的一个子类，用于计数可哈希对象（通常是元素的频率统计）。它类似于一个字典，键是元素，值是元素出现的次数。Counter 提供了许多便捷的方法来进行元素计数和操作。
Counter 会自动计算元素出现的频次，并将其作为值。
如果你访问一个不存在的键，Counter 返回的是 0，而不会抛出 KeyError。
"""

# 语料库
corpus = ["我喜欢吃苹果",
          "我喜欢吃香蕉",
          "她喜欢吃葡萄",
          "他不喜欢吃香蕉",
          "他喜欢吃苹果",
          "她喜欢吃草莓"]

# 分词函数：将文本转换为单个字符的列表
def tokenize(text):
    return [char for char in text]  


# 计算每个BiGram的词频
def count_ngrams(corpus, n):
    # ngrams_count 是一个字典，它的每个键（例如一个词）对应的值是一个 Counter，用来统计与该词相关联的其他词的频率。
    ngrams_count = defaultdict(Counter) # 每个键对应的值是一个 Counter 对象。
    for text in corpus: # 遍历每个文本
        tokens = tokenize(text) # 分词
        for i in range(len(tokens) - n + 1): # 6个词按2来分，就是5个2元组
            #print("======================================")
            ngram = tuple(tokens[i:i+n]) # 创建一个2元组
            #print("ngram: ", ngram) 
            prefix = ngram[:-1] # 获取2元组的前缀
            #print("prefix: ", prefix)
            token = ngram[-1] # 获取2元组的目标单字
            #print("token: ", token)
            ngrams_count[prefix][token] += 1 # 更新这个元组的计数
            #print("======================================")
            
    return ngrams_count

def main():
    bigram_counts = count_ngrams(corpus, 2)
    print("Bigram 词频：")
    for prefix, counts in bigram_counts.items():
        print("{}: {}".format("".join(prefix), dict(counts)))

if __name__ == '__main__':
    main()



