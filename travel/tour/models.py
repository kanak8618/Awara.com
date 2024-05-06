from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.utils.html import format_html
from colorfield.fields import ColorField
from django.db.models.signals import pre_save

# Create your models here.

class Hero_Slider(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    bg_image = models.ImageField(upload_to='media/hero_slider', null=True)

    def __str__(self):
        return self.title

class Hero_Featurs(models.Model):
    title = models.CharField(max_length=50, null=True)
    icon_class = models.CharField(max_length=100, null=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    link = models.CharField(max_length=100, null=True, blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title

class Tour_Ctgry(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    def get_all_category(self):
        return  Tour_Ctgry.objects.all().order_by('id')

class Package(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('Hot deals', 'Hot deals'),
    )
    title = models.CharField(max_length=100,null=True)
    description = CKEditor5Field('Text', config_name='extends')
    short_desc = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Tour_Ctgry, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, null=True)
    discount = models.IntegerField(default=0, null=True)
    featured_video = models.CharField(max_length=100,null=True)
    feature_image = models.ImageField(upload_to='media/pkg_feature', null=True)
    bg_image = models.ImageField(upload_to='media/pkg_bg', null=True)
    status = models.CharField(choices=STATUS, max_length=50, null=True)
    starting_date = models.DateField(null=True)
    duration = models.CharField(max_length=50, null=True)
    deadline = models.DateField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("package_detail", kwargs={'slug': self.slug})
    @staticmethod
    def get_all_package():
        return Package.objects.all()
    @staticmethod
    def get_package_by_category_id(category_id):
        if category_id:
            return Package.objects.filter(category = category_id)
        else:
            return Package.get_all_package()
    @staticmethod
    def get_package_by_price(FilterPrice):
        if FilterPrice:
            Int_FilterPrice = int(FilterPrice)
            return Package.objects.filter(price__lte=Int_FilterPrice)
        else:
            return Package.get_all_package()

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Package.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Package)

class Package_Slider(models.Model):
    bg_img = models.ImageField(upload_to='media/pkg_slider', null=True)
    title = models.CharField(max_length=50, null=True)
    short_desc = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.title
class Place(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name +" - "+ self.package.title

class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    Sub_title = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=100, null=True, blank=True)
    time_duration = models.CharField(max_length=50, null=True, blank=True)
    preview = models.BooleanField(default=False)

class Service(models.Model):
    title = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=100, null=True, blank=True)
    icon_class = models.CharField(max_length=100)
    icon_colour = ColorField(default='#FF0000', null=True, blank=True)
    bgPattern_colour = ColorField(default='#FF0000', null=True, blank=True)
    link = models.CharField(default='', max_length=100, null=True, blank=True)
    Description = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.title
