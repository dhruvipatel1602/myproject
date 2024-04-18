from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Signin(models.Model):
    Id = models.CharField(primary_key=True, max_length=30)
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=8)
    Tel = models.CharField(max_length=10)
    Pwd = models.CharField(max_length=8)

    def __str__(self):
        return self.Id


class Login(models.Model):
    Id = models.CharField(primary_key=True, max_length=30)
    Pwd = models.CharField(max_length=8)

    def __str__(self):
        return self.Id


class Donor(models.Model):
    Id = models.CharField(primary_key=True, max_length=30, default="")
    Name = models.CharField(max_length=30, default="")
    Email = models.CharField(max_length=8, default="")
    Tel = models.CharField(max_length=10, default="")
    Add = models.CharField(max_length=300, default="")
    element = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.Id


class Explore(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30, default="")
    Name = models.CharField(max_length=30, default="")
    Email = models.CharField(max_length=8, default="")
    Tel = models.CharField(max_length=10, default="")
    Add = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.user_id


class Donee(models.Model):
    Id = models.CharField(primary_key=True, max_length=30, default="")
    name = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=8, default="")
    add = models.CharField(max_length=300, default="")
    tel = models.CharField(max_length=10, default="")
    need = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.Id


class HomePage(models.Model):
    image1 = models.ImageField(upload_to='homepage_images/', blank=True, null=True)
    quote1 = models.TextField(max_length=300, default="")
    title1 = models.TextField(max_length=200, default="")
    about_text1 = models.TextField(max_length=500, default="")
    quote2 = models.TextField(max_length=300, default="")
    image2 = models.ImageField(upload_to='homepage_images/', blank=True, null=True)
    title2 = models.TextField(max_length=200, default="")
    about_text2 = models.TextField(max_length=500, default="")
    image3 = models.ImageField(upload_to='homepage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class AboutPage(models.Model):
    image1 = models.ImageField(upload_to='aboutpage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    about_text1 = models.TextField(max_length=1000, default="")
    title2 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")
    text2 = models.TextField(max_length=100, default="")
    text3 = models.TextField(max_length=100, default="")
    text4 = models.TextField(max_length=100, default="")
    text5 = models.TextField(max_length=100, default="")
    text6 = models.TextField(max_length=100, default="")
    image2 = models.ImageField(upload_to='aboutpage_images/', blank=True, null=True)
    title3 = models.TextField(max_length=200, default="")
    about_text2 = models.TextField(max_length=1000, default="")
    image3 = models.ImageField(upload_to='aboutpage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class WelcomePage(models.Model):
    image1 = models.ImageField(upload_to='welcomepage_images/', blank=True, null=True)

    def __str__(self):
        return f"WelcomePage - Image: {self.image1.name}"


class SigninPage(models.Model):
    image1 = models.ImageField(upload_to='signinpage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")
    text2 = models.TextField(max_length=100, default="")
    text3 = models.TextField(max_length=100, default="")
    text4 = models.TextField(max_length=100, default="")
    text5 = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.title1


class LoginPage(models.Model):
    image1 = models.ImageField(upload_to='loginpage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")
    text2 = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.title1


class ForgotPasswordPage(models.Model):
    image1 = models.ImageField(upload_to='forgotpasswordpage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.title1


class DonorPage(models.Model):
    title1 = models.TextField(max_length=200, default="")
    image1 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    text1 = models.TextField(max_length=1000, default="")
    text2 = models.TextField(max_length=100, default="")
    text3 = models.TextField(max_length=100, default="")
    form_text1 = models.TextField(max_length=100, default="")
    form_text2 = models.TextField(max_length=100, default="")
    form_text3 = models.TextField(max_length=100, default="")
    form_text4 = models.TextField(max_length=100, default="")
    form_text5 = models.TextField(max_length=100, default="")
    form_text6 = models.TextField(max_length=100, default="")
    form_image1 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    form_image2 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    form_image3 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    form_image4 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    form_image5 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    form_text7 = models.TextField(max_length=100, default="")
    text4 = models.TextField(max_length=200, default="")
    image2 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    image2_text1 = models.TextField(max_length=300, default="")
    image2_text2 = models.TextField(max_length=500, default="")
    image3 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    image3_text1 = models.TextField(max_length=300, default="")
    image3_text2 = models.TextField(max_length=500, default="")
    image4 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    image4_text1 = models.TextField(max_length=300, default="")
    image4_text2 = models.TextField(max_length=500, default="")
    image5 = models.ImageField(upload_to='donorpage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class DoneePage(models.Model):
    image1 = models.ImageField(upload_to='doneepage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")
    text2 = models.TextField(max_length=100, default="")
    text3 = models.TextField(max_length=100, default="")
    text4 = models.TextField(max_length=100, default="")
    text5 = models.TextField(max_length=100, default="")
    text6 = models.TextField(max_length=100, default="")
    text7 = models.TextField(max_length=100, default="")
    image2 = models.ImageField(upload_to='doneepage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class PartnershipsPage(models.Model):
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=500, default="")
    image1 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    title2 = models.TextField(max_length=200, default="")
    text2 = models.TextField(max_length=100, default="")
    text3 = models.TextField(max_length=100, default="")
    text4 = models.TextField(max_length=100, default="")
    text5 = models.TextField(max_length=100, default="")
    title3 = models.TextField(max_length=100, default="")
    image2 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    title4 = models.TextField(max_length=100, default="")
    text6 = models.TextField(max_length=500, default="")
    image6 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    title5 = models.TextField(max_length=100, default="")
    text7 = models.TextField(max_length=500, default="")
    text8 = models.TextField(max_length=500, default="")
    image7 = models.ImageField(upload_to='partnershipspage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class BlogsPage(models.Model):
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=500, default="")
    title2 = models.TextField(max_length=200, default="")
    image1 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    title3 = models.TextField(max_length=200, default="")
    text3 = models.TextField(max_length=500, default="")
    image6 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    title4 = models.TextField(max_length=200, default="")
    text4 = models.TextField(max_length=500, default="")
    image7 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='blogspage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class DonateMonthlyPage(models.Model):
    formtitle = models.TextField(max_length=200, default="")
    formtext1 = models.TextField(max_length=100, default="")
    formtext2 = models.TextField(max_length=100, default="")
    formtext3 = models.TextField(max_length=100, default="")
    formtext4 = models.TextField(max_length=100, default="")
    formtext5 = models.TextField(max_length=100, default="")
    formtext6 = models.TextField(max_length=100, default="")
    formtext7 = models.TextField(max_length=100, default="")
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=1000, default="")
    text2 = models.TextField(max_length=500, default="")
    text3 = models.TextField(max_length=500, default="")
    text4 = models.TextField(max_length=500, default="")
    image1 = models.ImageField(upload_to='donatemonthlypage_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='donatemonthlypage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class HelpingHandsPage(models.Model):
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=200, default="")
    text11 = models.TextField(max_length=200, default="")
    text12 = models.TextField(max_length=200, default="")
    image1 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    text2 = models.TextField(max_length=200, default="")
    text21 = models.TextField(max_length=200, default="")
    text22 = models.TextField(max_length=200, default="")
    image2 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    text3 = models.TextField(max_length=200, default="")
    text31 = models.TextField(max_length=200, default="")
    text32 = models.TextField(max_length=200, default="")
    image3 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    text4 = models.TextField(max_length=200, default="")
    text41 = models.TextField(max_length=200, default="")
    text42 = models.TextField(max_length=200, default="")
    image4 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    text5 = models.TextField(max_length=200, default="")
    text51 = models.TextField(max_length=200, default="")
    text52 = models.TextField(max_length=200, default="")
    image5 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='helpinghandspage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title1


class ExplorePage(models.Model):
    title = models.TextField(max_length=200, default="")
    image1 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    disc1 = models.TextField(max_length=300, default="")
    image2 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    title2 = models.TextField(max_length=200, default="")
    disc2 = models.TextField(max_length=300, default="")
    image3 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    title3 = models.TextField(max_length=200, default="")
    disc3 = models.TextField(max_length=300, default="")
    image4 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    title4 = models.TextField(max_length=200, default="")
    disc4 = models.TextField(max_length=300, default="")
    image5 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    title5 = models.TextField(max_length=200, default="")
    disc5 = models.TextField(max_length=300, default="")
    image6 = models.ImageField(upload_to='explorepage_images/', blank=True, null=True)
    copyright_title = models.TextField(max_length=200, default="")
    copyright_info = models.TextField(max_length=300, default="")
    contact = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.title


class req_camp(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30, default="")
    topic = models.CharField(max_length=30, default="")
    reason = models.CharField(max_length=300, default="")
    Tel = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.user_id


class feedback(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30, default="")
    feedback = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.user_id


class RequestCampaignPage(models.Model):
    image1 = models.ImageField(upload_to='requestcampaignpage_images/', blank=True, null=True)
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=500, default="")
    text2 = models.TextField(max_length=500, default="")
    text3 = models.TextField(max_length=500, default="")
    text4 = models.TextField(max_length=500, default="")
    image2 = models.ImageField(upload_to='requestcampaignpage_images/', blank=True, null=True)

    def __str__(self):
        return self.title1


class LogoutPage(models.Model):
    title1 = models.TextField(max_length=200, default="")
    text1 = models.TextField(max_length=100, default="")
    text2 = models.TextField(max_length=100, default="")

    def __str__(self):
        return self.title1


class Donation(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30, default="")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    amount = models.IntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}'s Donation"
