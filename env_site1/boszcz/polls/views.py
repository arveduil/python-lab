from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from .models import Question, Choice,Category
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic




class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    context_object_name = 'latest_question_list'

    def get_queryset(self):
         return Question.objects.filter(
             pub_date__lte=timezone.now()
         ).order_by('-pub_date')[:5]

    # def get_queryset(self):
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def add_choice(request, question_id):
    question_given = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        text = request.POST.get("new_choice", None)
        choice = Choice(question=question_given , choice_text=text)
        choice.save()
        return render(request, 'polls/add_choice.html', {'question': question_given})

    return render(request, 'polls/add_choice.html',
                  {'question': question_given},
                  )
#
# def add_question(request,category_id):
#     category_given = get_object_or_404(Category, pk=category_id)
#     return render(request, 'polls/add_question.html',
#                   {'question': question_given},
#                   )



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)


    return render(request, 'polls/results.html',
                  {'question': question},
                  )



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:

        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

