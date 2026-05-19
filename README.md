# 📄 Implementasi Probabilistic Model BM25 pada Sistem Pencarian Dokumen PDF Berbasis Web

## 📌 Deskripsi Project

Project ini merupakan implementasi algoritma **BM25 (Best Matching 25)** sebagai salah satu metode **Probabilistic Model** pada sistem **Information Retrieval** untuk pencarian dokumen PDF.

Sistem dibangun menggunakan:
- Python
- Streamlit
- PyPDF2

Aplikasi mampu:
- Upload beberapa file PDF
- Melakukan preprocessing dokumen
- Menghitung skor BM25
- Menampilkan ranking dokumen
- Highlight keyword pencarian
- Menampilkan Top-K hasil pencarian

---

# 🚀 Fitur Sistem

✅ Upload multiple PDF  
✅ Query pencarian dokumen  
✅ Perhitungan BM25 otomatis  
✅ Ranking dokumen berdasarkan relevansi  
✅ Highlight keyword pada preview dokumen  
✅ Tampilan web sederhana menggunakan Streamlit  

---

# 🧠 Algoritma yang Digunakan

Metode utama yang digunakan adalah:

## BM25 (Best Matching 25)

BM25 merupakan algoritma pada Information Retrieval yang digunakan untuk menghitung tingkat relevansi dokumen terhadap query pengguna.

Rumus BM25:

```math
score(D,Q)=\sum_{i=1}^{n} IDF(q_i)\cdot
\frac{f(q_i,D)(k_1+1)}
{f(q_i,D)+k_1\left(1-b+b\cdot\frac{|D|}{avgdl}\right)}
```

Rumus IDF:

```math
IDF(q_i)=\ln\left(
\frac{N-n(q_i)+0.5}
{n(q_i)+0.5}+1
\right)
```

---

# 📂 Struktur Project

```bash
Retrival/
│
├── app.py
├── bm25.py
├── pdf_utils.py
├── requirements.txt
└── README.md
```

Penjelasan:
- `app.py` → antarmuka Streamlit
- `bm25.py` → implementasi algoritma BM25
- `pdf_utils.py` → membaca file PDF
- `requirements.txt` → daftar library

---

# ⚙️ Instalasi

## 1. Clone Repository

```bash
git clone https://github.com/username/nama-repository.git
```

---

## 2. Masuk Folder Project

```bash
cd nama-repository
```

---

## 3. Install Library

```bash
pip install -r requirements.txt
```

atau

```bash
py -m pip install -r requirements.txt
```

---

# ▶️ Menjalankan Program

```bash
streamlit run app.py
```

Jika error:

```bash
py -m streamlit run app.py
```

---

# 🧪 Cara Penggunaan

1. Jalankan aplikasi Streamlit
2. Upload beberapa file PDF
3. Masukkan query pencarian
4. Klik tombol pencarian
5. Sistem akan menampilkan:
   - skor BM25
   - ranking dokumen
   - preview dokumen
   - highlight keyword

---

# 📊 Evaluasi Sistem

Evaluasi dilakukan menggunakan:
- Precision
- Recall
- F1-Score

Hasil evaluasi menunjukkan bahwa sistem mampu menemukan dokumen relevan dengan baik menggunakan algoritma BM25.

---

# 🛠️ Library yang Digunakan

| Library | Fungsi |
|---|---|
| Streamlit | Web interface |
| PyPDF2 | Membaca file PDF |
| Math | Perhitungan BM25 |
| Re | Text preprocessing |

---

# 📖 Dataset

Dataset yang digunakan berupa 20 dokumen PDF bertema teknik informatika, seperti:
- Machine Learning
- Information Retrieval
- Cyber Security
- Deep Learning
- Artificial Intelligence
- Database Management System
- dan lainnya

---

# 👨‍💻 Author

Nama: [Nama Kamu]  
Mata Kuliah: Information Retrieval  
Semester: 6  
Metode: Probabilistic Model BM25

---

# 📌 Catatan

Project ini dibuat untuk memenuhi tugas UTS mata kuliah Information Retrieval.