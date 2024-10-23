import os
import fitz  # PyMuPDF


# Função para extrair o texto de cada página de um PDF e salvar em um arquivo de texto
def extract_text_from_pdfs(input_dir, output_dir):
    # Certifique-se de que o diretório de saída exista
    os.makedirs(output_dir, exist_ok=True)

    # Percorrer todos os arquivos e subdiretórios no diretório de entrada
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                lote_name = os.path.basename(root)  # O nome do diretório é considerado como "Lote"
                output_file_path = os.path.join(output_dir, f"{lote_name}_{file}.txt")

                # Abrir o PDF e extrair o texto
                with fitz.open(pdf_path) as pdf_document:
                    with open(output_file_path, "w", encoding="utf-8") as text_file:
                        for page_number in range(len(pdf_document)):
                            page = pdf_document.load_page(page_number)
                            text = page.get_text()
                            text_file.write(f"Page {page_number + 1}\n")
                            text_file.write(text)
                            text_file.write("\n\n")


if __name__ == "__main__":
    input_directory = "C:\\Users\\josed\\OneDrive\\Documentos\\CASAMENTO_OCRED\\CASAMENTO_B057"  # Substitua pelo diretório onde estão os PDFs
    output_directory = "C:\\Users\\josed\\OneDrive\\Documentos\\CASAMENTO_EXTRACT\\CASAMENTO_B0"  # Substitua pelo diretório de saída dos arquivos de texto
    extract_text_from_pdfs(input_directory, output_directory)
    print("Extração de texto concluída.")
