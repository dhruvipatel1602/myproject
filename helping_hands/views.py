from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import (Signin, Login, Donor, Donee, HomePage, AboutPage, WelcomePage, LoginPage, SigninPage,
                     ForgotPasswordPage, DonorPage, DoneePage, PartnershipsPage, BlogsPage, DonateMonthlyPage,
                     HelpingHandsPage, Explore, ExplorePage, req_camp, feedback, RequestCampaignPage, LogoutPage,
                     Donation)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "Please Check Your Inbox Of Your Mail!!"
    success_url = reverse_lazy('helping_hands')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the template_name is 'users/password_reset.html'
        if self.template_name == 'users/password_reset.html':
            forgot_password_page_data = ForgotPasswordPage.objects.first()  # Adjust the query as needed
            context['forgot_password_page_data'] = forgot_password_page_data

        return context


@csrf_exempt
def logoutPage(request):
    if request.method == 'POST':
        user_id = request.POST.get('uid')
        fb = request.POST.get('feedback')

        User7 = get_user_model()
        user7 = User.objects.filter(username=user_id).first()

        if user7 is not None:
            exploreuser3 = feedback(user_id=user_id, feedback=fb)
            exploreuser3.save()

            logout(request)
            return redirect('welcome')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('logoutPage')

    lo_page_data = LogoutPage.objects.first()  # Assuming there's only one instance
    return render(request, 'logout_page.html', {'lo_page_data': lo_page_data})


@csrf_exempt
def welcome(request):
    welcome_page_data = WelcomePage.objects.first()  # Assuming there's only one instance
    return render(request, 'welcome.html', {'welcome_page_data': welcome_page_data})


@csrf_exempt
def home(request):
    home_page_data = HomePage.objects.first()  # Assuming there's only one instance
    return render(request, 'home.html', {'home_page_data': home_page_data})


@csrf_exempt
def aboutus(request):
    about_page_data = AboutPage.objects.first()  # Assuming there's only one instance
    return render(request, 'aboutus.html', {'about_page_data': about_page_data})


@csrf_exempt
def donor(request):
    donor_page_data = DonorPage.objects.first()  # Assuming there's only one instance
    return render(request, 'donor.html', {'donor_page_data': donor_page_data})


@csrf_exempt
def handledonor(request):
    if request.method == "POST":
        uid = request.POST['uid']
        name = request.POST['name']
        mail = request.POST['email']
        tel = request.POST['phone']
        add = request.POST['address']
        dragged_element_id = request.POST.get('image_id')

        User6 = get_user_model()
        user6 = User.objects.filter(username=uid).first()

        if user6 is not None:
            donoruser = Donor(Id=uid, Name=name, Email=mail, Tel=tel, Add=add, element=dragged_element_id)
            donoruser.save()
            return redirect('donor')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('donor')


@csrf_exempt
def donee(request):
    donee_page_data = DoneePage.objects.first()  # Assuming there's only one instance
    return render(request, 'donee.html', {'donee_page_data': donee_page_data})


@csrf_exempt
def handledonee(request):
    if request.method == "POST":
        did = request.POST['did']
        dname = request.POST['dname']
        dmail = request.POST['demail']
        dadd = request.POST['daddress']
        dtel = request.POST['dtel']
        need = request.POST['need']

        User5 = get_user_model()
        user5 = User.objects.filter(username=did).first()

        if user5 is not None:
            doneeuser = Donee(Id=did, name=dname, email=dmail, add=dadd, tel=dtel, need=need)
            doneeuser.save()
            return redirect('donee')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('donee')


@csrf_exempt
def login(request):
    login_page_data = LoginPage.objects.first()  # Assuming there's only one instance
    return render(request, 'login.html', {'login_page_data': login_page_data})


@csrf_exempt
def signin(request):
    signin_page_data = SigninPage.objects.first()  # Assuming there's only one instance
    return render(request, 'signin.html', {'signin_page_data': signin_page_data})


@csrf_exempt
def handleRequest(request):
    if request.method == "POST":
        id1 = request.POST['name']
        name1 = request.POST['name2']
        mail = request.POST['mail']
        tel = request.POST['tel']
        pwd = request.POST['pwd']

        # Validate input data
        if not id1.isdigit():
            messages.error(request, "Your User id should only contain numbers")
        if not name1.isalpha():
            messages.error(request, "Your Name should only contain letters")
        if len(tel) < 10 or not tel.isdigit():
            messages.error(request, "Please Enter Correct Contact Number")
        if len(pwd) < 8:
            messages.error(request, "Your Password should contain at least 8 characters")

        # Check if there are any validation errors
        if messages.get_messages(request):
            return redirect('signin')  # Redirect to 'signin' in case of validation errors

        # Check if the user already exists
        if User.objects.filter(username=id1).exists():
            messages.error(request, "This userid is already taken")
            return redirect('signin')

        myuser = User.objects.create_user(id1, mail, pwd)
        myuser.save()

        signinuser = Signin(Id=id1, Name=name1, Email=mail, Tel=tel, Pwd=pwd)
        signinuser.save()
        return redirect('home')

    return redirect('signin')


@csrf_exempt
def handlelogin(request):
    if request.method == "POST":

        uid = request.POST['name']
        upwd = request.POST['upwd']

        loginuser = Login(Id=uid, Pwd=upwd)
        loginuser.save()

        user = authenticate(username=uid, password=upwd)

        if user is not None:
            login(request)
            return redirect('home')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('login')

    return HttpResponse('404 - Not Found')


@csrf_exempt
def partnerships(request):
    partnerships_page_data = PartnershipsPage.objects.first()  # Assuming there's only one instance
    return render(request, 'partnership.html', {'partnerships_page_data': partnerships_page_data})


@csrf_exempt
def explore(request):
    explore_page_data = ExplorePage.objects.first()  # Assuming there's only one instance
    return render(request, 'explore.html', {'explore_page_data': explore_page_data})


@csrf_exempt
def request1(request):
    rc_page_data = RequestCampaignPage.objects.first()  # Assuming there's only one instance
    return render(request, 'request.html', {'rc_page_data': rc_page_data})


@csrf_exempt
def blogs(request):
    blogs_page_data = BlogsPage.objects.first()  # Assuming there's only one instance
    return render(request, 'blogs.html', {'blogs_page_data': blogs_page_data})


@csrf_exempt
def helping(request):
    hh_page_data = HelpingHandsPage.objects.first()  # Assuming there's only one instance
    return render(request, 'helping.html', {'hh_page_data': hh_page_data})


@csrf_exempt
def donatemonthly(request):
    if request.method == "POST":
        uid = request.POST['uid']
        name = request.POST['name']
        mail = request.POST['email']
        tel = request.POST['tel']
        amt = request.POST['amount']
        msg = request.POST['message']

        User2 = get_user_model()
        user2 = User.objects.filter(username=uid).first()

        if user2 is not None:
            donoruser2 = Donation(user_id=uid, name=name, email=mail, tel=tel, amount=amt, message=msg)
            donoruser2.save()
        else:
            messages.error(request, "Invalid User ID. Please Try Again To Fill The Form!!")
            return redirect('donatemonthly')

    dm_page_data = DonateMonthlyPage.objects.first()
    return render(request, 'donatemonthly.html', {'dm_page_data': dm_page_data})


@csrf_exempt
def handleexplore(request):
    if request.method == "POST":
        uid = request.POST['uid']
        name = request.POST['name']
        mail = request.POST['mail']
        tel = request.POST['contact']
        add = request.POST['address']

        User3 = get_user_model()
        user3 = User.objects.filter(username=uid).first()

        if user3 is not None:
            exploreuser = Explore(user_id=uid, Name=name, Email=mail, Tel=tel, Add=add)
            exploreuser.save()

            return redirect('explore')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('explore')


@csrf_exempt
def handle_camp(request):
    if request.method == "POST":
        uid = request.POST['cid']
        topic = request.POST['topic']
        reason = request.POST['reason']
        tel = request.POST['contact']

        User4 = get_user_model()
        user4 = User.objects.filter(username=uid).first()

        if user4 is not None:
            exploreuser2 = req_camp(user_id=uid, topic=topic, reason=reason, Tel=tel)
            exploreuser2.save()

            return redirect('request1')
        else:
            messages.error(request, "Please Check Your ID Again!!")
            return redirect('request1')
