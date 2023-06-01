import re

# 读取词典文件
def read_dict(filename):
    word_dict = {}
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            # 将词典中的词作为键，值为空字符串
            word_dict[word] = ''
    return word_dict

# 将符合词替换为HTML标记
def replace_words(text, word_dict):
    regex = re.compile("|".join(map(re.escape, word_dict)))
    def replace(match):
        word = match.group(0)
        new_word = f'<font color=blue>{word}</font>'
        return new_word
    return regex.sub(replace, text)

if __name__ == '__main__':
    # 读取词典文件
    word_dict = read_dict('N_dictionary.txt')
    # 读取文本文件
    with open('output.txt', 'r', encoding='utf-8') as f:
        # 逐行读取文件内容，并将每个评论视为一个单独的字符串进行处理
        comments = f.readlines()
        new_comments = []
        for comment in comments:
            # 去除评论中的换行符
            comment = comment.strip()
            # 将符合词替换为HTML标记
            new_comment = replace_words(comment, word_dict)
            new_comments.append(new_comment)
        # 将处理后的评论以换行符连接成一个字符串
        new_text = '\n'.join(new_comments)
    # 输出处理后的文本
    print(new_text)
    with open('output1.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)