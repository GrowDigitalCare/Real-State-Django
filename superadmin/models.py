from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, EmailField
from django.template.defaultfilters import slugify, truncatechars
from django.urls import resolve
import uuid
import random
from django.urls import reverse



class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/category/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    def get_absolute_url_edit(self):
        return reverse('category-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('category-delete', kwargs={'slug': self.slug})

class CategoryImgModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='categoryimg',null=True)
    image = models.ImageField(upload_to ="static/category/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/project/")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='category',null=True)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    video_link = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_edit', kwargs={'pk': self.pk})

    def get_absolute_url_edit(self):
        return reverse('project-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('project-delete', kwargs={'slug': self.slug})

class ProjectImgModel(models.Model):
    project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,related_name='projectimg',null=True)
    image = models.ImageField(upload_to ="static/project/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ProgressModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/progress/")
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    project = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,related_name='project',null=True)
    video_link = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_edit', kwargs={'pk': self.pk})

    def get_absolute_url_edit(self):
        return reverse('progress-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('progress-delete', kwargs={'slug': self.slug})

class ProgressImgModel(models.Model):
    progress = models.ForeignKey(ProgressModel,on_delete=models.CASCADE,related_name='progressimg',null=True)
    image = models.ImageField(upload_to ="static/progress/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.progress.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/Blog/")
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class BlogImgModel(models.Model):
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name='blogimg',null=True)
    image = models.ImageField(upload_to ="static/blog/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class MasterPlanModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/MasterPlan/")
    long_description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class ContactModel(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    short_description = models.CharField(max_length=500)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class BookingModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    fullname = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    property = models.CharField(max_length=500)
    message = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class SliderModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/Slider/")
    short_description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

class CustomerReviewModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

