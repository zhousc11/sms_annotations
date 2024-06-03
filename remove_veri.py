def remove_blocked_lines(file_path, blocked_word):
    # Read the file and filter out lines containing the blocked word
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Filter lines that do not contain the blocked word
    filtered_lines = [line for line in lines if blocked_word not in line]

    # Write the filtered lines back to the same file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

# Example usage
remove_blocked_lines("/home/zhousc66/spamdata/processed/tobeprocessed/no_veri_data.txt", "測試")
