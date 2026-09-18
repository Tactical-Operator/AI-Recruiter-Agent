from pypdf import PdfReader

pdf_path = "candidates/ready_for_testing.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

print("==========================================")
print("              CV CONTENT                  ")
print("==========================================")

print(text)

