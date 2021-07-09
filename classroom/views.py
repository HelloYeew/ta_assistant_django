from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from .forms import EditMember, AddStudent
from .models import Class
from database_function.conversion import get_all_class_member, convert_member, create_member_query, convert_to_usable_value
from database_function.home_view import get_available_class_student, get_available_class_ta, get_available_class_teacher, check_status
from database_function.add_remove_member import add_student_to_db


@login_required
def home(request):
    class_as_student = get_available_class_student(request.user.id)
    class_as_ta = get_available_class_ta(request.user.id)
    class_as_teacher = get_available_class_teacher(request.user.id)
    only_student = False
    no_class = False
    if check_status(request.user.id) == 1:
        only_student = True
    elif check_status(request.user.id) == 2:
        no_class = True
    context = {
        'class_as_student': class_as_student,
        'class_as_ta': class_as_ta,
        'class_as_teacher': class_as_teacher,
        'only_student': only_student,
        'no_class': no_class,
        'page_title': 'Classes',
    }
    return render(request, 'classroom/home.html', context)


@login_required
def view_member(request, pk):
    class_detail = get_object_or_404(Class, pk=pk)
    student, ta, teacher = convert_to_usable_value(class_detail)
    context = {
        'page_title': 'Member',
        'class': class_detail,
        'student': student,
        'ta': ta,
        'teacher': teacher,
        'student_number': len(student),
        'ta_number': len(ta),
        'teacher_number': len(teacher),
    }
    return render(request, 'classroom/class_member.html', context)


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.teacher = self.request.user.id
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


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'classroom/class_delete.html'
    success_url = '/'


def add_student(request, pk):
    class_detail = get_object_or_404(Class, pk=pk)
    if request.method == "POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            add_status = add_student_to_db(form['student_list'].value(), class_detail.id)
            if add_status:
                messages.success(request, f'Add student to {class_detail.name} success!')
            else:
                messages.error(request, f"Fail to add student to {class_detail.name}. Please check user ID that you put in add form.")
            return redirect(reverse('class-member', kwargs={'pk': class_detail.id}))
    else:
        form = AddStudent()

    context = {
        'form': form,
        'page_title': 'Add Student'
    }

    return render(request, "classroom/class_addstudent.html", context)