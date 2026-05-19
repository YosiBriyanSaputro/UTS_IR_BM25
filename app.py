import re
import streamlit as st
from bm25 import BM25
from pdf_utils import extract_text_from_pdf


# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="BM25 PDF Search Engine",
    page_icon="🔎",
    layout="wide"
)


# =========================
# FUNGSI HIGHLIGHT KEYWORD
# =========================
def highlight_keywords(text, query):
    """
    Memberi tanda highlight pada kata yang sesuai dengan query.
    """

    words = query.lower().split()
    highlighted_text = text

    for word in words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        highlighted_text = pattern.sub(
            lambda match: f"<mark>{match.group(0)}</mark>",
            highlighted_text
        )

    return highlighted_text


# =========================
# TAMPILAN UTAMA
# =========================
st.title("🔎 Sistem Pencarian Dokumen PDF Menggunakan BM25")

st.write(
    "Aplikasi ini digunakan untuk mencari dokumen PDF yang paling relevan "
    "berdasarkan query pengguna menggunakan algoritma BM25."
)

st.divider()


# =========================
# SIDEBAR PARAMETER
# =========================
st.sidebar.header("⚙️ Pengaturan BM25")

k1 = st.sidebar.number_input(
    "Nilai k1",
    min_value=0.1,
    max_value=3.0,
    value=1.5,
    step=0.1
)

b = st.sidebar.number_input(
    "Nilai b",
    min_value=0.0,
    max_value=1.0,
    value=0.75,
    step=0.05
)

top_k = st.sidebar.number_input(
    "Jumlah Top-K Ranking",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)


# =========================
# UPLOAD PDF
# =========================
uploaded_files = st.file_uploader(
    "📂 Upload beberapa file PDF",
    type=["pdf"],
    accept_multiple_files=True
)


# =========================
# INPUT QUERY
# =========================
query = st.text_input(
    "Masukkan query pencarian",
    placeholder="Contoh: machine learning, sistem informasi, ayam crispy pedas"
)


# =========================
# TOMBOL CARI
# =========================
if st.button("🔍 Cari Dokumen"):
    if not uploaded_files:
        st.warning("Silakan upload minimal 1 file PDF terlebih dahulu.")

    elif query.strip() == "":
        st.warning("Silakan masukkan query pencarian terlebih dahulu.")

    else:
        documents = {}

        with st.spinner("Sedang membaca isi PDF..."):
            for uploaded_file in uploaded_files:
                text = extract_text_from_pdf(uploaded_file)
                documents[uploaded_file.name] = text

        bm25 = BM25(documents, k1=k1, b=b)
        results = bm25.search(query, top_k=top_k)

        st.success("Pencarian selesai!")

        st.subheader("📌 Informasi Koleksi Dokumen")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Jumlah Dokumen", bm25.N)

        with col2:
            st.metric("Average Document Length", f"{bm25.avgdl:.3f}")

        with col3:
            st.metric("Jumlah Hasil Ditampilkan", len(results))

        st.divider()

        st.subheader("🏆 Hasil Ranking BM25")

        for rank, result in enumerate(results, start=1):
            doc_id = result["doc_id"]
            score = result["score"]
            text = result["text"]
            length = result["length"]

            preview = text[:1500]
            preview = highlight_keywords(preview, query)

            with st.expander(
                f"Ranking {rank} | {doc_id} | Skor BM25: {score:.4f}"
            ):
                st.write(f"**Nama Dokumen:** {doc_id}")
                st.write(f"**Panjang Dokumen:** {length} term")
                st.write(f"**Skor BM25:** {score:.4f}")

                st.markdown("**Preview Isi Dokumen:**")
                st.markdown(preview, unsafe_allow_html=True)

        st.divider()

        st.subheader("📊 Tabel Ringkasan Hasil")

        table_data = []

        for rank, result in enumerate(results, start=1):
            table_data.append({
                "Ranking": rank,
                "Nama Dokumen": result["doc_id"],
                "Skor BM25": round(result["score"], 4),
                "Panjang Dokumen": result["length"]
            })

        st.dataframe(table_data, use_container_width=True)