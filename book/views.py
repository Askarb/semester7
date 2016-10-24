from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response, render

from book.models import Books, Customer
from django.template import loader
from book.forms import CustomerForm


def index(request):
    context = {}
    template = loader.get_template("visual_index.html")
    return HttpResponse(template.render(context, request))


def index_book(request):
    context = {
        'books': Books.objects.all(),
    }
    template = loader.get_template("book_index.html")
    return HttpResponse(template.render(context, request))


def checkout(request, id):
    context = {
        'form': CustomerForm,
    }
    template = loader.get_template("checkout.html")
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            import datetime
            book = Books.objects.get(id=id)
            new_customer = Customer.objects.create(name=name, address=address, book_id=book, date=datetime.datetime.now())
            new_customer.save()
            book.count = book.count - 1;
            book.save()
            template = loader.get_template("thanks.html")

    return HttpResponse(template.render(context, request))


def viewbook(request, id):
    context={
        'status': 0,
    }
    template = loader.get_template("book_view.html")
    try:
        context['book'] = Books.objects.get(id=id)
        return HttpResponse(template.render(context, request))
    except Books.DoesNotExist:
        raise Http404("Object with such ID doesn't exist!!!")


def myredirect(request):
    return redirect("/")


