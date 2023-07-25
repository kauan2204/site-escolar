from django.shortcuts import render
from django import forms
from site_escola.forms import QuizForm, QuizQuestionForm




# Create your views here.
def createtask(request):
    if request.method == "POST":
        botao = 0
        form = QuizForm(request.POST)
        quizquestio = QuizQuestionForm(request.POST)
        teste = False
        context = {
            'title_page': 'create task',
            'form': form,
            'questions': quizquestio,
            'teste': teste,
            'numero': botao,
        }

        if form.is_valid():
            if quizquestio.is_valid():
                form.save()
                quizquestio.save()

            # nem_quiz = form.save()
            count = 0
            if 'teste' in request.POST:
                count += 1
                print(count)
                
             
        return render(
        request,
        'site_escola/create_task.html',
        context,
    )

    return render(
        request,
        'site_escola/create_task.html',
        {
            'title_page': 'create task',
            'form': QuizForm(request.POST),
            'teste': False
        }
    )
