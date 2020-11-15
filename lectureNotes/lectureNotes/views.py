from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Course, Note, Permission

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method=="POST" and request.POST.get("coursename")!="":
        if len(Course.objects.filter(user=request.user, name=request.POST.get("coursename")))==0:
            Course.objects.create(user=request.user,name=request.POST.get("coursename"))
    courses=Course.objects.filter(user=request.user)
    notes=Permission.objects.filter(user=request.user)
    return render(request,"lectureNotes/index.html",{"courses":courses, "notes":notes})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.GET.get("username")!=None:
        user=authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
        if user!=None:
            login(request=request, user=user)
            return redirect("/")
    return render(request,"lectureNotes/login.html")
    
def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        User.objects.create_user(request.POST.get("username"),"", request.POST.get("password"))
        return redirect("login")
    return render(request,"lectureNotes/signup.html")

def logoutpage(request):
    logout(request)
    return redirect("/")

@csrf_exempt
def newnote(request):
    if request.method=="POST" and request.POST.get("notes")!="":
        course=Course.objects.get(pk=int(request.POST.get("course")))
        date=request.POST.get("date")
        noteText=request.POST.get("notes")
        link=request.POST.get("link")
        Note.objects.create(course=course, date=date, noteText=noteText, link=link)
        return redirect("course/"+request.POST.get("course"))

    courses=Course.objects.filter(user=request.user)
    return render(request,"lectureNotes/newnote.html",{"courses":courses})

def courseview(request, coursekey):
    course=Course.objects.raw("SELECT * FROM lectureNotes_course WHERE id="+str(coursekey)+";")[0]
    notes=Note.objects.raw("SELECT * FROM lectureNotes_note WHERE course_id="+str(coursekey)+" ORDER BY date;")
    users=User.objects.all
    return render(request,"lectureNotes/course.html",{"notes":notes, "course":course, "users":users})

def share(request):
    if request.method=="POST":
        user=User.objects.filter(pk=request.POST.get("userId"))[0]
        note=Note.objects.filter(pk=request.POST.get("noteId"))[0]
        Permission.objects.create(user=user, note=note)

        return redirect("course/"+str(note.course.pk))
    return redirect("/")