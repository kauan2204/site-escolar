from django.shortcuts import render

# Create your views here.
def taskviews(request):
    return render(
        request,
        'site_escola/task.html',
        {
            'title_page': 'tarefas',
        }
    )
