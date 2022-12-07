from django.shortcuts import render

from apps.course.models import Course, CourseDetail


def course_view(request):
    courses = Course.objects.all().order_by('-id')

    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    author = request.GET.get('author')
    date = request.GET.get('date')

    if cat:
        courses = courses.filter(category__title__exact=cat)

    if tag:
        courses = courses.filter(tags__title__exact=tag)

    if author:
        courses = courses.filter(author__account__username__exact=author)

    if date:
        courses = courses.filter(created_at__contains=date)

    context = {
        'posts': courses,
    }

    return render(request, 'courses.html', context)


def course_detail(request, pk):
    courses = CourseDetail.objects.get(id=pk)
    context = {
        'courses': courses
    }
    return render(request, 'course-single.html', context)
