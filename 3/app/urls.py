from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('new/', views.TodoCreateView.as_view(), name='todo-create'),
    path('<pk>/edit/', views.TodoUpdateView.as_view(), name='todo-edit'),
    path('<pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
]
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
