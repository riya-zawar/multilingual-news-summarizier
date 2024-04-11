from gensim.models import Word2Vec
from gensim import summarization

def summarize_text(sentences, words):
    model = Word2Vec(words, min_count=1, size=100, window=5)

    sentence_vectors = []
    for sentence in words:
        sentence_vec = sum([model.wv[word] for word in sentence]) / len(sentence)
        sentence_vectors.append(sentence_vec)

    similarity_matrix = [[model.wv.similarity(w1, w2) for w1 in sentence_vectors] for w2 in sentence_vectors]

    summary = summarize(" ".join(sentences), ratio=0.3, word_count=None, split=False)

    return summary
