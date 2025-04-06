from aimakerspace.text_utils import CharacterTextSplitter
import os
import PyPDF2
import io
from typing import List

class PDFTextExtractor:
    """
    Class to extract text from PDF files and prepare it for RAG applications.
    """
    def __init__(self, pdf_path: str):
        """
        Initialize the PDFTextExtractor with path to a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
        """
        self.pdf_path = pdf_path
        self.documents = []
        self.metadata = []
        
    def extract_text(self) -> List[str]:
        """
        Extract text from the PDF file
        
        Returns:
            List[str]: List containing the extracted text
        """
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")
        
        try:
            with open(self.pdf_path, 'rb') as file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Get total number of pages
                num_pages = len(pdf_reader.pages)
                
                # Extract text from each page
                all_text = ""
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    all_text += page.extract_text() + "\n\n"
                    
                    # Store page metadata
                    self.metadata.append({
                        'source': os.path.basename(self.pdf_path),
                        'page_number': page_num + 1,
                        'total_pages': num_pages
                    })
                
                self.documents.append(all_text)
                return self.documents
                
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    def split_documents(self, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
        """
        Split the extracted documents into smaller chunks
        
        Args:
            chunk_size (int): Size of each chunk
            chunk_overlap (int): Overlap between chunks
            
        Returns:
            List[str]: List of document chunks
        """
        if not self.documents:
            self.extract_text()
            
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        return text_splitter.split_texts(self.documents)