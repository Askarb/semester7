from django.http import HttpResponse
from django.template import loader
from fibonacci.forms import FibonacciForm
from fibonacci.core_fibonacci import fibonacci


def index(request):
    context = {
        'status': 0,
        'form': FibonacciForm(),
    }
    template = loader.get_template("index_fibonacci.html")
    if request.method == "POST":
        form = FibonacciForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            context['a'] = a
            context['result'] = fibonacci(a)
            context['a'] = a
            context['status'] = 1
        else:
            context['status'] = 2
            context['comment'] = 'Enter only positive integer!!!'
    return HttpResponse(template.render(context, request))
