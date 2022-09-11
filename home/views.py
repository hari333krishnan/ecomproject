from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def home(request, c_slug=None):
    c_page = None
    prod = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug)
        prod = Products.objects.filter(category=c_page, available=True)
    else:
        prod = Products.objects.all().filter(available=True)
    cat = Categ.objects.all()
    paginator=Paginator(prod,16)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        p=paginator.page(page)
    except(InvalidPage,EmptyPage):
        p=paginator.page(paginator.num_pages)

    return render(request, "index.html", {'pr': prod, 'cat': cat,'pro':p})


def ProdDetails(request, c_slug, prod_slug):
    try:
        pro = Products.objects.get(category__slug=c_slug, slug=prod_slug)
    except Exception as e:
        raise e
    c_page = get_object_or_404(Categ, slug=c_slug)
    pr = Products.objects.filter(category=c_page, available=True)
    return render(request, "detail.html", {'pro': pro, 'pr': pr})


def Searching(request):
    query = None
    prod = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, "search.html", {'qr': query, 'pr': prod})
