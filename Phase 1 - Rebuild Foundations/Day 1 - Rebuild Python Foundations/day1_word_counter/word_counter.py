# word_counter.py

def count_words_chars(file_path):
    try:
        with open(file_path,"r", encoding="utf-8") as file:
            text = file.read()
            
            num_lines = 1 + len(file.readline())

            words = text.split()
            num_words = len(words)
            num_chars = len(text)

            print(f"📄 File: {file_path}")
            print(f"🧮 Total Words: {num_words}")
            print(f"🔠 Total Characters: {num_chars}")
            print(f"🧮 Total Lines: {num_lines}")

            with open("report.txt", "w") as report:
                report.write(f'File: {file_path}\n')
                report.write(f'Words: {num_words}\n')
                report.write(f'Characters: {num_chars}\n')
                report.write(f'Lines: {num_lines}\n')

            print("Saving reporting in report.txt")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    path = input("Enter the file path:")
    count_words_chars(path)