from django.shortcuts import render

# Create your views here.
def teste(request):
    return render(
        request,
        'site_escola/index.html',
                {
            'title_page': 'Escola'
        }
    )
