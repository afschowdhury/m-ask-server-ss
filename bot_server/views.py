from django.http import JsonResponse
from .models import Query
from .serializers import QuerySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bot_server.nlp_core.qna_answer import find_answer_qna






@api_view(['GET','POST'])
def query_list(request, format=None):
    
    if request.method == 'GET':
    
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many= True)
        
        return Response(serializer.data )
    
    if request.method == 'POST':
        
        data = request.data
        
        
        question = data['question']
        
        ans = find_answer_qna(question)
        print(f"Answer: {ans}")
        
        
        serializer = QuerySerializer(data = {'question':question,'answer':ans})
        
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status.HTTP_201_CREATED)
        
        
