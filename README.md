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
