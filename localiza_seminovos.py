import os
from PyPDF2 import PdfMerger

def merge_pdfs_from_folder(folder_path, output):
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

    sorted_pdfs = sorted(pdf_files, key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))

    if not sorted_pdfs:
        print("Nenhum arquivo PDF numerado encontrado na pasta.")
        return

    merger = PdfMerger()
    try:
        for pdf in sorted_pdfs:
            pdf_path = os.path.join(folder_path, pdf)
            print(f"Adicionando: {pdf_path}")
            merger.append(pdf_path)

        merger.write(output)
        merger.close()
        print(f"Merged PDF saved as '{output}'")
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = os.getcwd()  # Usar a pasta onde o script está localizado
output_file = "arquivo_merged.pdf"  # Nome do arquivo de saída

merge_pdfs_from_folder(folder_path, output_file)
