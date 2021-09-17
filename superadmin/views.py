from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from superadmin.models import *
from django.shortcuts import (render, HttpResponseRedirect)
from django.contrib.auth import authenticate, get_user,  login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from urllib.parse import quote_plus

# ********************** Login Functions *******************************

class loginPage(View):
    initial = {'key': 'value'}
    template_name = 'dashboard/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Login"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return HttpResponseRedirect('/failed/')


def logoutUser(request):
    logout(request)

    return redirect('login')


class changePassword(View):
    initial = {'key': 'value'}
    template_name = 'dashboard/change_password.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Change Password"})

    def post(self, request, *args, **kwargs):
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(get_user(request))

        if password2 == password1:
            user = authenticate(request, username=get_user(
                request), password=password)
            if user is not None:
                u = User.objects.get(username=get_user(request))
                u.set_password(password1)
                u.save()
                return redirect('login')
            else:
                messages.info(request, 'Password is incorrect')
                return HttpResponse('/failed due to pass incorrect/')
        else:
            messages.info(request, 'Password not matched')
            return HttpResponse('/failed due to pass not match/')


# *************************************************************************


# ********************** Category Functions *******************************

def Category(request):
    template_name = "dashboard/category.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = CategoryModel.objects.all()
            itemsimg = CategoryImgModel.objects.all()
            context = {
                'items': items,
                'itemsimg': itemsimg
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def CategoryAdd(request):
    template_name = "dashboard/category.html"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            images = request.FILES.getlist('image')
            image = images[0]
            images.remove(image)
            items = CategoryModel.objects.create(
                title=request.POST.get('title'),
                image=image
            )
            for img in images:
                cimg = CategoryImgModel.objects.create(
                    category=items,
                    image=img
                )
            return redirect('category')
    else:
        return render(request, 'dashboard/login.html')


def CategoryEdit(request, slug):
    template_name = "dashboard/category.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = CategoryModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('category')
    else:
        return render(request, 'dashboard/login.html')


def CategoryUpdate(request, slug):
    template_name = "dashboard/category.html"
    category = CategoryModel.objects.filter(slug=slug)
    if category:
        data = CategoryModel.objects.get(slug=slug)
        dataimg = CategoryImgModel.objects.filter(category=data)
        image = data.image
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.image = request.FILES.getlist(
                'image')[0] if request.FILES.getlist('image') else image
            data.save()
            if request.FILES.getlist('image'):
                if dataimg:
                    dataimg.delete()
                images = request.FILES.getlist('image')
                images.remove(images[0])
                for img in images:
                    cimg = CategoryImgModel.objects.create(
                        category=data,
                        image=img
                    )
        return redirect('category')


def CategoryDelete(request, slug):
    template_name = "dashboard/category.html"
    if get_user(request).is_authenticated:
        items = CategoryModel.objects.get(slug=slug)
        items.delete()
        return redirect('category')
    else:
        return render(request, 'dashboard/login.html')


# ********************************************************************


# ********************** Project Functions *******************************

def Project(request):
    template_name = "dashboard/project.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ProjectModel.objects.all()
            category = CategoryModel.objects.all()
            itemsimg = ProjectImgModel.objects.all()
            context = {
                'items': items,
                'itemsimg':itemsimg,
                'category': category
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def ProjectAdd(request):
    template_name = "dashboard/project.html"
    if get_user(request).is_authenticated:
        category = CategoryModel.objects.get(slug=request.POST.get('category'))
        if request.method == "POST":
            images = request.FILES.getlist('image')
            image = images[0]
            images.remove(image)

            items = ProjectModel.objects.create(
                title=request.POST.get('title'),
                image=image,
                category=category,
                short_description=request.POST.get('short_description'),
                long_description=request.POST.get('long_description'),
                video_link=request.POST.get('video_link'),
            )
            for img in images:
                cimg = ProjectImgModel.objects.create(
                    project=items,
                    image=img
                )
            return redirect('project')
    else:
        return render(request, 'dashboard/login.html')


def ProjectEdit(request, slug):
    template_name = "dashboard/project.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ProjectModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('project')
    else:
        return render(request, 'dashboard/login.html')


def ProjectUpdate(request, slug):
    template_name = "dashboard/project.html"
    category = CategoryModel.objects.get(id=request.POST.get('category'))
    project = ProjectModel.objects.filter(slug=slug)
    if project:
        data = ProjectModel.objects.get(slug=slug)
        dataimg = ProjectImgModel.objects.filter(project=data)
        image = data.image
        category_id = data.category_id
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.image = request.FILES.getlist(
                'image')[0] if request.FILES.getlist('image') else image
            data.short_description = request.POST.get('short_description')
            data.long_description = request.POST.get('long_description')
            data.video_link = request.POST.get('video_link')
            data.category = category
            data.save()

            if request.FILES.getlist('image'):
                if dataimg:
                    dataimg.delete()
                images = request.FILES.getlist('image')
                images.remove(images[0])
                for img in images:
                    cimg = ProjectImgModel.objects.create(
                        project=data,
                        image=img
                    )
        return redirect('project')

def ProjectDelete(request, slug):
    template_name = "dashboard/project.html"
    if get_user(request).is_authenticated:
        items = ProjectModel.objects.get(slug=slug)
        items.delete()
        return redirect('project')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************


# ********************** Progress Functions *******************************

def Progress(request):
    template_name = "dashboard/progress.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ProgressModel.objects.all()
            project = ProjectModel.objects.all()
            itemsimg = ProgressImgModel.objects.all()
            context = {
                'items': items,
                'itemsimg': itemsimg,
                'project': project
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def ProgressAdd(request):
    template_name = "dashboard/progress.html"
    if get_user(request).is_authenticated:
        project = ProjectModel.objects.get(slug=request.POST.get('project'))
        if request.method == "POST":
            images = request.FILES.getlist('image')
            image = images[0]
            images.remove(image)

            items = ProgressModel.objects.create(
                title=request.POST.get('title'),
                image=image,
                short_description=request.POST.get('short_description'),
                long_description=request.POST.get('long_description'),
                project=project,
                video_link=request.POST.get('video_link'),
            )
            for img in images:
                cimg = ProgressImgModel.objects.create(
                    progress=items,
                    image=img
                )
            return redirect('progress')
    else:
        return render(request, 'dashboard/login.html')


def ProgressEdit(request, slug):
    template_name = "dashboard/progress.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ProgressModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def ProgressUpdate(request, slug):
    template_name = "dashboard/progress.html"
    
    project = ProjectModel.objects.get(id=request.POST.get('project'))
    progress = ProgressModel.objects.filter(slug=slug)
    if progress:
        data = ProgressModel.objects.get(slug=slug)
        dataimg = ProgressImgModel.objects.filter(progress=data)
        image = data.image
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.image = request.FILES.getlist(
                'image')[0] if request.FILES.getlist('image') else image
            data.short_description = request.POST.get('short_description')
            data.long_description = request.POST.get('long_description')
            data.video_link = request.POST.get('video_link')
            data.project = project
            data.save()
            if request.FILES.getlist('image'):
                if dataimg:
                    dataimg.delete()
                images = request.FILES.getlist('image')
                images.remove(images[0])
                for img in images:
                    cimg = ProgressImgModel.objects.create(
                        progress=data,
                        image=img
                    )
        return redirect('progress')

def ProgressDelete(request, slug):
    template_name = "dashboard/progress.html"
    if get_user(request).is_authenticated:
        items = ProgressModel.objects.get(slug=slug)
        items.delete()
        return redirect('progress')
    # return render(request, template_name)
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************

# ********************** Blog Functions *******************************

def BlogView(request):
    template_name = "dashboard/blog.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = BlogModel.objects.all()
            itemsimg = BlogImgModel.objects.all()
            context = {
                'items': items,
                'itemsimg': itemsimg,
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def BlogAdd(request):
    template_name = "dashboard/blog.html"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            images = request.FILES.getlist('image')
            image = images[0]
            images.remove(image)

            items = BlogModel.objects.create(
                title=request.POST.get('title'),
                image=image,
                short_description=request.POST.get('short_description'),
                long_description=request.POST.get('long_description'),
            )
            for img in images:
                cimg = BlogImgModel.objects.create(
                    blog=items,
                    image=img
                )
            return redirect('blogview')
    else:
        return render(request, 'dashboard/login.html')


def BlogEdit(request, slug):
    template_name = "dashboard/blog.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = BlogModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('blogview')
    else:
        return render(request, 'dashboard/login.html')


def BlogUpdate(request, slug):
    template_name = "dashboard/blog.html"
    blog = BlogModel.objects.filter(slug=slug)
    if blog:
        data = BlogModel.objects.get(slug=slug)
        dataimg = BlogImgModel.objects.filter(blog=data)
        image = data.image
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.image = request.FILES.getlist(
                'image')[0] if request.FILES.getlist('image') else image
            data.short_description = request.POST.get('short_description')
            data.long_description = request.POST.get('long_description')
            # data.image = request.FILES.get(
            #     'image') if request.FILES.get('image') else image
            data.save()
            if request.FILES.getlist('image'):
                if dataimg:
                    dataimg.delete()
                images = request.FILES.getlist('image')
                images.remove(images[0])
                for img in images:
                    cimg = BlogImgModel.objects.create(
                        blog=data,
                        image=img
                    )
        return redirect('blogview')

def BlogDelete(request, slug):
    template_name = "dashboard/blog.html"
    if get_user(request).is_authenticated:
        items = BlogModel.objects.get(slug=slug)
        items.delete()
        return redirect('blogview')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************


# ********************** MasterPlan Functions *******************************

def MasterPlan(request):
    template_name = "dashboard/masterplan.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = MasterPlanModel.objects.all()
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def MasterPlanAdd(request):
    template_name = "dashboard/masterplan.html"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = MasterPlanModel.objects.create(
                title=request.POST.get('title'),
                image=request.FILES.get('image'),
                long_description=request.POST.get('long_description'),
            )
            return redirect('masterplan')
    else:
        return render(request, 'dashboard/login.html')


def MasterPlanEdit(request, slug):
    template_name = "dashboard/masterplan.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = MasterPlanModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('masterplan')
    else:
        return render(request, 'dashboard/login.html')


def MasterPlanUpdate(request, slug):
    template_name = "dashboard/masterplan.html"
    masterplan = MasterPlanModel.objects.filter(slug=slug)
    if masterplan:
        data = MasterPlanModel.objects.get(slug=slug)
        image = data.image
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.image = request.FILES.get(
                'image') if request.FILES.get('image') else image
            data.save()
        return redirect('masterplan')

def MasterPlanDelete(request, slug):
    template_name = "dashboard/masterplan.html"
    if get_user(request).is_authenticated:
        items = MasterPlanModel.objects.get(slug=slug)
        items.delete()
        return redirect('masterplan')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************



# ********************** Contact Functions *******************************

def Contact(request):
    template_name = "website/contact.html"
    if request.method == "GET":
        items = ContactModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name, {"data": context})


def ContactInfo(request):
    template_name = "dashboard/contact.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ContactModel.objects.all()
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def ContactAdd(request):
    template_name = "dashboard/"
    if request.method == "POST":
        items = ContactModel.objects.create(
            title=request.POST.get('title'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            short_description=request.POST.get('short_description'),
            message=request.POST.get('message'),
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def ContactEdit(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = ContactModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('contactinfo')
    else:
        return render(request, 'dashboard/login.html')


def ContactUpdate(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = ContactModel.objects.filter(slug=slug).update(
                title=request.POST.get('title'),
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                short_description=request.POST.get('short_description'),
                message=request.POST.get('message'),
            )
            return redirect('contactinfo')
    else:
        return render(request, 'dashboard/login.html')

def ContactDelete(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        items = ContactModel.objects.get(slug=slug)
        items.delete()
        return redirect('contactinfo')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************


# ********************** CallBack Functions *******************************

def Booking(request):
    template_name = "dashboard/booking.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = BookingModel.objects.all()
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def BookingAdd(request):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = BookingModel.objects.create(
                fullname=request.POST.get('fullname'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                property=request.POST.get('property'),
                message=request.POST.get('message'),
            )
            return redirect('home')
    else:
        return render(request, 'dashboard/login.html')

def BookingEdit(request, slug):
    template_name = "dashboard/"
    if request.method == "GET":
        items = BookingModel.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('booking')

def BookingUpdate(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = BookingModel.objects.filter(id=slug).update(
                fullname=request.POST.get('fullname'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                property=request.POST.get('property'),
                message=request.POST.get('message'),
            )
            return redirect('booking')
    else:
        return render(request, 'dashboard/login.html')

def BookingDelete(request, slug):
    template_name = "dashboard/booking.html"
    if get_user(request).is_authenticated:
        items = BookingModel.objects.get(id=slug)
        items.delete()
        return redirect('booking')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************
# ********************** Dashboard Functions *******************************

def Dashboard(request):
    template_name = "dashboard/index.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            category = CategoryModel.objects.count()
            project = ProjectModel.objects.count()
            progress = ProgressModel.objects.count()
            masterplan = MasterPlanModel.objects.count()
            blog = BlogModel.objects.count()
            slider = SliderModel.objects.count()
            review = CustomerReviewModel.objects.count()
            contact = ContactModel.objects.count()
            context = {
                'category': category,
                'project': project,
                'progress': progress,
                'masterplan': masterplan,
                'blog': blog,
                'slider': slider,
                'review': review,
                'contact': contact,
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


# ********************************************************************


# ********************** Slider Functions *******************************

def Slider(request):
    template_name = "dashboard/slider.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = SliderModel.objects.all()
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def SliderAdd(request):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = SliderModel.objects.create(
                title=request.POST.get('title'),
                image=request.FILES.get('image'),
                short_description=request.POST.get('short_description'),
            )
            return redirect('slider')
    else:
        return render(request, 'dashboard/login.html')

def SliderEdit(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = SliderModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('slider')
    else:
        return render(request, 'dashboard/login.html')


def SliderUpdate(request, slug):
    template_name = "dashboard/slider.html"
    slider = SliderModel.objects.filter(slug=slug)
    if slider:
        data = SliderModel.objects.get(slug=slug)
        image = data.image
    if request.method == "POST":
        if data:
            data.title = request.POST.get('title')
            data.short_description = request.POST.get('short_description')
            data.image = request.FILES.get(
                'image') if request.FILES.get('image') else image
            data.save()
        return redirect('slider')

def SliderDelete(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        items = SliderModel.objects.get(slug=slug)
        items.delete()
        return redirect('slider')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************


# ********************** Customer Preview Functions *******************************

def Review(request):
    template_name = "website/review.html"
    if request.method == "GET":
        items = CustomerReviewModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name, {"data": context})


def CustomerReview(request):
    template_name = "dashboard/customerreview.html"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = CustomerReviewModel.objects.all()
            context = {
                'items': items
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'dashboard/login.html')


def CustomerReviewAdd(request):
    template_name = "dashboard/"
    if request.method == "POST":
        items = CustomerReviewModel.objects.create(
            title=request.POST.get('title'),
            message=request.POST.get('message'),
        )
        return redirect('review')

def CustomerReviewEdit(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "GET":
            items = CustomerReviewModel.objects.get(slug=slug)
            context = {
                'items': items
            }
            return redirect('customerreview')
    else:
        return render(request, 'dashboard/login.html')


def CustomerReviewUpdate(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        if request.method == "POST":
            items = CustomerReviewModel.objects.filter(slug=slug).update(
                title=request.POST.get('title'),
                message=request.POST.get('message'),
            )

            return redirect('customerreview')
    else:
        return render(request, 'dashboard/login.html')


def CustomerReviewDelete(request, slug):
    template_name = "dashboard/"
    if get_user(request).is_authenticated:
        items = CustomerReviewModel.objects.get(slug=slug)
        items.delete()
        return redirect('customerreview')
    else:
        return render(request, 'dashboard/login.html')

# ********************************************************************


# ********************** Website Functions *******************************


def Home(request):
    template_name = "website/home.html"
    if request.method == "GET":
        slider = SliderModel.objects.all()
        project = ProjectModel.objects.all()
        projectimg = ProjectImgModel.objects.all()
        progress = ProgressModel.objects.all()
        progressimg = ProgressImgModel.objects.all()
        category = CategoryModel.objects.all()
        categoryimg = CategoryImgModel.objects.all()
        blog = BlogModel.objects.all()
        review = CustomerReviewModel.objects.all()
        context = {
            'slider': slider,
            'category': category,
            'categoryimg': categoryimg,
            'project': project,
            'projectimg': projectimg,
            'progress': progress,
            'progressimg': progressimg,
            'blog': blog,
            'review': review,
        }
        return render(request, template_name, {"data": context})


def About(request):
    template_name = "website/about-us.html"
    if request.method == "GET":
        return render(request, template_name)

def PrivacyPolicy(request):
    template_name = "website/privacy-policy.html"
    if request.method == "GET":
        return render(request, template_name)

def TermsCondition(request):
    template_name = "website/terms-condition.html"
    if request.method == "GET":
        return render(request, template_name)

def Blog(request):
    template_name = "website/blog.html"
    if request.method == "GET":
        items = BlogModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name, {"data": context})


def BlogSingle(request, slug):
    template_name = "website/blog-single.html"
    items = BlogModel.objects.get(slug=slug)
    itemsimg = BlogImgModel.objects.filter(blog=items)
    share_string = quote_plus(items.title)
    share_string_desc = quote_plus(items.short_description)
    print(share_string)
    if request.method == "GET":
        context = {
            'items': items,
            'itemsimg': itemsimg,
            'share_string': share_string,
            'share_string_desc': share_string_desc,
        }
        return render(request, template_name, {"data": context})


def ProgressPage(request):
    template_name = "website/progress.html"
    if request.method == "GET":
        items = ProgressModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name, {"data": context})


def ProgressSingle(request, slug):
    template_name = "website/progress-single.html"
    items = ProgressModel.objects.get(slug=slug)
    itemsimg = ProgressImgModel.objects.filter(progress=items)
    if request.method == "GET":
        context = {
            'items': items,
            'itemsimg': itemsimg,
        }
        return render(request, template_name, {"data": context})


def CategoryDetail(request, slug):
    template_name = "website/category-detail.html"
    items = ProjectModel.objects.filter(category__slug=slug)
    if request.method == "GET":
        context = {
            'items': items,
            'slug': slug
        }
        return render(request, template_name, {"data": context})

def CategorySingle(request, slug):
    template_name = "website/category.html"
    category = CategoryModel.objects.all()
    items = CategoryModel.objects.get(slug=slug)
    itemsimg = CategoryImgModel.objects.filter(category=items)
    if request.method == "GET":
        context = {
            'category': category,
            'items': items,
            'itemsimg': itemsimg,
            'slug': slug
        }
        return render(request, template_name, {"data": context})


def ProjectSingle(request, slug):
    template_name = "website/project-single.html"
    items = ProjectModel.objects.get(slug=slug)
    itemsimg = ProjectImgModel.objects.filter(project=items)
    if request.method == "GET":
        context = {
            'items': items,
            'itemsimg': itemsimg
        }
        return render(request, template_name, {"data": context})

# ********************************************************************
