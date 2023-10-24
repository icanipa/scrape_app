from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Page, Detail
from .forms import TitleForm
from .tasks import scrape_page


# Create your views here.
@login_required
def index(request):
    form = TitleForm()
    if request.method == 'POST':
        link = request.POST['link']
        form = TitleForm(request.POST)
        if form.is_valid():
            scrape_page(link)
            form = TitleForm()
    scrape_list = Page.objects.annotate(count=Count('detail'))
    context = {'page_list': scrape_list, 'form' : form }
    return render(request, 'scrape/app.html', context)

@login_required
def detail(request, page_id):
    name = get_object_or_404(Page, pk=page_id)
    page = get_list_or_404(Detail, page_id=page_id)
    paginator = Paginator(page, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'page_details': page_obj, 'page_name': name}

    return render(request, 'scrape/detail.html', context)

