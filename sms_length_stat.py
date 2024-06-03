import matplotlib.pyplot as plt


def plot_character_histogram(file_path):
    # Read the file and count characters per line
    with open(file_path, 'r', encoding='utf-8') as file:
        line_lengths = [len(line.strip()) for line in file.readlines()]

    # Create a histogram of the line lengths
    plt.figure(figsize=(10, 6))
    plt.hist(line_lengths, bins=range(min(line_lengths), max(line_lengths) + 1), alpha=0.75, color='blue')
    plt.title('Histogram of Character Counts per Line')
    plt.xlabel('Number of Characters')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


# Example usage
plot_character_histogram("/home/zhousc66/spamdata/processed/tobeprocessed/no_veri_data")
