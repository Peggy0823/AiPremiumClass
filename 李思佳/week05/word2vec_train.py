import fasttext
import jieba

# #文档分词预处理
# with open('李思佳/week05/HLM.txt', 'r' ) as f:
#     lines = f.read()

# with open('李思佳/week05/HLM_c.txt', 'w') as f:
#     f.write(' '.join(jieba.cut(lines)))

# 将词汇变成向量进行相关性分析


#传入的文本必须是要有空格分词的文档文件，fasttext就能进行模型训练
model = fasttext.train_unsupervised('李思佳/week05/HLM_c.txt', model='skipgram') #无监督的
# print('文档词汇表：', model.words)
#获取词向量的最近邻
print(model.get_word_vector('宝玉'))

# 获取近邻词
print(model.get_nearest_neighbors('宝玉', k=5))

# 分析词间对比
print(model.get_analogies('宝玉','黛玉', '宝钗'))

# 保存模型
model.save_model('hlm_skipgram.bin')

# 加载模型
model1 = fasttext.load_model('hlm_skipgram.bin')

