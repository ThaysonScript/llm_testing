from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplit:
    def __init__(self, size_chunk, overlap_chunk, start_index, document):
        self.__split_text(self, size_chunk, overlap_chunk, start_index, document)


    def __split_text(self, size_chunk, overlap_chunk, start_index=True, document):
        '''
        chunk_size=1024, chunk_overlap=150

        :param size_chunk:
        :param overlap_chunk:
        :param document:
        :return: RecursiveCharacterTextSplitter
        '''
        return RecursiveCharacterTextSplitter(chunk_size=size_chunk, chunk_overlap=overlap_chunk, add_start_index=start_index).split_documents(documents=document)