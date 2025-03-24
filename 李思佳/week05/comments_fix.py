
#修复后内容存盘
fixed = open("李思佳/week05/doubanbook_fixed.txt", "w", encoding="utf-8")

#修复前
lines = [line for line in open("李思佳/week05/doubanbook_top250_comments.txt", "r", encoding="utf-8")]

for i, line in enumerate(lines):
    #保存标题列
    if i == 0:
        fixed.write(line)
        prev_line = '' #上一行书名置为空
        continue
    # 提取书名和评论对应的文本
    terms = line.split("\t")

    # 当前行的书名 == 上一行的书名
    if terms[0] == prev_line.split('\t')[0]:
        if len(prev_line.split('\t')) == 6: #上一行是评论
            # 保存上一行的记录
            fixed.write(prev_line + '\n')
            prev_line = line.strip() #上一行变为当前行
        else:
            prev_line = ""
    else:
        # 处理换书的场景和同一本书的场景
        if len(terms) == 6: #新书
            prev_line = line.strip()
        else:
            prev_line += line.strip()

fixed.close()
