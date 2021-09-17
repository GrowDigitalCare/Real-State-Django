from django.contrib.auth import get_user
from superadmin.models import *

def navbar_category(request):
    category = CategoryModel.objects.all()[:4]
    return {
        'category': category,
        'username':get_user(request)
    }