from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == "name":
        phones = Phone.objects.all().order_by('name')
        template = 'catalog.html'
        context = {'phones': phones}
    elif sort == "min_price":
        phones = Phone.objects.all().order_by('price')
        template = 'catalog.html'
        context = {'phones': phones}
    elif sort == "max_price":
        phones = Phone.objects.all().order_by('-price')
        template = 'catalog.html'
        context = {'phones': phones}
    else:
        phones = Phone.objects.all()
        template = 'catalog.html'
        context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
