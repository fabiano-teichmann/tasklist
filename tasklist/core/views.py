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
        redirect('home')


class EditTaskListView(generic.UpdateView):
    model = TaskList
    template_name = 'create_task.html'

    def post(self, request, slug):
        if request.POST:
            post = self.model.objects.get(id=slug)
            form = request.data
            post.title = form['title']
            post.desc = form['desc']
            post.status = form['status']
            post.update_at = datetime.now()
            post.save()
            redirect('')
        else:
            return render(request, self.template_name)


class DeleteTaskListView(generic.DeleteView):
    model = TaskList
    template_name = 'delete_task.html'

    def get(self, request, slug):
        post = self.model.objects.get(id=slug).delete()
        redirect('')


