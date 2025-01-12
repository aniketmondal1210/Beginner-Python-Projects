from pdfmerge import pdfmerge

def merged_pdfs(pdf_list, output_filename):
    pdfmerge(pdf_list, output_filename)

pdf_list = ['file1.pdf', 'file2.pdf', 'file3.pdf']
output_filename = 'output.pdf'

merged_pdfs(pdf_list, output_filename)

print('PDFs merged successfully!')
print('Your PDFs is merged to: ' + output_filename)
