# Lecture notes -application
Cyber security fall 2020 -project

## Brief desription

Application is used to save notes from lectures and to share these notes with other users. 

User must signup first. After that user can login with credentials given. First, new course entry must be crated. After that user can add new notes to that course. 

User can share notes to other users from noteview. 

## Vulnerabilites

### Broken Authentication
Problem: Notes can be accessed by anybody without login. This can be done by direct web address "../courses/{number}".

Fix: Use Djangos own authentication system, in this case for example by using @login_required in "def course(request, coursekey)" function. This same decorator shoud be placed in in other functions (index, share, newnote).

Problem: There is vulnerability for Cross-site request forgery (CSRF) in newNote function, which can predispose to malicous requests (in this case creation of new notes without users intent).

Fix: {% csrf_token %} should be included in the form in newnote.html and decoration @csrf_exempt should be removed from def newnote(request). 

### Cross-Site Scripting XSS
Problem: malicious user can add javascrip code in note which then shares with other users. When other users view this note, malicious script is executed by users browser.

Fix: Django has built in feature which escapes all strings inserted in html templates. In index.html file where shared notes are diplayed "{{n.noteText|safe}}" should be replaced with this {{n.noteText}} so that this feature is enabled. 

### Sensitive Data Exposure
Problem: Login information is sent to the server by GET method, which means that credentials are not encrypted when sent via internet.

Fix: This can be fixed by using POST method similarly than is done in signup. In that case credentials are better secured if https protocol is used. Even better would be to use the Djangos own authentication system insted of self made login and signup functions.

### Broken Access Control
Problem: Even after fix under the title "Broken Authentication" any logged in user can access other users notes from direct web address "../courses/{number}".

Fix: Before displaying the data function should check that current user is the same ase the user who dreated the course (if course.user==request.user). Actually, same issue is in the functions share and newNote. 

### SQL Injection
Problem: In courseview page malicious user can make sql injection by replacing web address from "../course/2/" to "../course/2or 1=1/" which has the effect that it lists notes from every user. 

Fix: Current raw sql commands with inserting unsanitized parameters predisposes to SQL injection. Django does sanitization if first two lines in courseview function are replaced with this

```
course=Course.objects.get(pk=coursekey)
notes=Note.objects.filter(course=course).order_by("date")
```

