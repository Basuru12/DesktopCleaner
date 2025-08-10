# 📂 File Sorter Script

A simple Python script that automatically organizes files in the current directory into folders based on their file type.

## ✨ Features
- Organizes files into predefined folders (Excel, Text Files, Images, Documents, PDFs, Filmora, etc.)
- Case-insensitive extension matching (e.g., `.JPG` and `.jpg` are treated the same)
- Automatically creates folders if they don’t exist
- Prevents overwriting files by renaming duplicates (e.g., `file (1).txt`)
- Works with any folder you run it from

## 🗂 Folder Structure
When you run the script, it will create (if missing) these folders in the current directory:

- `Excel` → `.xlsx`
- `textFiles` → `.txt`
- `PNGimages` → `.png`
- `Documents` → `.docx`
- `JPGimages` → `.jpg`, `.jpeg`
- `PDFfiles` → `.pdf`
- `Filmora` → `.wfp`

  ## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-sorter.git
   cd file-sorter
Place the file_sorter.py script in the folder containing the files you want to sort.

Run the script:

bash
Copy
Edit
python file_sorter.py
Your files will be moved into their corresponding folders.

⚙️ Requirements
Python 3.7+

No third-party dependencies (uses only built-in libraries)

📝 How It Works
The script looks for files in the current working directory.

It checks the file’s extension against a predefined mapping of extensions to folders.

If a match is found:

Creates the destination folder if it doesn’t exist

Moves the file to that folder

If a file with the same name exists, renames it to avoid overwriting
