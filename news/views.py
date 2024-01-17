from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Girls
from .forms import GirlAddForm


def home(request):
    girls = Girls.objects.all()
    context = {
        "girls": girls
    }
    return render(request, "girls.html", context)


def girl_biography(request, girl_id):
    girl = get_object_or_404(Girls, id=girl_id)
    context = {
        "girl": girl
    }
    return render(request, "girl_biography.html", context)


class GirlAddView(View):
    template = "girl_add.html"

    def get(self, request):
        form = GirlAddForm()
        context = {
            'form': form
        }
        return render(request, self.template, context)

    def post(self, request):
        form = GirlAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template, context)


class GirlUpdateView(View):
    template = "girl_update.html"

    def get(self, request, girl_id):
        girl = Girls.objects.get(id=girl_id)
        form = GirlAddForm(instance=girl)
        context = {
            'girl': girl,
            'form': form
        }
        return render(request, self.template, context)

    def post(self, reqeust, girl_id):
        girl = Girls.objects.get(id=girl_id)
        form = GirlAddForm(reqeust.POST, instance=girl)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {
            'girl': girl,
            'form': form
        }
        return render(reqeust, self.template, context)


def girl_delete(request, girl_id):
    girl = Girls.objects.get(id=girl_id)
    girl.delete()
    return redirect('home')
