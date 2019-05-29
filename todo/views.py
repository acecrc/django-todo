from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# ToDoの一覧表示機能
class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5

# ToDoの詳細表示機能
class TodoDetailView(generic.DetailView):
    model = Todo

# ToDoの作成機能
class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

# ToDoの編集機能
class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

# ToDoの削除機能
class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')