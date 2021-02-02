from django.shortcuts import render
from .models import Course_Details
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .mypaginations import MyPaginations


# Create your views here.

def Index(request):
    course_details = Course_Details.objects.all()
    page = request.GET.get('page')

    all_post = Paginator(course_details, 6)
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except EmptyPage:
        posts = all_post.page(all_post.num_pages)
    # pagination_class = MyPaginations

    d = {
        'course_details': course_details, 'posts': posts
    }
    return render(request, 'core/index.html', d)


#
# def Course_Descriptions(request):
#     course_desc = Course_Details.objects.all()
#     return render(request, 'core/CourseDescriptions.html', {'course_desc': course_desc})


def about(request):
    return render(request, 'core/about.html')


def feedback(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email_id = request.POST['email']
        comments = request.POST['comment']

        send_mail(
            "Bigapple's" + " " + firstname + " " + comments,  # Subject
            comments,  # Message
            email_id,  # From Email
            ['i.m.ashishhh@gmail.com'],  # To Email
        )
        return render(request, 'core/feedback.html', {'firstname': firstname})
    else:
        return render(request, 'core/feedback.html', {})


def search(request):
    query = request.GET.get('query')
    course_details = Course_Details.objects.filter(title__icontains=query)
    params = {'course_details': course_details}
    return render(request, 'core/search.html', params)

# def search1(request):
#     query = request.GET.get('query1')
#     course_details = Course_Details.objects.filter(title__icontains=query1)
#     params = {'course_details': course_details}
#     return render(request, 'core/search1.html', params)
