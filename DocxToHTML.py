import mammoth

with open("/Users/kaartik/Desktop/document.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value  # The generated HTML
    messages = result.messages
mammoth.convert_to_html(docx_file)
