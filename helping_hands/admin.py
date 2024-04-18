from django.contrib import admin
from .models import (Signin, Login, Donor, Donee, HomePage, AboutPage, WelcomePage, SigninPage, LoginPage,
                     ForgotPasswordPage, DonorPage, DoneePage, PartnershipsPage, BlogsPage, DonateMonthlyPage,
                     HelpingHandsPage, Explore, ExplorePage, req_camp, feedback, RequestCampaignPage, LogoutPage,
                     Donation)

# Register your models here.
admin.site.register(Signin)
admin.site.register(Login)
admin.site.register(Donor)
admin.site.register(Donee)
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(WelcomePage)
admin.site.register(SigninPage)
admin.site.register(LoginPage)
admin.site.register(ForgotPasswordPage)
admin.site.register(DonorPage)
admin.site.register(DoneePage)
admin.site.register(PartnershipsPage)
admin.site.register(BlogsPage)
admin.site.register(DonateMonthlyPage)
admin.site.register(HelpingHandsPage)
admin.site.register(Explore)
admin.site.register(ExplorePage)
admin.site.register(req_camp)
admin.site.register(feedback)
admin.site.register(RequestCampaignPage)
admin.site.register(LogoutPage)
admin.site.register(Donation)
