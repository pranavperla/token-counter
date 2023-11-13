import PyPDF2

def count_tokens_in_pdf(pdf_path):
    total_tokens = 0

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            tokens = text.split()
            total_tokens += len(tokens)

    return total_tokens

# Example usage
pdf_file_path = '1daytoken.pdf'
token_count = count_tokens_in_pdf(pdf_file_path)
print(f"Total tokens in the PDF file: {token_count}")
