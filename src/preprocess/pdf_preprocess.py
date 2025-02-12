from langchain_community.document_loaders import PyPDFLoader
import os

docs_list = []
i = 1

def return_docs_list_loaded(diretorio_base='../data/minuta/'):
    for nome_arquivo in os.listdir(diretorio_base):
        if nome_arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(diretorio_base, nome_arquivo)

            loader = PyPDFLoader(caminho_pdf)

            print(f'loader: {loader}\n\n')

            docs = await loader.aload()

            print(f'docs_loader: {docs[0].page_content[:100]}\n\n')
            print(docs[0].metadata)

            docs_list.append(docs)

    return docs_list