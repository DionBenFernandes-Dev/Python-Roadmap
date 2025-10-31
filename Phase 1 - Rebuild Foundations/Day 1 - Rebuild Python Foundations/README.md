# 🗓️ **Day 1 — Rebuild Python Foundations**

**Goal:** Warm up your Python brain — practice file handling, loops, and string manipulation by building a *Word & Character Counter* tool.

---

## ⏱️ **1-Hour Plan**

| Time      | Task                        | Description                                                                      |
| --------- | --------------------------- | -------------------------------------------------------------------------------- |
| 0-10 min  | **Setup & Refresher**       | Open your IDE (VS Code / Colab / Jupyter). Create a folder: `day1_word_counter`. |
| 10-25 min | **Learn / Recall Concepts** | Review `open()`, `with`, `read()`, `split()`, `len()`, and `try/except`.         |
| 25-50 min | **Code Along**              | Build the script step by step.                                                   |
| 50-60 min | **Mini-assignment**         | Add an enhancement, test on files, and push to GitHub.                           |

---

## 🧠 **Concept Review (10 min)**

You’ll need:

```python
# File reading
with open("filename.txt", "r") as file:
    content = file.read()

# Splitting text
words = content.split()          # List of words
characters = len(content)        # Count all characters

# Exception handling
try:
    ...
except FileNotFoundError:
    ...
```

---

## 💻 **Main Program (25 min)**

Let’s build the base version.

### 1️⃣ Create your working folder

```
day1_word_counter/
    ├── word_counter.py
    └── sample.txt
```

Add some text into `sample.txt` — any paragraph.

---

### 2️⃣ Code Step by Step

```python
# word_counter.py

def count_words_characters(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            
            words = text.split()
            num_words = len(words)
            num_chars = len(text)
            
            print(f"📄 File: {file_path}")
            print(f"🧮 Total Words: {num_words}")
            print(f"🔠 Total Characters: {num_chars}")
            
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    path = input("Enter file path: ")
    count_words_characters(path)
```

✅ **Run the program**:

```bash
python word_counter.py
```

Enter: `sample.txt`
You should see the word and character count printed.

---

## 🧩 **Mini-Assignment (10 min)**

Add at least **one** of these upgrades:

1. **Line Counter** — also count number of lines in the file.
2. **Save Results to a Report** — output to a text or CSV file.
3. **Multiple File Mode** — let user input several filenames separated by commas.

**Example (Saving Results):**

```python
with open("report.txt", "w") as report:
    report.write(f"File: {file_path}\n")
    report.write(f"Words: {num_words}\n")
    report.write(f"Characters: {num_chars}\n")
```

---

## 🧰 **Optional Exploration (if you have time)**

Try reading a **large text** (e.g., a book from Project Gutenberg) and compare counts.
Experiment with:

* `text.lower()` to make case-insensitive analysis.
* `collections.Counter` to count top 10 frequent words.

Example:

```python
from collections import Counter

word_freq = Counter(words)
print(word_freq.most_common(10))
```

---

## 🏁 **End-of-Day Deliverables**

* ✅ `word_counter.py`
* ✅ `sample.txt`
* ✅ `report.txt` (if you implemented save feature)

Push to GitHub:

```bash
git init
git add .
git commit -m "Day 1: Word & Character Counter"
git branch -M main
git remote add origin <your_repo_url>
git push -u origin main
```

---

## 🧠 **Reflection Questions**

1. Could you explain how `with open()` works to someone else?
Answer:
```
The mechanism behind with open() relies on Python's context manager protocol, which involves two special "magic" methods: __enter__() and __exit__(). 
1. Entry (__enter__()): When the with statement is executed, the open() function is called, which returns a file object. Python then automatically calls the file object's __enter__() method. This method opens the file and returns the file object itself, which is then bound to the variable specified after the as keyword (e.g., f in as f).
2. Execution of the Block: The code block indented under the with statement is executed, allowing you to perform read or write operations using the file object.
3. Exit (__exit__()): As soon as the execution leaves the with code block, Python automatically calls the file object's __exit__() method. This method handles the teardown logic, which, for a file object, means reliably calling the close() method to release the system resources associated with the file. 
```
2. What’s the difference between reading and splitting a file?
Answer:
```
Reading a file means opening the file and loading its content into memory, typically as a continuous string or a list of lines, depending on the method used (e.g., read(), readlines()). Splitting a file usually refers to dividing its content into smaller parts or segments based on some delimiter or criteria, such as lines, paragraphs, or custom separators. This split is done on the content after or while reading it (e.g., using split(), splitlines(), or manual slicing).
```
3. How would you handle a huge file (GB-size)?
Answer:
```
In Python, a common example is reading line-by-line in a loop, possibly buffering lines for batch processing. This method is efficient in both memory and performance for very large files. For extremely large files, leveraging memory mapping or chunked reading can speed up processing while keeping resource use practical.
```