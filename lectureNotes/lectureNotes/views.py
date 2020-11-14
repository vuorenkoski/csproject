from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Course, Note, Permission

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method=="POST" and request.POST.get("coursename")!="":
        if len(Course.objects.filter(user=request.user, name=request.POST.get("coursename")))==0:
            Course.objects.create(user=request.user,name=request.POST.get("coursename"))
    courses=Course.objects.filter(user=request.user)
    return render(request,"lectureNotes/index.html",{"courses":courses})

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

def newnote(request):
    if request.method=="POST" and request.POST.get("notes")!="":
        course=Course.objects.get(user=request.user, name=request.POST.get("course"))
        date=request.POST.get("date")
        noteText=request.POST.get("notes")
        link=request.POST.get("link")
        Note.objects.create(course=course, date=date, noteText=noteText, link=link)
        return redirect("/")

    courses=Course.objects.filter(user=request.user)
    return render(request,"lectureNotes/newnote.html",{"courses":courses})

def course(request, coursekey):
    course=Course.objects.get(pk=coursekey)
    notes=Note.objects.filter(course=course)
    users=User.objects.all
    return render(request,"lectureNotes/course.html",{"notes":notes, "course":course, "users":users})

def share(request):
    if request.method=="POST":
        user=User.objects.filter(pk=request.POST.get("userId"))
        note=Note.objects.filter(pk=request.POST.get("noteId"))
    return redirect("/")