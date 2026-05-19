import math
import re
from collections import Counter


class BM25:
    """
    Class BM25 digunakan untuk menghitung skor relevansi dokumen
    terhadap query menggunakan algoritma BM25.
    """

    def __init__(self, documents, k1=1.5, b=0.75):
        """
        Inisialisasi data awal BM25.

        Parameter:
        documents = kumpulan dokumen dalam bentuk dictionary
                    contoh: {"D1": "isi dokumen", "D2": "isi dokumen"}
        k1        = parameter untuk mengatur pengaruh term frequency
        b         = parameter untuk normalisasi panjang dokumen
        """

        self.documents = documents
        self.k1 = k1
        self.b = b
        self.doc_ids = list(documents.keys())

        # Melakukan preprocessing pada seluruh dokumen
        self.tokenized_docs = {
            doc_id: self.preprocess(text)
            for doc_id, text in documents.items()
        }

        # Menghitung panjang setiap dokumen
        self.doc_lengths = {
            doc_id: len(tokens)
            for doc_id, tokens in self.tokenized_docs.items()
        }

        # Menghitung jumlah seluruh dokumen
        self.N = len(self.documents)

        # Menghitung rata-rata panjang dokumen
        self.avgdl = (
            sum(self.doc_lengths.values()) / self.N
            if self.N > 0 else 0
        )

    def preprocess(self, text):
        """
        Melakukan text preprocessing sederhana:
        1. Case folding
        2. Menghapus simbol/tanda baca
        3. Tokenizing
        """

        # Case folding: mengubah semua huruf menjadi kecil
        text = text.lower()

        # Menghapus karakter selain huruf, angka, dan spasi
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

        # Tokenizing: memecah teks menjadi kata
        tokens = text.split()

        return tokens

    def calculate_df(self, term):
        """
        Menghitung Document Frequency (DF).

        DF adalah jumlah dokumen yang mengandung term tertentu.
        """

        count = 0

        for tokens in self.tokenized_docs.values():
            if term in tokens:
                count += 1

        return count

    def calculate_idf(self, term):
        """
        Menghitung Inverse Document Frequency (IDF).

        IDF digunakan untuk mengukur seberapa penting sebuah term.
        Term yang jarang muncul akan memiliki IDF lebih besar.
        """

        df = self.calculate_df(term)

        idf = math.log(((self.N - df + 0.5) / (df + 0.5)) + 1)

        return idf

    def calculate_bm25(self, query, doc_id):
        """
        Menghitung skor BM25 untuk satu dokumen terhadap query.
        """

        # Preprocessing query
        query_terms = self.preprocess(query)

        # Mengambil token dokumen berdasarkan doc_id
        doc_tokens = self.tokenized_docs[doc_id]

        # Mengambil panjang dokumen
        doc_length = self.doc_lengths[doc_id]

        # Menghitung frekuensi kemunculan setiap term di dokumen
        term_frequency = Counter(doc_tokens)

        score = 0

        for term in query_terms:
            # TF = frekuensi term query dalam dokumen
            tf = term_frequency[term]

            # Jika term tidak muncul, lanjut ke term berikutnya
            if tf == 0:
                continue

            # Menghitung IDF term
            idf = self.calculate_idf(term)

            # Bagian pembilang rumus BM25
            numerator = tf * (self.k1 + 1)

            # Bagian penyebut rumus BM25
            denominator = tf + self.k1 * (
                1 - self.b + self.b * (doc_length / self.avgdl)
            )

            # Menambahkan skor term ke skor total dokumen
            score += idf * (numerator / denominator)

        return score

    def search(self, query, top_k=5):
        """
        Mencari dokumen paling relevan berdasarkan query.

        Output:
        daftar dokumen yang sudah diurutkan berdasarkan skor BM25 terbesar.
        """

        results = []

        for doc_id in self.doc_ids:
            score = self.calculate_bm25(query, doc_id)

            results.append({
                "doc_id": doc_id,
                "score": score,
                "text": self.documents[doc_id],
                "length": self.doc_lengths[doc_id]
            })

        # Mengurutkan hasil berdasarkan skor terbesar
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # Mengambil top-k hasil teratas
        return results[:top_k]