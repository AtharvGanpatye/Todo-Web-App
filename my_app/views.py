from django.shortcuts import render, reverse
from my_app.models import Todo
from django.http import HttpResponseRedirect

def Index(request):
    todos = Todo.objects.all()
    return render(request, 'my_app/index.html', {'todos':todos})

def Add_Item(request):

    if request.method == 'POST':
        item = Todo(content=request.POST.get('content'))
        if item.content != '':
            item.save()
        return HttpResponseRedirect(reverse('index'))

def Delete_Item(request, pk):

    if request.method == 'POST':
        item_to_delete = Todo.objects.get(id=pk)
        item_to_delete.delete()
        return HttpResponseRedirect(reverse('index'))
