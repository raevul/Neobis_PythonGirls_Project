from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import News
from .forms import NewCreateForm


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


class NewCreateView(View):
    template = "create_new.html"

    def get(self, request):
        form = NewCreateForm()
        context = {
            'form': form
        }
        return render(request, self.template, context)

    def post(self, request):
        form = NewCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template, context)


class NewUpdateView(View):
    template = "update_new.html"

    def get(self, request, new_id):
        new = News.objects.get(id=new_id)
        form = NewCreateForm(instance=new)
        context = {
            'new': new,
            'form': form
        }
        return render(request, self.template, context)

    def post(self, reqeust, new_id):
        new = News.objects.get(id=new_id)
        form = NewCreateForm(reqeust.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {
            'new': new,
            'form': form
        }
        return render(reqeust, self.template, context)


class NewDeleteView(View):
    ...
