import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_de_arquivos = os.listdir("arquivos") # Localiza o diretório que contém os arquivos que serão unificados em um novo PDF
lista_de_arquivos.sort() # Ordena os arquivos PDF

for arquivo in lista_de_arquivos: # Loop que irá ler os arquivos PDF e unificar em um arquivo final
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF final.pdf") # Finalização do código para criação do novo arquivo com os PDFs unificados