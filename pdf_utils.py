from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Mengekstrak teks dari file PDF yang di-upload melalui Streamlit.

    Parameter:
    uploaded_file = file PDF dari st.file_uploader

    Output:
    text = isi teks dari seluruh halaman PDF
    """

    text = ""

    try:
        reader = PdfReader(uploaded_file)

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        text = f"ERROR membaca PDF: {e}"

    return text