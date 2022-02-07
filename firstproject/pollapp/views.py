from django.http import HttpResponseRedirect
from .models import questions, choice
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list = questions.objects.order_by('date')[:5]
    context = {'latest_question_list': latest_question_list}
    print(latest_question_list.first().id)
    return render(request, 'pollapp/index.html', context)

    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

     
def detail(request, question_id):
    question = get_object_or_404(questions, pk=question_id)
    return render(request, 'pollapp/detail.html', {'question': question})

    # return render(request, 'polls/detail.html', {'question': question})
    # question = get_object_or_404(questions, pk=question_id)
    # return render(request, 'pollapp/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(questions, pk=question_id)
    return render(request, 'pollapp/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pollapp/detail.html', {'question': question,'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('pollapp:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     latest_question_list = questions.objects.order_by('date')[:5]
#     template = loader.get_template('pollapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
print("views")