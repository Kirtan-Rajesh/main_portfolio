import PyPDF2
with open(r'd:\portfolio\src\Kirtan_Resume (4).pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
with open(r'd:\portfolio\resume_text.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(text)
