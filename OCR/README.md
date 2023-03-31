# Optical Character Recognition

 a technology that recognizes and pulls out text in images like scanned documents and photos.

 INSTALL :
 1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

 2. install python package using pip: pip install pytesseract

 3. Set the tesseract path in the script before using :

    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' (Base on default installation path)