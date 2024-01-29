from django.shortcuts import render
from datetime import datetime  

# Create your views here.


# def index(req):
#     username = input('enter username=')
#     context={}
#     context['username']=username
#     #return render(req,'index.html',{"username":username})
#     return render(req,'index.html',context)

def index(req):
    username="Admin"
    products=["mobies","laptop","camera"]
    movies={"the godfather":4,"the shawshank":5,"the dark knight":4}
    fruitdata=fruits()
    context={"username":username,"products":products,"movies":movies,"fruitdata":fruitdata}
    return render(req,'index.html',context)

def fruits():
    fruitlist=("apple","banana","orange","mango")
    return fruitlist

def login(req):
    username=input('enter username=')
    todaysdate=datetime.now() 
    context={'username':username,'todaysdate':todaysdate}
    return render(req,'login.html',context)

