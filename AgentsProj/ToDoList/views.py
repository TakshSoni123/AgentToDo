from django.shortcuts import render
from .models import Agent, todo
from passlib.hash import pbkdf2_sha256
from rest_framework.response import Response
from rest_framework import viewsets
import requests
from rest_framework.decorators import api_view
from .serializer import AgentSerializer, todoSerializer
import json

user_id = ''

@api_view(['GET'])
def showagents(request):
    if request.method=='GET':
        query = Agent.objects.all()
        serialize =AgentSerializer(query, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def showTodo(request):
    if request.method=='GET':
        query = todo.objects.all()
        serialize =todoSerializer(query, many=True)
        return Response(serialize.data)

# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('password') and request.POST.get('name'):
            new_agent = Agent()
            new_agent.agent_name = request.POST.get('name')
            new_agent.agent_id = request.POST.get('id')
            x = request.POST.get('password')
            enc_pass = pbkdf2_sha256.encrypt(x)

            new_agent.agent_pass = enc_pass
            new_agent.save()
            user_id = new_agent.agent_id
            return render(request,'todo.html', {'id': new_agent.agent_id})


    else:
        return render(request, 'signup.html', {})

def login(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('password'):
            callapi = requests.get('http://localhost:8000/show')
            results = callapi.json
            print(results)
            agent = Agent()
            agent.agent_id = request.POST.get('id')
            i=0

            for i in results:
                if(i['agent_id']== agent.agent_id):
                    i=1
                    if(agent.verifyPass(request.POST.get('password'), i['agent_pass'])):
                        return render(request, 'todo.html')
                        break
            if(i==0):
                return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def todoView(request):
    if request.method=='POST':
        if request.POST.get('id') and request.POST.get('title') and request.POST.get('date'):
            new_todo = todo()
            new_todo.agent_id = request.POST.get('id')
            new_todo.title = request.POST.get('title')
            new_todo.desc = request.POST.get('desc')
            new_todo.date = request.POST.get('date')
            new_todo.save()
            callapi = requests.get('http://localhost:8000/showtodoAPI')
            results = callapi.json()
            context = {
                'query': results,
                'id':user_id
            }
            return render(request, 'todo.html', context)
    else:
        callapi = requests.get('http://localhost:8000/showtodoAPI')
        results = callapi.json()
        context = {
            'query': results,
            'id': user_id
        }
        return render(request, 'todo.html', context)


