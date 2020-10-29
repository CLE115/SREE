import doc2vec


# def test_doc2vec():
# 加载模型
model = doc2vec.Doc2Vec.load('title.model')
# 与标签‘0’最相似的
print(model.docvecs.most_similar('0'))
# 进行相关性比较
# print(model.docvecs.similarity('0','1'))
# 输出标签为‘10’句子的向量
# print(model.docvecs['10'])
# 也可以推断一个句向量(未出现在语料中)
# words = u"vscode"
# print(model.infer_vector(words.split()))
# 也可以输出词向量
# print(model[u'debugging'])