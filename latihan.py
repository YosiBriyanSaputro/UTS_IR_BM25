import math

documents = {
    "D1": "ayam geprek crispy disajikan dengan sambal pedas dan nasi hangat",
    "D2": "chicken katsu crispy menggunakan saus mentai dan sayuran segar",
    "D3": "mie ayam bakso kuah hangat cocok dimakan saat hujan",
    "D4": "nasi goreng ayam pedas dengan telur dan kerupuk renyah",
    "D5": "ayam bakar madu disajikan dengan sambal manis dan lalapan",
    "D6": "seblak pedas berisi ceker ayam bakso dan kerupuk basah",
    "D7": "katsu rice bowl crispy dengan saus teriyaki dan mayones",
    "D8": "ayam goreng tepung crispy memiliki rasa gurih dan renyah",
    "D9": "mie goreng pedas spesial dengan telur sosis dan sayuran",
    "D10": "chicken steak crispy disajikan dengan kentang goreng dan saus lada hitam",
    "D11": "ayam penyet sambal pedas disajikan dengan tahu tempe dan lalapan",
    "D12": "burger ayam crispy dengan keju selada tomat dan saus spesial",
    "D13": "bakso mercon pedas memiliki kuah gurih dan isian cabai",
    "D14": "nasi ayam teriyaki dengan saus manis dan taburan wijen",
    "D15": "jamur crispy pedas cocok sebagai camilan ringan sore hari"
}

k1 = 1.5
b = 0.75

def preprocess(text):
    return text.lower().split()

tokenized_docs = {doc_id: preprocess(text) for doc_id, text in documents.items()}
doc_lengths = {doc_id: len(tokens) for doc_id, tokens in tokenized_docs.items()}

N = len(documents)
avgdl = sum(doc_lengths.values()) / N

def calculate_df(term):
    return sum(1 for tokens in tokenized_docs.values() if term in tokens)

def calculate_idf(term):
    df = calculate_df(term)
    return math.log(((N - df + 0.5) / (df + 0.5)) + 1)

def calculate_bm25(query, doc_id):
    query_terms = preprocess(query)
    doc_tokens = tokenized_docs[doc_id]
    doc_length = doc_lengths[doc_id]

    score = 0

    for term in query_terms:
        tf = doc_tokens.count(term)

        if tf == 0:
            continue

        idf = calculate_idf(term)

        numerator = tf * (k1 + 1)
        denominator = tf + k1 * (1 - b + b * (doc_length / avgdl))

        score += idf * (numerator / denominator)

    return score

def search(query):
    results = []

    for doc_id, text in documents.items():
        score = calculate_bm25(query, doc_id)
        results.append((doc_id, text, score))

    return sorted(results, key=lambda x: x[2], reverse=True)

query = "ayam crispy pedas"

print("Jumlah Dokumen:", N)
print("Average Document Length:", round(avgdl, 3))

print("\nIDF:")
for term in preprocess(query):
    print(term, "DF:", calculate_df(term), "| IDF:", round(calculate_idf(term), 3))

print("\nHASIL RANKING BM25:")
results = search(query)

for rank, (doc_id, text, score) in enumerate(results, start=1):
    print(f"{rank}. {doc_id} | Skor: {score:.3f} | {text}")