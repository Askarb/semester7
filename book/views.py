from django.http import Http404
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect, render_to_response, render

from book.models import Books, Customer, Phone
from django.template import loader
from book.forms import CustomerForm, LoginForm
from django.core.paginator import Paginator, PageNotAnInteger


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


def football_index(request):
    context = {}
    template = loader.get_template("foot_index.html")
    return HttpResponse(template.render(context, request))


def login_index(request):
    context = {
        'form': LoginForm
    }
    template = loader.get_template("login.html")


    # print("Sending Email")
    # mail_title = 'Test Email'
    # message = 'This is a test email.'
    # email = settings.DEFAULT_FROM_EMAIL
    # recipients = [settings.DEFAULT_TO_EMAIL]
    # send_mail('Subject here', 'Hi nooruz, Django mail SMTP server', settings.EMAIL_HOST_USER, ['oskar95.kg@mail.ru'], fail_silently=False)
    #
    # from twilio.rest import TwilioRestClient
    # # put your own credentials here
    # ACCOUNT_SID = 'AC321facd931a6cd4f8652bd5d4c1b30ec'
    # AUTH_TOKEN = '27ad68c3ca34a8aa5ffcfa8cef44c959'
    #
    # client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    #
    # client.messages.create(
    #     to='+996700401014',
    #     from_='+12016901725',
    #     body='Kanday????????????????????????????????????????????????????????????!!!'
    # )

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
            book.count = book.count - 1
            book.save()
            template = loader.get_template("thanks.html")
    return HttpResponse(template.render(context, request))


def viewbook(request, id):
    context = {
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


def phone(request):
    contact_list = Phone.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        phones = paginator.page(1)
    except Phone:
        # If page is out of range (e.g. 9999), deliver last page of results.
        phones = paginator.page(paginator.num_pages)

    context = {
        'phone': phones,
        'before': range(1,phones.number),
        'after': range(phones.number+1, phones.paginator.num_pages+1)
    }
    return render(request, 'phone_index.html', context)



