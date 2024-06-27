from audioop import reverse
import csv
import json
from msilib.schema import ListView
import random
from django.conf import settings
from django.contrib.auth import login,authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from frontend.forms import *
from frontend.models import *
from django.contrib import messages
from datetime import date, datetime
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
from dashboard.models import *
from dashboard.forms import MainCategoryForm
from django.views.decorators.csrf import csrf_exempt
def reset_password(request, token):
    return render(request, 'dashboard/reset-password.html', {'token': token})
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        users = User.objects.filter(username=username)

        if users.exists():
           
            for user in users:
                
                token = "random_generated_token"
                user.set_password(token)
                user.save()

                
                subject = 'Password Reset Request'
                message = f'Click the link to reset your password: http://127.0.0.1:8000/dashboard/reset-password/{token}/'
                from_email = 'allin17077@gmail.com'
                to_email = [user.email]
                send_mail(subject, message, from_email, to_email, fail_silently=False)

            messages.success(request, 'Password reset link sent to your email.')
            return redirect('login')
        else:
            messages.error(request, 'No user with this email address.')
    return render(request, 'dashboard/forgot-password.html')
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def add_event(request):
    event = Event.objects.all()

    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def edit_rsvps(request, id):
    rsvp = get_object_or_404(rsvp_order, id=id)

    context = {
        'rsvp': rsvp,
    }

    if request.method == "POST":
        # Retrieve form data from request.POST
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        event_details = request.POST.get("event_details")
        status = request.POST.get("status")

        # Update the existing Rsvp object with the new data and save it
        rsvp.name = name
        rsvp.email = email
        rsvp.phone = phone
        rsvp.event_details = event_details
        rsvp.status = status
        rsvp.save()

        # Optionally, you can perform additional actions here

        return redirect('rsvps')  # Redirect to a success page or wherever you want
    else:
        return render(request, 'dashboard/edit_rsvplist.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def rsvps(request):
    rsvp= rsvp_order.objects.all()
    return render(request,'dashboard/rsvplist.html',{'rsvp':rsvp})
# Create your views here.
#def Index(request):
    #return render(request, 'dashboard/index.html')
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def rsvp_orders(request):
    users = User.objects.all()
    if request.method == "POST":
        # Extract data from the form
        image = request.POST['image']
        user_id = request.POST['user']  # Assuming 'user' is a valid user ID
        status = request.POST['status']
        product_name = request.POST['product_name']
        order_number = request.POST['order_number']
        total_price = request.POST['total_price']
        product_id = request.POST['product_id']

        # Validate the data if needed (e.g., check if order_number is unique)

        try:
            # Create an Order object and save it to the database
            user = User.objects.get(id=user_id)
            order = Order(
                image=image,
                user=user,
                status=status,
                product_name=product_name,
                order_number=order_number,
                total_price=total_price,
                product_id=product_id
            )
            order.save()

            messages.success(request, "Order has been successfully submitted.")
            return HttpResponseRedirect(reverse('rsvp_order'))
        except Exception as e:
            print(e)  # Print the exception for debugging
            messages.error(request, 'An error occurred while saving the order.')

    # Render the form on GET request or after processing POST request
    return render(request, 'dashboard/rsvp_order.html', {'users':users})
    
def logout_view(request):
    logout(request)
    return redirect('dashboard')

def is_admin(user):
    return user.is_authenticated and user.is_staff
def dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')  # Replace 'panel' with the desired URL after successful login
        else:
            error_message = 'Invalid username or password'
            return render(request, 'dashboard/index.html', {'error_message': error_message})
    else:
        # Check if the user is already authenticated, if yes, redirect to 'panel'
        if request.user.is_authenticated:
            return redirect('panel')  # Replace 'panel' with the desired URL for authenticated users
        else:
            return render(request, 'dashboard/index.html')

def log(request):
    return redirect('dashboard')


def is_admin(user):
    return user.is_authenticated and user.is_superuser



@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Export_to_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="project_statuses.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Templates Name', 'Clients Name', 'Invite Type', 'Starts', 'End', 'Status',  'Deadline'])

    orders = Order.objects.all()  # Fetch your data here

    for order in orders:
        writer.writerow([
            order.order_number,
            order.product_name,
            order.user,
            order.product_type,
            order.order_date.strftime('%d-%m-%Y'),  # Assuming order_date is a datetime field
           order.order_date,
            order.status,
            
            '25-11-2023'  # Hardcoded, replace with actual data if needed
        ])

    return response
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def home(request):
    pending_order = Order.objects.filter(status='Pending')
    orders = Order.objects.all()
    total_orders = orders.count()

    today = date.today()
    today_orders = Order.objects.filter(order_date__date=today).count()
    user = request.user
    user_today_orders = Order.objects.filter(order_date__date=today).values('user').distinct().count()
    pending_order_count = Order.objects.filter(status='Pending').count()
    order = Order.objects.prefetch_related('order_items').all()

    context = {'order': order, 'orders': orders, 'pending_order':pending_order, 'total_orders': total_orders, 'today_orders': today_orders, 'user_today_orders':user_today_orders, 'pending_order_count':pending_order_count}
    return render(request, 'dashboard/main/dashboard.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
@login_required  # Requires user to be logged in
@staff_member_required  # Requires user to be a staff member (adjust this decorator based on your role logic)
def edit_project_status(request, id):
    # Retrieve all users for any related functionalities in the template
    users = User.objects.all()

    # Retrieve the specific Order object based on the id
    order = get_object_or_404(Order, id=id)
    
    if request.method == 'POST':
        # Extract data from the POST request
        phone_number = request.POST.get('phone_number')
        product_name = request.POST.get('product_name')
        date = request.POST.get('date')
        email = request.POST.get('email')

        # Update related fields in User and Order models
        order.user.userprofile.phone_number = phone_number
        order.product_name = product_name
        order.date = date
        order.user.email = email
        
        # Save the updated order
        order.save()

        # Redirect to dashboard:index after successful update
        return redirect('dashboard:index')

    # If the request is GET, render the edit form with the current order and users data
    context = {'order': order, 'users': users}
    return render(request, 'dashboard/edit_project_status.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def project_view_status(request,id):
    try:
        orders = Order.objects.get(id=id)
    except Order.DoesNotExist:
        # Handle case where order does not exist
        return render(request, 'error_page.html')  

    context = {'orders': orders}
    return render(request, 'dashboard/project_view_status.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Project(request):
    orders = Order.objects.all()

    # Extract unique status values from the Order model
    unique_statuses = Order.objects.values_list('status', flat=True).distinct()

    context = {'orders': orders, 'unique_statuses': unique_statuses}
    return render(request, 'dashboard/projectstatus.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Services(request):
    if request.method == 'GET' and 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        if sort_by == 'popularity':
            product = Product.objects.order_by('-popularity')
        elif sort_by == 'newest':
            product = Product.objects.order_by('-created_at')
        else:  # Default to sorting by date
            product = Product.objects.all()
    else:
        # Default to sorting by date if no option selected
        product = Product.objects.all()
    
    product_images = ProductImage.objects.all()
    
    context ={
        'product': product,
        'product_images': product_images
    }
    return render(request, 'dashboard/services.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def delete_monogram(request, id):
    monogram = get_object_or_404(Monograms, pk=id)
    monogram.delete()
    return redirect('monogram')
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Monogram(request):
    monogram=Monograms.objects.all()
    if request.method == 'POST':
       
        logo = request.FILES.get('logo')
        Monograms.objects.create(logo=logo)

        return redirect('monogram')
    context = {'monogram': monogram}
    return render(request, 'dashboard/monogram.html',context)


@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Add_Services(request):
    subcategories = sub_category.objects.all()
    sections = Section.objects.all()
    cultural_segregations = CulturalSegregation.objects.all()  # For ManyToManyField
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        discount = request.POST.get('Discount')
        image = request.FILES.get('image')
        description = request.POST.get('Description')
        model_name = request.POST.get('model_Name')
        tags = request.POST.get('Tags')
        section_id = request.POST.get('section')
        status = request.POST.get('status')
        sub_category_id = request.POST.get('sub_category')
        main_category_id = request.POST.get('main_category')
        cultural_segregation_ids = [int(id) for id in request.POST.getlist('cultural_segregation')]

        try:
            section = Section.objects.get(id=section_id)
            sub_category_instance = sub_category.objects.get(id=sub_category_id)
            main_category_instance = main_category.objects.get(id=main_category_id)

            product = Product(
                product_name=product_name,
                price=price,
                Discount=discount,
                image=image,
                Description=description,
                model_Name=model_name,
                Tags=tags,
                section=section,
                category=sub_category_instance,
                status=status,
                main_category=main_category_instance,
            )
            product.save()
            images = request.FILES.getlist('image')  # 'image' is the name of your input field
            for img in images:
                product_image = ProductImage(product=product, images=img)
                product_image.save()
            product.cultural_segregation.set(cultural_segregation_ids)

            # Adding cultural segregations to the product (ManyToManyField)

            return redirect('Services')  # Ensure 'Services' is correctly defined in your urls.py
        except (Section.DoesNotExist, sub_category.DoesNotExist, CulturalSegregation.DoesNotExist):
            # Handle exception or display appropriate error message
            pass

    context = {
        'subcategories': subcategories,
        'sections': sections,
        'cultural_segregations': cultural_segregations,

    }
    return render(request, 'dashboard/add_services.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Edit_Services(request, slug):
    product = get_object_or_404(Product, slug=slug)
    sections = Section.objects.all()
    subcategories = sub_category.objects.all()
    cultural_segregations = CulturalSegregation.objects.all()
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.price = request.POST.get('price')
        product.Discount = request.POST.get('Discount')
        product.model_Name = request.POST.get('model_Name')
        image = request.FILES.get('image')
        if image:
            product.image = image
        # Extract sub_category_id from the POST data
        sub_category_id = request.POST.get('sub_category')
        sub_category_instance = get_object_or_404(sub_category, id=sub_category_id)  # Assuming you have a SubCategory model

        product.category = sub_category_instance

        product.Tags = request.POST.get('Tags')
        product.Description = request.POST.get('Description')

        section_id = request.POST.get('section')
        section_instance = get_object_or_404(Section, id=section_id)
        product.section = section_instance

        product.status = request.POST.get('status')

        product.save()
        images = request.FILES.getlist('image')  # 'image' is the name of your input field
        for img in images:
            product_image = ProductImage(product=product, images=img)
            product_image.save()

        return redirect('Services')

    context = {
        'cultural_segregations':cultural_segregations,
        'product': product,
        'sections': sections,
        'subcategories': subcategories,
    }

    return render(request, 'dashboard/edit_services.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def fetch_related_main_categories(request, subcategory_id):
    try:
        main_categories = main_category.objects.filter(category_id=subcategory_id).values('id', 'name')
        main_categories_list = list(main_categories)
        return JsonResponse(main_categories_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def delete_services(request, slug):

    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
       
        product.delete()
        return redirect('Services')

    return redirect('Services')



@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Collection(request):
   
    Category = sub_category.objects.all()
    maincategory=main_category.objects.all()
    product=Product.objects.all()
    context ={
        'product':product,
        'Category':Category,
        'maincategory':maincategory,
    }
    return render(request, 'dashboard/collection.html', context)  
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def delete_collection(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'POST':
       
        product.delete()
        return redirect('Services')

    return render(request, 'dashboard/collection.html')  
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Add_Collection(request):
    form = MainCategoryForm()
    main_category_exists = main_category.objects.exists()

    if request.method == 'POST':
        form = MainCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_collection') # Adjust this redirect as needed

    return render(request, 'dashboard/add_collection.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Edit_Collection(request, slug):
    product = get_object_or_404(Product, slug=slug)
    products = sub_category.objects.all()

    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Collection details updated successfully.')
            return redirect('Collection')  # Redirect to the collection list or another appropriate URL
        else:
            print(form.errors)  # Print form errors to the console
            messages.error(request, 'Error updating collection details. Please check the form.')

    else:
        form = CollectionForm(instance=product)

    context = {
        'product': product,
        'products': products,
        'form': form,
    }

    return render(request, 'dashboard/edit_collection.html', context)
def get_events(request):
    events = Event.objects.all()

    events_data = []
    for event in events:
        start_date_iso = event.start_date.isoformat() if event.start_date else None

        events_data.append({
            'title': event.title,
            'start': start_date_iso,
            'color': '#FFC18E ',  
            'textColor': 'black',  
        })

    return JsonResponse(events_data, safe=False)
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Calender(request):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        title = request.POST.get('title')
        start_date_str = request.POST.get('start_date')
        invitation_type = request.POST.get('invitation_type')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            start_date = None

        

        if event_id:  # Update an existing event
            event = get_object_or_404(Event, pk=event_id)
            event.title = title
            event.start_date = start_date
            event.invitation_type = invitation_type
            event.save()
        else:  # Create a new event
            Event.objects.create(
                title=title,
                start_date=start_date,
                invitation_type=invitation_type
            )

        return redirect('calender')

    events = Event.objects.all()
    orders = Order.objects.all()

    events_data = []
    for event in events:
        start_date_iso = event.start_date.isoformat() if event.start_date else None

        # Assuming each event is associated with an order based on order_date
        associated_order = orders.filter(date=event.start_date).first()

        events_data.append({
            'id': event.id,
            'title': event.title,
            'start_date': start_date_iso,
            'invitation_type': event.invitation_type,
            'order_id': associated_order.id if associated_order else None,
            'order_number': associated_order.order_number if associated_order else None,
            'date': associated_order.date.strftime('%Y-%m-%d') if associated_order else None,
            # Add other properties you want to display
        })

    context = {
        'events': events_data,
        'orders': orders,
    }

    return render(request, 'dashboard/calender.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Invoice(request):
    return render(request, 'dashboard/invoice.html')
from django.contrib.auth.decorators import user_passes_test
def is_manager_or_editor(user):
    return user.has_perm('frontend.is_manager') or user.has_perm('frontend.is_editor') or user.is_superuser
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Feedback(request):
    # Your view logic here
    return render(request, 'dashboard/feedback.html')
@user_passes_test(lambda u: u.is_superuser, login_url='log')
def Roles(request):
    userprofiles = role.objects.all()
    context = {
        'userprofiles': userprofiles,
    }
    return render(request, 'dashboard/roles.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def edit_Role(request):
    userprofiles = role.objects.all()
    context = {
        'userprofiles': userprofiles,
    }
    return render(request, 'dashboard/edit_role.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='log')
def toggle_product_status(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Toggle the status
    if product.status == 'Active':
        product.status = 'Inactive'
    else:
        product.status = 'Active'
    
    product.save()
    
    return JsonResponse({'status': product.status})



@user_passes_test(lambda u: u.is_superuser, login_url='log')
def filter_orders(request):
    status = request.GET.get('status')
    if status:
        orders = Order.objects.filter(status=status)
    else:
        orders = Order.objects.all()
    return render(request, 'dashboard/orders_list.html', {'orders': orders})


def project_status(request):
    orders = Order.objects.all()
    unique_statuses = Order.objects.values_list('status', flat=True).distinct()
    return render(request, 'dashboard/project_status.html', {'orders': orders, 'unique_statuses': unique_statuses})

# Example views.py
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Order

def approve_order(request, orderId):  # Ensure parameter name matches URL pattern
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=orderId)
        # Perform approval logic here, such as updating the order status
        order.status = 'Activate'
        order.save()
        return JsonResponse({'message': 'Order approved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def reject_order(request, order_id):
    if request.method == 'POST':
        try:
            order = get_object_or_404(Order, id=order_id)
            data = json.loads(request.body)
            
            
            # Perform rejection logic
            order.status = 'DeActivate'
           
            order.save()

            return JsonResponse({'message': 'Order rejected successfully'}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({'error': f'Order with id {order_id} does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
@csrf_exempt  # Use this decorator for testing purposes; consider securing it properly in production
def send_mail_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        
        try:
            send_mail(
                'Subject of the Email',
                'Body of the email.',
                'allin17077@gmail.com',  # Replace with your email address
                [email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)