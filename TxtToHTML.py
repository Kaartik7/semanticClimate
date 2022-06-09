import docx
from docx import Document
import re
import os

doc = Document()
nomination = doc.add_paragraph("Hello")
doc.save('nomination.docx')
