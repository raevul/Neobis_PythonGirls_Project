from django.shortcuts import render, get_object_or_404, redirect

from .models import News
from .forms import NewsCreateForm


def home(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, "news.html", context)


def new_detail(request, new_id):
    new = get_object_or_404(News, id=new_id)
    context = {
        "new": new
    }
    return render(request, "new_detail.html", context)


def create_new(request):
    if request.method == 'POST':
        form = NewsCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_detail')
    else:
        form = NewsCreateForm()
    return render(request, "create_new.html", {'form': form})
