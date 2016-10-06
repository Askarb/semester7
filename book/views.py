from django.http import HttpResponse
from django.shortcuts import redirect

from book.models import Books, Customer
from django.template import loader
from book.forms import CustomerForm


def index(request):
    context = {
        'books': Books.objects.all(),
    }
    template = loader.get_template("book_index.html")
    return HttpResponse(template.render(context, request))


def checkout(request, id):
    context = {
        'form': CustomerForm,
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            import datetime
            new_customer = Customer.objects.create(name=name, address=address, book_id=id, date=datetime.datetime.now())
            new_customer.save()
            book = Books.objects.get(id=id)
            book.count = book.count - 1;
            book.save()
            return redirect('/books/')
    template = loader.get_template("checkout.html")
    return HttpResponse(template.render(context, request))
