# 目录说明

此目录实现了文本标注功能，鉴于手动标注过程繁琐且效率低，使用python脚本进行标注。
首先根据相关论文[Gu ASE 2015](https://ieeexplore.ieee.org/document/7372064)来提取词典，然后遍历文本，查找到在词典中的单词就用html格式高亮。

目录结构如下
```
.
├── N_dictionary.txt # Negative dictionary
├── P_dictionary.txt # Positive dictionary
├── README.md 
├── head.html # head.md导出的html
├── head.md # 标注完的前200行，用于前端展示
├── hightlight.py # 标注脚本
└── output.html # 标注完的所有文本
```