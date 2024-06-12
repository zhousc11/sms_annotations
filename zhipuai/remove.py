import pandas as pd

# 读取Excel文件
file_path = "D:\\Users\\Downloads\\1.xlsx"  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设数据在第一列和第二列
first_column = df.iloc[:, 3]
second_column = df.iloc[:, 6]

# 找出第二列有但是第一列没有的数据
second_not_in_first = second_column[~second_column.isin(first_column)]

# 输出结果
print("第二列有但第一列没有的数据：")
print(second_not_in_first)
