# Vocab Practice Selector 🎯

A lightweight Python CLI tool designed to automate daily vocabulary practice. It recursively scans a given directory for Anki-style `.csv` files, extracts English words along with their translations, and randomly selects exactly 20 unique words for pronunciation and sentence-building exercises.

## Features
- **Recursive Search:** Automatically finds all `.csv` files in the target folder and its subdirectories.
- **Anki-Format Support:** Correctly parses rows using the `;` delimiter (e.g., `word;translation`).
- **Smart Selection:** Filters out empty rows and duplicates, outputting a clean list of 20 random words.
- **CLI Interface:** Built with `argparse` for easy terminal usage, including built-in path validation and `--help` support.

## Usage
Run the script from your terminal, providing the path to your vocabulary folder:
```bash
python3 main.py /path/to/your/csv/folder
