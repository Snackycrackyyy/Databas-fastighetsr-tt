import requests
import pdfplumber

# URL of the PDF
pdf_url = "https://www.lantmateriet.se/globalassets/om-lantmateriet/rattsinformation/handbocker/handbok-fbl.pdf"  # Replace with your PDF URL

# Download the PDF
response = requests.get(pdf_url)
with open("document.pdf", "wb") as pdf_file:
    pdf_file.write(response.content)

# Extract text from the PDF
text = ""
with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text()

# Save the extracted text to a file
with open("output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)
