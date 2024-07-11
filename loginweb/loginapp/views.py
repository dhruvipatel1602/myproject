from django.shortcuts import render
# Create your views here.
def loginPage(req):
    return render(req,"login.html")

def welPage(req):
    email = req.POST.get('email')
    password = req.POST.get('password')
    if email == 'vagheladharmesh2004@gmail.com' and password == 'Dharmesh2.4':
        return render(req,'welcome.html')
    else:
        print("Eror")