from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views import generic

from .forms import TaskListForm
from .models import TaskList


class HomeView(generic.ListView):
    def get(self, request):
        context = TaskList.objects.all()
        return render(request, 'home.html', {'context': context})


class CreateTaskListView(generic.CreateView):
    model = TaskList
    template_name = 'task.html'
    form_class = TaskListForm

    def get(self, request):
        form = TaskListForm
        return render(request, 'task.html', {'form': form})

    def form_valid(self, form):
        post = form.save(commit=False)
        post.update_at = datetime.now()
        post.save()
        return redirect('home')


class EditTaskListView(generic.UpdateView):
    model = TaskList
    form_class = TaskListForm
    template_name = 'task.html'
    slug_field = 'id'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.update_at = datetime.now()
        post.save()
        return redirect('home')


class DeleteTaskListView(generic.DeleteView):
    model = TaskList
    template_name = 'delete_task.html'
    slug_field = 'id'

    def get(self, request, slug):
        post = self.model.objects.get(id=slug).delete()
        return redirect('home')


