from sentence_transformers import SentenceTransformer
import numpy as np
import torch
from sentence_transformers.util import semantic_search
from transformers import  pipeline
import random
import pickle


# retriever_model = SentenceTransformer('/bot_server/nlp_core/models/afs-ml-st')
# qa_model_location = '/home/shagoto/codes/nlp/b-server-askmujib/bot_server/nlp_core/models/afs_xlm_roberta'
# qa_model = pipeline("question-answering",model = qa_model_location,tokenizer=qa_model_location)

retriever_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
import json

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
  
  


  
  
  
  
  
  
  
  
#   q_emb = retriever_model.encode(query)
#   respns = []

#   query_embeddings = torch.FloatTensor(q_emb)
#   hits = semantic_search(query_embeddings, context_embeddings, top_k = 7)
# #   print(f"User's Question: {query}")
#   for i in range(len(hits[0])):
#     context = contexts[hits[0][i]["corpus_id"]]
#     qa_input = {'question': query,'context': context}
    
#     res = qa_model(qa_input)
#     respns.append(res)
    
#   max_score = max([ans['score'] for ans in respns])
#   for res in respns:
#     if max_score == res['score']:
#     #   print(f"{'*'*15} QA models best answer:  {'*'*15}")
#     #   print(res['answer'])
#         return res['answer']