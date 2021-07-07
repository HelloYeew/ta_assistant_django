from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView
)
from .forms import EditMember
from .models import Class
from database_function.conversion import get_all_class_member,convert_member


@login_required
def home(request):
    context = {
        'class_list': Class.objects.all(),
        'page_title': 'Classes'
    }
    return render(request, 'classroom/home.html', context)


def view_member(request, pk):
    class_detail = get_object_or_404(Class, pk=pk)
    context = {
        'page_title': 'Member',
        'class': class_detail,
        'student':  get_all_class_member(convert_member(class_detail.student)),
        'ta':  get_all_class_member(convert_member(class_detail.ta)),
        'teacher':  get_all_class_member(convert_member(class_detail.teacher)),
    }
    return render(request, 'classroom/class_member.html', context)


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassDetailView(DetailView):
    model = Class


class ClassUpdateMember(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    template_name = 'classroom/class_editmember.html'
    fields = ['student', 'ta', 'teacher']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
