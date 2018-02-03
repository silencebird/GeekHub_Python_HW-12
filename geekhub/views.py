from django.shortcuts import render
from geekhub.models import Course
from geekhub.models import Student
from geekhub.models import New
from geekhub.forms import PostForm
from django.shortcuts import redirect


def index(request):
    news = New.objects.order_by('date')
    context = {
        'title': 'home',
        'news': news
    }

    return render(request, './geekhub/home/home.html', context)


def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, './geekhub/courses.html', context)


def newstudent(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            course = Course.objects.get(id=request.POST.get('course'))
            if course:
                student.course = course
                student.save()
            return redirect('courses')
    else:
        courses = Course.objects.order_by('name')
        form = PostForm()

        context = {
            'form': form,
            'courses': courses
        }
        return render(request, './geekhub/newstudent.html', context)


