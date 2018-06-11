from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello World")


def root_page(request):
    return HttpResponse("Root HomePage")

def random_number(request,max_rand=100):
    random_number= random.randrange(0,int(max_rand))

    msg = "random number between 0 and %s : %d" % (max_rand,random_number)
    return  HttpResponse(msg)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
