from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Question
import random

def test(request):
    question=Question.objects.get(id=random.randint(1,3))
    q=question.que
    options=[
    question.optiona,
    question.optionb,
    question.optionc,
    question.optiond,

    ]
    data={
    'que':q,'options':options
    }
    res=render(request,'exam/textpepar.html',data)
    return res
def result(request):
    s="<h1>result page</h1>"
    return HttpResponse(s)



# def test(request):
#     s="<h1>test page</h1>"
#     return HttpResponse(s)
# def result(request):
#     s="<h1>result page</h1>"
#     return HttpResponse(s)
