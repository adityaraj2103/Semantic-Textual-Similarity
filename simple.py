# Two lists of sentences
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

def compare(sentence1, sentence2):

    #Compute embedding for both lists
    embeddings1 = model.encode(sentence1, convert_to_tensor=True)
    embeddings2 = model.encode(sentence2, convert_to_tensor=True)

    #Compute cosine-similarits
    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
    return cosine_scores