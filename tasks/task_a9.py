from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def task_a9():
    with open("data/comments.txt", "r") as file:
        comments = file.readlines()
    
    # Compute TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(comments)
    
    # Compute pairwise cosine similarities
    similarities = cosine_similarity(tfidf_matrix)
    
    # Find the most similar pair
    most_similar = None
    max_sim = -1
    for i in range(len(similarities)):
        for j in range(i + 1, len(similarities[i])):
            if similarities[i][j] > max_sim:
                max_sim = similarities[i][j]
                most_similar = (comments[i].strip(), comments[j].strip())
    
    # Write the most similar pair to a new file
    with open("data/comments-similar.txt", "w") as file:
        file.write("\n".join(most_similar))