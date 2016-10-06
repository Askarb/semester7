from django.http import HttpResponse
from django.template import loader
from .forms import QuadraticForm
from univer.settings import STATIC_URL
from .core_quadratic import solve_quadratic


def index(request):
    context = {
        'form': QuadraticForm(),
        'STATIC_URL': STATIC_URL,
        'result': 0
    }
    template = loader.get_template("quadratic.html")
    if request.method == "POST":
        form = QuadraticForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            context['a'] = a
            context['b'] = b
            context['c'] = c
            context['result'] = 1
            context.update(solve_quadratic(a, b, c))
        else:
            context['result'] = 2
            context['comment'] = 'Enter only real or integer!!!'
    return HttpResponse(template.render(context, request))
