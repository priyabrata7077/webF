from decimal import Decimal
from email import message
from gettext import npgettext
from http.client import HTTPResponse
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import razorpay
from sklearn.metrics.pairwise import cosine_similarity

from .models import Profile as pf
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ContactForm, FormDataForm, rsvp_orderForm
from django.contrib import messages
from cart.cart import Cart
from .forms import UserProfileForm
from django.utils import timezone
import random
import string
from django.db.models import Max, Min
from django.db.models import Q
import cv2
import numpy as np
from django.shortcuts import render
from .models import Product

def process_image(image):
    try:
        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Failed to decode the image")
        bgr_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return bgr_img
    except Exception as e:
        print("Error processing image:", e)
        return None

def upload_image_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image = process_image(uploaded_image)
        if image is not None:
            all_products = Product.objects.all()
            similar_products = find_similar_products(image, all_products)
            return render(request, 'similar_products.html', {'similar_products': similar_products})
        else:
            return HttpResponse("Error processing the uploaded image")
    return render(request, 'upload_image.html')

def extract_features(image):
    try:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist
    except Exception as e:
        print("Error extracting features:", e)
        return None

def find_similar_products(query_image, all_products, similarity_threshold=0.4):
    query_features = extract_features(query_image)
    if query_features is None:
        return []
    similar_products = []
    for product in all_products:
        product_features = extract_features(cv2.imread(product.image.path))
        if product_features is None:
            continue
        similarity = calculate_similarity(query_features, product_features)
        if similarity >= similarity_threshold:
            similar_products.append(product)
    return similar_products

def calculate_similarity(features1, features2):
    return cosine_similarity([features1], [features2])[0][0]
def about_us(request):
    return render(request, 'aboutus/aboutus.html')
    
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        success = send_mail(
            'Subject',
            f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',
            'from@gmail.com',
            ['allin17077@gmail.com'],
            fail_silently=False,
        )

        if success:
            return HttpResponse('Form submitted successfully')
        else:
            return HttpResponse('Failed to send email')
def collection_view(request):
    # Get the sort_by parameter from the request
    sort_by = request.GET.get('sort_by', 'recommended')

    # Define a queryset based on the sort_by parameter
    if sort_by == 'recommended':
        queryset = Product.objects.all()  # Retrieve all items
    elif sort_by == 'popularity':
        queryset = Product.objects.order_by('-popularity_field')  # Sort by popularity
    elif sort_by == 'rating':
        queryset = Product.objects.order_by('-rating_field')  # Sort by rating
    elif sort_by == 'price':
        queryset = Product.objects.order_by('price_field')  # Sort by price

    # You can also filter the queryset based on other filter parameters here
    # For example, if you have price range filters, styles, themes, etc.

    # Generate a context dictionary with filtered data
    context = {
        'items': queryset,  # Include the filtered queryset in the context
        'selected_sort': sort_by,  # Include the selected sorting option in the context
    }

    return render(request, 'collection/collection.html', context)

def profile_edit(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile/profile_edit.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('profile')
@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)

    for cart_item in cart_items:
        OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
        cart_item.delete()

    return redirect('order_detail', order_id=order.id)  # Redirect to the order detail page
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'profile/order.html', {'order': order})
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})
@login_required(login_url="/users/login")
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    context = {'profile': profile, 'orders': orders}
    #user = User.request
    #profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.user.is_superuser:
        # Redirect to the Django admin panel for superusers
        return redirect('dashboard')
    else:


      return render(request, 'profile/profile.html', context)
def track_order(request, order_id):
    # Retrieve the order and related information
    try:
        order = Order.objects.get(id=order_id)
        order_details = {
            'product_name': order.product_name,
            'order_number': order.order_number,
            'product_image_url': order.image.url,
            # Add other order details as needed
        }
        return JsonResponse(order_details)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
        # Add logic to save the review

    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the authenticated user
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'profile/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'profile/login.html')


def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        User.save()

        # Create associated profile
        profile = pf.objects.create(user=user)

        login(request, user)
        return redirect('login')
    else:
        return render(request, 'profile/signup.html')


def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product)
    return redirect("cart_detail")
    # cart = Cart(request)
    # if request.POST.get('action') == 'post':
        
    #     user_id = request.user.id
    #     carttotal = cart.get_total_price()

    #     # Check if order exists
    #     if Order.objects.filter(order_key=order_key).exists():
    #         pass
    #     else:
    #         order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
    #                             address2='add2', total_paid=carttotal, order_key=order_key)
    #         order_id = order.pk

    #         for item in cart:
    #             OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

    #     response = JsonResponse({'success': 'Return something'})
    #     return response

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    valid_coupon = None
    coupon = None
    Invalid_coupon = None
    if request.method =="GET":
      coupoun_code = request.GET.get('coupoun_code')
      if coupoun_code:
          try:
              coupon = Coupon_Code.sort().object.get(code = 'coupon_code')
              valid_coupon = "Are applicable on current order"
          except:
              Invalid_coupon = "Invalid"
    context = {
        'coupon': coupon,
        'valid_coupon' : valid_coupon,
        'invalid_coupon' : Invalid_coupon,
    }    
    return render(request, 'cart/cart.html', context)
def hello(request):
    Category=sub_category.objects.all()
    Popular = Product.objects.filter(section__name="Popular Invites")
    Print = Product.objects.filter(section__name="Print Invites")
    Invites = Product.objects.filter(section__name="3D Invites")
    logo = Monograms.objects.all()
    testimonial = Testimonial.objects.all()
    context={
        'Category': Category,
        'Popular': Popular,
        'Print' : Print,
        'Invites' : Invites,
        'logo': logo,
        'testimonial': testimonial,
    }
    return render(request, 'main/home.html', context)
def Category(request, slug):
    subcategory = get_object_or_404(sub_category, slug=slug)
    main_categories = main_category.objects.filter(category=subcategory)
    product = Product.objects.all()
    
    
    context = {
        'product': product,
        'subcategory': subcategory,
        'main_categories': main_categories,
    }
    return render(request, 'collection/main_category.html', context)
def main_category_detail(request, sub_category_slug, main_category_slug):
    maincategory = get_object_or_404(main_category, slug=main_category_slug)
    
    # Here, you might want to fetch the main categories related to the specific sub-category or use any other logic based on your requirements
    main_categories = main_category.objects.all()  # This is just an example; adjust based on your requirements
    
    selected_main_categories = request.GET.getlist('main_categories')
    selected_sub_categories = request.GET.getlist('sub_categories')

    products = Product.objects.filter(main_category__in=selected_main_categories, 
                                      sub_category__in=selected_sub_categories)
    
    print(f"Main Category Slug: {main_category_slug}")
    print(f"Sub Category Slug: {sub_category_slug}")

    # Fetch products
    products = Product.objects.filter(main_category__slug=main_category_slug, sub_category__slug=sub_category_slug)

    # Print number of products fetched
    print(f"Number of Products: {products.count()}")

    context = {
        'maincategory': maincategory,
        'Products': products,
        'main_categories': main_categories  # Passing main categories to the template
    }
    return render(request, 'collection/collection.html', context)


def Collection(request, tag=None):
    query = request.GET.get('query')
    products = Product.objects.filter(status='Active')
    selected_cultural_segregations = request.GET.getlist('cultural_segregation')
    if selected_cultural_segregations:
        # Filtering products based on selected cultural segregations
        products = products.filter(cultural_segregation__name__in=selected_cultural_segregations)

    # ... [rest of your existing code]

    # Fetch all distinct cultural segregations to display as filter options
    all_cultural_segregations = CulturalSegregation.objects.all()
    selected_main_categories = request.GET.getlist('main_category')
    if selected_main_categories:
        products = products.filter(main_category__name__in=selected_main_categories)
    

    if query:
        products = products.filter(
            Q(product_name__icontains=query) |
            Q(Description__icontains=query) 
        )

    sort_by = request.GET.get('sort_by', 'recommended')
    if sort_by == 'popularity':
        products = products.order_by('-popularity_field')
    elif sort_by == 'rating':
        products = products.order_by('-rating_field')
    elif sort_by == 'price':
        products = products.order_by('price_field')

    min_price = products.aggregate(Min('price'))
    max_price = products.aggregate(Max('price'))

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        products = products.filter(price__lte=int(FilterPrice))

    selected_tags = request.GET.getlist('tag')
    if selected_tags:
        products = products.filter(Tags__in=selected_tags)

    selected_main_categories = request.GET.getlist('main_categories')
    if selected_main_categories:
        products = products.filter(main_category__name__in=selected_main_categories)

    main_categories = main_category.objects.all()

    context = {
        'SelectedCulturalSegregations': selected_cultural_segregations,
        'AllCulturalSegregations': all_cultural_segregations,
        'min_price': min_price,
        'max_price': max_price,
        'Products': products,
        'FilterPrice': FilterPrice,
        'items': products,  # Consider renaming this variable to avoid confusion
        'selected_sort': sort_by,
        'all_tags': set(tag for product in products for tag in product.get_tags_list()),
        'selected_tags': selected_tags,
        'Category': sub_category.objects.all(),
        'MainCategories': main_categories,
        'SelectedMainCategories': selected_main_categories,
    }

    return render(request, 'Collection/collection.html', context)
def Rsvp(request):
    if request.method == 'POST':
        form = rsvp_orderForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data to the MyModel model
            return redirect('rsvp')  # Redirect to a success page or URL
    else:
        form = rsvp_orderForm()

    return render(request, 'rsvp/rsvp.html', {'form': form})
    
def custom_form(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
              # Save the form data to the database
            return redirect('custom_form')  # Redirect to a success page
    else:
        form = FormDataForm()
    return render(request, 'collection/custom_form.html', {'form': form})



def custom_form_save(request):
    if request.method != "POST":
        return redirect('custom_form')
    else:
        ph = request.POST.get("ph")
        email = request.POST.get("email")
        billing_name = request.POST.get("billing_name")
        gstnumber = request.POST.get("gstnumber")
        billing_address = request.POST.get("billing_address")
        you = request.POST.get("you")
        Name = request.POST.get("Name")
        Instagrame_id = request.POST.get("Instagrame_id")
        fathter_name = request.POST.get("fathter_name")
        mother_name = request.POST.get("mother_name")
        grandfathter_name = request.POST.get("grandfathter_name")
        grandmother_name = request.POST.get("grandmother_name")
        image = request.POST.get("image")
        Spouse = request.POST.get("Spouse")
        SpouseName = request.POST.get("SpouseName")
        SpouseInstagrame_id = request.POST.get("SpouseInstagrame_id")
        Spousefathter_name = request.POST.get("Spousefathter_name")
        Spousemother_name = request.POST.get("Spousemother_name")
        Spousegrandfathter_name = request.POST.get("Spousegrandfathter_name")
        Spousegrandmother_name = request.POST.get("Spousegrandmother_name")
        Spouseimage = request.POST.get("Spouseimage")
        Event_name = request.POST.get("Event_name")
        date_field = request.POST.get("date_field")
        time_field = request.POST.get("time_field")
        venue = request.POST.get("venue")
        Description = request.POST.get("Description")

        try:
            Custome = custome(
                ph=ph, email=email, billing_name=billing_name, gstnumber=gstnumber,
                billing_address=billing_address, you=you, Name=Name, Instagrame_id=Instagrame_id,
                fathter_name=fathter_name, mother_name=mother_name, grandfathter_name=grandfathter_name,
                grandmother_name=grandmother_name, image=image, Spouse=Spouse, SpouseName=SpouseName,
                SpouseInstagrame_id=SpouseInstagrame_id, Spousefathter_name=Spousefathter_name,
                Spousemother_name=Spousemother_name, Spousegrandfathter_name=Spousegrandfathter_name,
                Spousegrandmother_name=Spousegrandmother_name, Spouseimage=Spouseimage,
                Event_name=Event_name, date_field=date_field, time_field=time_field,
                venue=venue, Description=Description
            )
            Custome.save()
            if Custome:
                messages.success(request, "Thanks for submitting this form")
                return redirect('custom_form')
            else:
                messages.error(request, 'Please fill in all required fields.')
                return redirect('custom_form')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('custom_form')
def Services(request):
    Category = sub_category.objects.all()
    context ={
        'Category':Category,
    } 
    return render(request,'services/services.html',context)
def Process(request):
    return render(request,'process/process.html')
def Wedskey(request):
    return render(request,'wedskey/wedskey.html')
def Contact(request):
    # if request.method == 'POST':
    #     # Get form data
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')

    #     # Compose email message
    #     subject = 'Contact Form Submission'
    #     message_body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}'
    #     from_email = settings.EMAIL_HOST_USER  

    #     # Send the email
    #     recipient_list = [settings.EMAIL_HOST_USER]  # Replace with the recipient's email address
    #     send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)

    #     # Redirect after successful submission (you can customize this)
    #     return redirect('success_page')
    return render(request,'form/contact.html')
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Initialize product_type with a default value
    product_type = None
    
    if request.method == 'POST':
        # Retrieve form data
        product_type = request.POST.get('product_type')
        # Other form data retrieval here
        
    # Get the main product type choices (excluding wedding options)
   

    #related_products = product.related_products.all()
    request.session['id'] = product.id
    request.session['product_name'] = product.product_name
    request.session['total_price'] = product.price
    context = {
        #'related_products': related_products,
        'product': product,
        
        'product_type': product_type,
    }
    
    return render(request, 'collection/details.html', context)


@login_required
def Payment(request):
    product_type = request.POST.get('product_type')
    product = Product.objects.all()
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            order.status = 'Paid'
            order.save()
            return render(request, 'collection/payment.html')

    return render(request, 'collection/payment.html',{'product':product, 'product_type':product_type })
@login_required
def order_confirmation_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.orderitem_set.all()  # Retrieve related OrderItems
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})
def Thanks(request):
    if request.method == 'POST':
        payment_option = request.POST.get('payment_option')
        if payment_option == 'COD':
            image = request.POST.get('image')
            product_name = request.POST.get('product_name')
            total_price = Decimal(request.POST.get('price'))
            product_type = request.POST.get('product_type')
            order_number = generate_order_number()

            order = Order(user=request.user, image=image, product_name=product_name, product_type=product_type, total_price=total_price, order_number=order_number, Allocate= request.user)
            order.save()

            context = {
                'product_type': product_type,
                'image': image,
                'product_name': product_name,
                'total_price': total_price,
                
                
            }
            return render(request, 'collection/thank-you.html', context)
        else:
            cart = Cart(request)
            total_price = cart.calculate_total_price()
            product_type = "Default Product Type" 

  
            order_number = generate_order_number()

  
            order = Order(user=request.user, image=image, product_type=product_type, total_price=total_price, order_number=order_number)
            order.save()

            cart.clear()

            return redirect('thanks')
             
        
    return render(request, 'collection/thank-you.html')
def generate_order_number():
    timestamp_str = timezone.now().strftime('%Y%m%d%H%M%S')
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f'ORDER-{timestamp_str}-{random_str}'
def order(request):
    

    # Render the order confirmation page with the order data
    return render(request, 'profile/order.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST('name')
        phone = request.POST('phone')
        email = request.POST('email')
        message = request.POST('message')
        send_mail(
                subject='New Contact Form Submission',
                message=f'name: {name}\nphone: {phone}\nemail: {email}\nmessage: {message}',
                from_email=email,
                recipient_list=['priyabrata7077@gmail.com'], 
            )

        return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'Home', {'form': form})



def Error(request):
    return render(request,'Error/404.html')

@login_required
def process_order(request):
    cart_data = request.session.get('cart', {})
    

    if request.method == 'POST':
        request.session['cart'] = {}

        return redirect('order_success')

    context = {
        'cart_data': cart_data,
        
    }
    return render(request, 'profile/order.html', context)
from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = 'profile/login.html'
    success_url = 'profile' 
def Notification(request):
    notify = notifications.objects.all()
    context = {
        'notify':notify

    }
    stored_messages = request.session.get('messages', [])
    for message in stored_messages:
        messages.add_message(request, message.level, message.message, extra_tags=message.extra_tags)
    return render(request, 'notification/notification.html', context)



def details_view(request):
        context = {}
        return render(request, 'details.html', context)
    
def collection_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    amount_in_paisa = int(product.price * 100)  # Calculate amount in paisa

    # Razorpay client initialization
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create an order in Razorpay
    order_data = {
        'amount': amount_in_paisa,
        'currency': 'INR',
        'payment_capture': '1'
    }
    razorpay_order = client.order.create(data=order_data)
    order_id = razorpay_order['id']

    context = {
        'product': product,
        'amount_in_paisa': amount_in_paisa,
        'razorpay_order_id': order_id,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    }
    return render(request, 'your_template.html', context)