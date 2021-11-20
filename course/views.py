from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator
from .filters import CourseFilter
# Create your views here.

def course_list(request):
    course_list = Course.objects.all()

        ## filters 
    myfilter = CourseFilter(request.GET, queryset=course_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 1) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'courses':page_obj, 'myfilter':myfilter }
 
    return render(request, 'course/course_list.html', context)


def course_detail(request, slug):

    course_detail = Course.objects.get(slug= slug)
    
    year = course_detail.when.year
    month = course_detail.when.month
    days = course_detail.when.day
    hours = course_detail.when.hour
    minutes = course_detail.when.minute
    seconds = course_detail.when.second

    context = {'course': course_detail, 'year':year, 'month':month, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds}
    return render(request, 'course/course_detail.html', context)