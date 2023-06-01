########### 将导出的body.txt重复行去除

fi = open('./issue_title.txt', 'r') # 打开需要处理的test.txt。
txt = fi.readlines()
with open('issue_title_OK.txt', 'a') as f:#创建处理去重复后的结果保存文档，防止找不到文件出错
    f.close()
for w in txt:
    fi2 = open('issue_title_OK.txt', 'r')
    txt2 = fi2.readlines()
    with open('issue_title_OK.txt', 'a') as f:  # 打开目标文件开始写入
        if w not in txt2:	#如果从源文档中读取的内容不在目标文档中则写入，否则跳过，实现去除重复功能！
            f.write(w)
        else:
            print("已去除重复-->"+w)
        f.close()
fi.close()


########### 将一个csv文件加入到另一个csv文件的右侧(增加列)

source_file_path = "20_out.txt11"  # 替换为实际的源文件路径
target_file_path = "extracted_results.csv"  # 替换为实际的目标文件路径

# 读取源文件和目标文件的内容
with open(source_file_path, 'r', encoding='utf-8') as source_file:
    source_lines = source_file.readlines()

with open(target_file_path, 'r', encoding='utf-8') as target_file:
    target_lines = target_file.readlines()

# 确保源文件和目标文件行数相同
if len(source_lines) != len(target_lines):
    print("源文件和目标文件行数不匹配。")
else:
    # 将每一行源文件的内容添加到目标文件对应行的末尾
    merged_lines = [target_lines[i].strip() + " " + source_lines[i] for i in range(len(target_lines))]

    # 将合并后的行写入目标文件
    with open(target_file_path+'new', 'w', encoding='utf-8') as target_file:
        target_file.writelines(merged_lines)

    print("内容已成功合并到目标文件。") '''
