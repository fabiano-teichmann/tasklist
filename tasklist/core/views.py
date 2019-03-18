from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views import generic
from .models import TaskList


class HomeView(generic.ListView):
    model = TaskList
    template_name = 'list_task.html'


class CreateTaskListView(generic.CreateView):
    model = TaskList
    template_name = 'create_task.html'

    def post(self, request):
        if request.POST:
            form = request.data
            post = self.model.create(title=form['title'], desc=form['desc'], status=form['status'])
            post.save()
            redirect('')
        else:
            return render(request, self.template_name)


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


