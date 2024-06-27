from audioop import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import CharField
from django.shortcuts import render
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import models
import phonenumbers
# Create your models here.

#customize form
class Testimonial(models.Model):
    text = models.CharField(max_length=400)
    name = models.CharField(max_length=30)
    def __str__(self):
      return self.name
    
class custome(models.Model):
    ph = models.CharField(max_length=50)
    email= models.EmailField()
    billing_name = models.CharField(max_length=50)
    gstnumber =models.CharField(max_length=20)
    billing_address = models.CharField(max_length=200)
    you = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Instagrame_id = models.CharField(max_length=50)
    fathter_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    grandfathter_name = models.CharField(max_length=50)
    grandmother_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    Spouse = models.CharField(max_length=50)
    SpouseName = models.CharField(max_length=50)
    SpouseInstagrame_id = models.CharField(max_length=50)
    Spousefathter_name = models.CharField(max_length=50)
    Spousemother_name = models.CharField(max_length=50)
    Spousegrandfathter_name = models.CharField(max_length=50)
    Spousegrandmother_name = models.CharField(max_length=50)
    Spouseimage = models.ImageField(upload_to='images/')
    Event_name = models.CharField(max_length=50)
    date_field = models.DateField()
    time_field = models.TimeField()
    venue = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    def __str__(self):
        return self.email
    
class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
class Status(models.Model):
    STATUS_CHOICES = (
        ('Activate', 'Activate'),
        ('DeActivate', 'DeActivate'),
        ('Pending', 'Pending'),
        ('Working', 'Working'),
       
    )
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES)
class rsvp_order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_details = models.TextField()
    STATUS_CHOICES = (
        ('Activate', 'Activate'),
        ('DeActivate', 'DeActivate'),
        ('Pending', 'Pending'),
        ('Working', 'Working'),
       
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name    
class Order(models.Model):
    STATUS_CHOICES = (
        ('Activate', 'Activate'),
        ('DeActivate', 'DeActivate'),
        ('Pending', 'Pending'),
        ('Working', 'Working'),
       
    )
    # product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/products/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Activate')
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=100, unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    Allocate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allocations',blank=True) 
    product_id = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return f"Order {self.order_number} by {self.product_name}"   
#customize end
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('protected')
        else:
            return render(request, 'profile/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'profile/login.html')

@login_required
def protected_page(request):
    return render(request, 'protected.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def purchase(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        # Process the purchase logic here

        return render(request, 'payment.html', {
            'product_name': product_name,
            'product_price': product_price
        })
class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.CharField(max_length=5,null=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.user.username
class Monograms(models.Model):
    logo = models.ImageField(upload_to='static/assets/logo', blank=True, null=True)
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
class Checkout(models.Model):
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    zip = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.fname
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images')
    
class category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='static/assets/path', blank=True, null=True)
    
    def __str__(self):
        return self.name
class sup_category(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("supcategory", kwargs={'slug': self.slug})    

    
class main_category(models.Model):
    category = models.ForeignKey('sub_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('maincategory_detail', kwargs={'sub_category_slug': self.category.slug, 'main_category_slug': self.slug})



class sub_category(models.Model):
    name = models.CharField(max_length=255)
    banner = models.FileField(upload_to="static/assets/path",blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Category", kwargs={'slug': self.slug})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/assets/user')
    #role = models.ForeignKey('dashboard.role', on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        try:
            # Normalize and validate phone number
            parsed_number = phonenumbers.parse(self.phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid phone number")
            self.phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError("Invalid phone number")

        super(UserProfile, self).save(*args, **kwargs)
def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = sub_category.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    pre_save.connect(pre_save_post_receiver, sub_category)
class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class ProductType(models.Model):
    TYPE_CHOICES = (
        ('cast', 'Cast'),
        ('wedding', 'Wedding'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.get_type_display()

class WeddingType(models.Model):
    WEDDING_CHOICES = (
        ('love_story', 'Love Story'),
        ('event_base', 'Event Base'),
        ('others', 'Others'),
    )
    wedding_type = models.CharField(max_length=20, choices=WEDDING_CHOICES)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, limit_choices_to={'type': 'wedding'})

    def __str__(self):
        return self.get_wedding_type_display()
class Duration(models.Model):
    DURATION_CHOICES = (
        ('15s', '15 seconds'),
        ('20s', '20 seconds'),
        ('30s', '30 seconds'),
        ('40s', '40 seconds'),
        ('1m', '1 minute'),
        ('1.5m', '1.5 minutes'),
        ('above', 'Above 1.5 minutes'),
    )
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
class Format(models.Model):
    FORMAT_CHOICES = (
        ('MP4', 'Mp4'),
        ('GIF', 'Gif'),
    )
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Other fields and methods

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey('frontend.Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
class CulturalSegregation(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')
    images = models.ImageField(upload_to='static/products/')  
    
class Product(models.Model):
    image = models.ImageField(upload_to='static/products/')
    product_name = models.CharField(max_length=100)
    cultural_segregation = models.ManyToManyField(CulturalSegregation)
    Description = RichTextField()
    category = models.ForeignKey(sub_category,on_delete=models.CASCADE)
    main_category = models.ForeignKey(main_category,on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    price = models.IntegerField()
    Discount = models.IntegerField()
    model_Name = models.CharField(max_length=100)
    Tags = models.CharField(max_length=100)
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    
    def get_tags_list(self):
        return self.Tags.split(',')
    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "ecom_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    pre_save.connect(pre_save_post_receiver, Product)
pre_save.connect(pre_save_post_receiver, Product)
class Coupon_Code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()
    
    def __str__(self):
        return self.code
   
class style(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='style')   
    name = models.CharField(max_length=10)
class size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')
    Num = models.CharField(max_length=10)  
    def __str__(self):
        return self.Num
class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
class notifications(models.Model):
    header = models.CharField(max_length=100)
    paragraph =  models.CharField(max_length=100)
