# word counter version:2
# added top 10 frequent words
from collections import Counter

def main_func(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

            words = text.split()
            num_words = len(words)
            num_chars = len(text)

            freq_words = Counter(text.lower().split())

            print(f"📄 File: {file_path}")
            print(f"🧮 Total Words: {num_words}")
            print(f"🔠 Total Characters: {num_chars}")
            print(f"Top 10 frequent words: {freq_words.most_common(10)}")

            with open("report.txt", "w") as report:
                report.write(f"File: {file_path}\n")
                report.write(f"Total Words: {num_words}\n")
                report.write(f"Total Characters: {num_chars}\n")
                report.write(f"Top 10 frequent words: {freq_words.most_common(10)}\n")
    
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    path = input("Enter the path:")
    main_func(path)