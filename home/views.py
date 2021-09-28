from django.shortcuts import render, redirect
from home.models import Todo,Dev
from home.forms import TodoForm, CForm

# Create your views here.

def home(request):
    todolist = Todo.objects.all()
    dev = Dev.objects.all()
    print(todolist)

    # for i in todolist:
    #     print(i.name)
    #     print(i.des)

    context = {"todolist" : todolist,
                "dev":dev
                }
    return render(request, 'index.html', context)


def tododetails(request, pk):
    # todo= Dev.objects.get(id=pk)
    dev = Dev.objects.get(id=pk)
    context= {"dev":dev}
    return render(request, 'details.html', context)


def CreateTodo(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('/')

    context = {'form':form}
    return render(request, 'create.html', context)

def createForm(request):
    form = CForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('/')

    context = {'form':form}
   
    return render(request, 'form.html', context)

def update(request, id):
    todo = Todo.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()

        return redirect('/')

    context = {'form':form, "todo":todo}
    return render(request, 'update.html', context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')


def fulltime(request):
    fulltime = Dev.objects.filter(Job__name="Full-time")
    print(fulltime)
    context = {'fulltime': fulltime}
    return render(request, 'fulltime.html', context)

def internship(request):
    internship = Dev.objects.filter(Job__name="Internship")
    print(internship)
    context = {'internship': internship}
    return render(request, 'internship.html', context)

def freelance(request):
    freelance = Dev.objects.filter(Job__name="Freelance")
    print(freelance)
    context = {'freelance': freelance}
    return render(request, 'freelance.html', context)

def remote(request):
    remote = Dev.objects.filter(Job__name="Remote")
    print(remote)
    context = {'remote': remote}
    return render(request, 'remote.html', context)

def parttime(request):
    parttime = Dev.objects.filter(Job__name="part-time")
    print(parttime)
    context = {'parttime': parttime}
    return render(request, 'parttime.html', context)



