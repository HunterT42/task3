from django.views import generic
from .models import Todo
from .forms import TodoForm

class TodoListView(generic.ListView):
    model = Todo
    template_name = 'app/todolist.html'
class TodoCreateView(generic.CreateView):
    form_class = TodoForm
    template_name = 'app/todocreate.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_at = timezone.now()
        instance.updated_at = timezone.now()
        instance.save()
        return super().form_valid(form)

class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = 'app/todoupdate.html'
    form_class = TodoForm

    def form_valid(self, form):
        instance = self.get_object()
        instance.update(form.cleaned_data)
        instance.updated_at = timezone.now()
        instance.save()
        return super().form_valid(form)

class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = 'app/tododelete.html'
    success_url = '/'

    def get_object(self):
        return Todo.objects.get(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super().delete(request, *args, **kwargs)

