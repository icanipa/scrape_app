from django.shortcuts import render

from .models import Page
from .forms import TitleForm
from .utils.scrape_link import scrape_link


# Create your views here.

def index(request):
    scrape_list = Page.objects.all()
    form = TitleForm()
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            scrape_link(request.POST['link'])

    context = {'page_list': scrape_list, 'form' : form }
    return render(request, 'scrape/app.html', context)


