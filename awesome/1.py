# 按照版本统计文本中积极、消极、中立情绪的占比

import csv
from collections import defaultdict

def count_number_values(csv_file):
    group_counts = defaultdict(lambda: {'positive': 0, 'negative': 0, 'zero': 0, 'total': 0})

    with open(csv_file, 'r', encoding='gb18030', errors='ignore') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                value = float(row[-1])  # Assuming last column contains numerical values
                group = row[-6]  # Assuming second last column is used for grouping

                group_counts[group]['total'] += 1

                if value > 0:
                    group_counts[group]['positive'] += 1
                elif value < 0:
                    group_counts[group]['negative'] += 1
                else:
                    group_counts[group]['zero'] += 1
            except ValueError:
                pass  # Ignore non-numeric values in the last column

    for group, counts in group_counts.items():
        total_count = counts['total']
        positive_count = counts['positive']
        negative_count = counts['negative']
        zero_count = counts['zero']

        positive_percentage = (positive_count / total_count) * 100 if total_count > 0 else 0
        negative_percentage = (negative_count / total_count) * 100 if total_count > 0 else 0
        zero_percentage = (zero_count / total_count) * 100 if total_count > 0 else 0

        print(f"Group: {group}")
        print(f"Positive count: {positive_count} ({positive_percentage}%)")
        print(f"Negative count: {negative_count} ({negative_percentage}%)")
        print(f"Zero count: {zero_count} ({zero_percentage}%)")
        print()

# 用法示例
count_number_values('1475305_with_versions.csv')
