# 去除一模一样的行
def remove_duplicates(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if line not in seen_lines:
                file.write(line)
                seen_lines.add(line)


if __name__ == "__main__":
    input_path = '/home/zhousc66/spamdata/processed/finished/latest.txt'  # 这里填写你的输入文件路径
    output_path = '/home/zhousc66/spamdata/processed/finished/latest_rm_duplicate.txt'  # 这里填写你的输出文件路径
    remove_duplicates(input_path, output_path)
