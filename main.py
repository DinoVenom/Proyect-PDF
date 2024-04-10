import PyPDF2

def extraer_texto(pdf_filename):
    texto = ""
    with open(pdf_filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_paginas = pdf_reader.numPages
        for pagina_num in range(num_paginas):
            pagina = pdf_reader.getPage(pagina_num)
            texto += pagina.extractText()
    return texto

def main():
    pdf_filename = input("Introduce el nombre del archivo PDF: ")
    try:
        texto_extraido = extraer_texto(pdf_filename)
        print("Texto extraído del PDF:")
        print(texto_extraido)
    except FileNotFoundError:
        print("El archivo PDF especificado no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error al intentar extraer el texto del PDF:", str(e))

if __name__ == "__main__":
    main()