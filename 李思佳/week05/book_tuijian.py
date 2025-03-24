import csv
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer  #feature_extraction 特征提取
from sklearn.metrics.pairwise import cosine_similarity

def load_data(filename):
    # 图书的评论信息集合
    book_comments = {} #{书名：”评论1词 + 评论2词 + ...“}

    with open(filename,'r' ) as f:
        reader = csv.DictReader(f, delimiter='\t' ) #识别格式文本中的标题列
        for item in reader:
            book = item['book']
            comment = item['body']
            comment_words = jieba.lcut(comment)

            if book == '': continue #书名为空的保护

            # 图书评论集合收集
            book_comments[book] = book_comments.get(book, []) #dict的get方法，key不存在，可赋值
            book_comments[book].extend(comment_words)
    return book_comments

if __name__ == '__main__':

    #加载停用词列表
    stop_words = [line.strip() for line in open("李思佳/week05/stopwords.txt", 'r', encoding="utf-8")]

    # 加载评论信息
    book_comments = load_data("李思佳/week05/doubanbook_fixed.txt")
    print(len(book_comments))

    #构建TF-IDF特征矩阵
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform([' '.join(comments) for comments in book_comments.values()])  #返回基于tfidf的得分矩阵
    # print(tfidf_matrix.shape)
    # print(vectorizer.get_feature_names_out) # 获取关键词信息，会过滤重复项

    #分析矩阵的每一行的非0数值和所有行做余弦相似度的计算
    similarity_matrix = cosine_similarity(tfidf_matrix)
    print(similarity_matrix.shape)


