from sentence_transformers import SentenceTransformer
import numpy as np
import torch
from sentence_transformers.util import semantic_search
from transformers import  pipeline
import random
import pickle
import json



retriever_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")


with open('bot_server/nlp_core/data/data_v4.json', 'r') as f:
  data = json.load(f)

ques_embds = np.load('bot_server/nlp_core/data/ques_embeddings.npy')

with open('bot_server/nlp_core/data/questions.bin', 'rb') as f:
   
    ques = pickle.load(f)







def find_answer_qna(query):
  
  
  q_emb = retriever_model.encode(query)
  query_embeddings = torch.FloatTensor(q_emb)
  hits = semantic_search(query_embeddings, ques_embds, top_k = 1)
  answers = []
  for i in range (len(hits[0])):

  
  
    answers.append(ques[hits[0][i]["corpus_id"]])
  for item in data:
    for qas in item['qas']:
      for qts in qas['qtns']:
        for q in answers:
          if q == qts:
            # print(f"Question: {q} Answer : {qas['answer']}")
            return qas['answer']
  return "Invalid Input. Try with another question !"
  

