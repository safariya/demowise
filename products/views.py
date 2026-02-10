from django.shortcuts import render,redirect
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from  .forms import ProfileForm
from  .forms import CheckoutEditForm
from .forms import AboutForm
from .forms import pendingForm
from .forms import CustomerForm
from .forms import CateForm1
from .forms import CateForm2
from .forms import CateForm3
from .forms import contactForm
from .forms import IndexForm
from .forms import InstaForm
from .forms import LeaveComForm
from .forms import LatestForm
from .forms import saleofForm
from .forms import TeamForm
from .forms import FormProduct
from .models import category
from .models import category_1
from .models import category_2
from .models import sale_of
from .models import instagram
from .models import latest_news
from .models import newletter
from .models import index_collection
from .models import logo
from .models import *
from .models import Product
from .models import Customer
from .models import Order
from .models import Order_item
from .models import shippingAddress
from .models import contact_us_view
from .models import send_comment
from .models import contact_us_message
from .models import leave_comment
from .models import aboutus
from .models import team_members


from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login,logout
def index(request):
    Category=category.objects.all()
    Category_1=category_1.objects.all()
    Category_2=category_2.objects.all()
    Sale_of=sale_of.objects.all()
    Instagram=instagram.objects.all()
    Latest_news=latest_news.objects.all()
    Newletter=newletter.objects.all()
    Index_collection=index_collection.objects.all()
    Logo=logo.objects.all()
    
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        return redirect('/')
    else:
   
        return render(request,'index.html',{'Category':Category,'Category_1':Category_1,'Category_2':Category_2,'Sale_of':Sale_of,'Instagram':Instagram,'Latest_news':Latest_news,'Index_collection':Index_collection
                                            ,'Logo':Logo})
@login_required(login_url='/login.html')
def shop(request):
    Category=category.objects.all()
    Category_1=category_1.objects.all()
    Category_2=category_2.objects.all()
    product=Product.objects.all()
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/shop.html')
    
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_items.all()
        cartItem=order.get_cart_items
    else:
        
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order,'Category':Category,'Category_1':Category_1,'Category_2':Category_2,'product':product}
    return render(request,'shop-details.html',context)
        
def search(request):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/shop.html')
    q=request.GET['q']
    product=Product.objects.filter(name__icontains=q).order_by('-id')
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_items.all()
        cartItem=order.get_cart_items
    else:
        
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order,'product':product}
    return render(request,'search.html',context)
    
def about_us(request):
    about=aboutus.objects.all()
    team_mem=team_members.objects.all()
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/about.html')
    context={'about':about,'team_mem':team_mem}
    return render(request,'about.html',context)

@login_required(login_url='/login.html')
def shopping_cart(request):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/shopping-cart.html')
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_items.all()
        
    else:
        
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order}
    return render(request,'shopping-cart.html',context)
@login_required(login_url='/login.html')
def checkout(request):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/checkout.html')
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_items.all()
        
    else:
        
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
    context={'items':items,'order':order}
    return render(request,'checkout.html',context)
def blog_details(request):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']
        form = send_comment(name=name,email=email,phone=phone,comment=comment)
        form.save()
        messages.info(request,'comment posted')
        return redirect('/blog-details.html')
    blog_comment=leave_comment.objects.all()
    view_comment=send_comment.objects.all()
    context={'blog_comment':blog_comment,'view_comment':view_comment}
    return render(request,'blog-details.html',context)
def blog(request):
    return render(request,'blog.html')
def contact(request):
    contacts=contact_us_view.objects.all()
    
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        form = contact_us_message(name=name,email=email,message=message)
        form.save()
        return redirect('/')
    else:
        context={'contacts':contacts}
        return render(request,'contact.html',context)

def signin(request):
    
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.info(request,'password not matching')
            return redirect('/signin.html')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return redirect('/signin.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already exists')
            return redirect('/signin.html')
        else:
             user=User.objects.create_user(username=username,email=email,password=password1)
             user.save()
             return redirect('/')
             
             
    else:
        return render(request,'signin.html')
  
def login_name(request):
        
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            
            else:
                messages.info(request,'username or password not matching')
                return redirect('login.html')
        else:
            return render(request,'login.html',{})
def navbar(request):
    return render(request,'navbar.html')
def footer(request):
    return render(request,'ecom/footer.html')
def logout_name(request):
    logout(request)
    return redirect('/')
@csrf_exempt
@login_required(login_url='/login.html')
def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action',action)
    print('productId',productId)
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created=Order_item.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity + 1 )
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity - 1 )
    orderItem.save()    
    if orderItem.quantity<= 0:
        orderItem.delete()    

    return JsonResponse('item was added',safe=False)
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        total=data['form']['total']
        order.transaction_id=transaction_id
        if total==order.get_cart_total:
            order.complete=True
        order.save()
        if order.shipping==True:
            shippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
                



            )
    else:
        print('user is not logged in')
    return JsonResponse('payment complete',safe=False)
@login_required(login_url='/login.html')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/login.html')
def checkout_view(request):
    shipping_address=shippingAddress.objects.filter(customer=request.user.customer).first()
    return render(request,'checkout_view.html',{'shipping_address':shipping_address})

@login_required(login_url='/login.html')
def edit_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.customer)
        if form.is_valid():
            form.save()
            username=request.user.username
            messages.success(request,f'{username}, your profile is updated')
            return redirect('/')
    else:
        form=ProfileForm(instance=request.user.customer)
    context={'form':form}
    return render(request,'edit-profile.html',context)
#admin-panel
def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin/admin-index.html')
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_obj=User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request,'account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj=authenticate(username=username,password=password)
            if user_obj and user_obj.is_superuser:
                login(request,user_obj)
                return redirect('admin-index.html')
            messages.info(request,'Invalid password')
            return redirect('/admin')
        return render(request,'adminlogin.html')
    except Exception as e:
        print(e)
@login_required(login_url='admin/adminlogin.html')   
def admin_index(request):
    customercount=Customer.objects.all().count()
    productcount=Product.objects.all().count()
    ordercount=Order.objects.all().count()
    orders=Order.objects.all()
    customer=Customer.objects.all()
    context={
        'customercount':customercount,
        'ordercount':ordercount,
        'productcount':productcount,
        'customer':customer,
    }
    return render(request,'admin/admin-index.html',context)
@login_required(login_url='adminlogin')
def admin_card(request):
    customercount=Customer.objects.all().count()
    productcount=Product.objects.all().count()
    ordercount=Order.objects.all().count()
    orders=Order.objects.all()
    context={
        'customercount':customercount,
        'ordercount':ordercount,
        'productcount':productcount
    }

@login_required(login_url='adminlogin')
def admin_edit_user(request,pk):
    order=Customer.objects.get(id=pk)
    form=CustomerForm(instance=order)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin-index')
    return render(request,'admin/admin_edit_user.html',{'form':form})
@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('admin-index')
@login_required(login_url='adminlogin')
def admin_aboutus(request):
    about=aboutus.objects.all()
    form=AboutForm()
    if request.method=='POST':
        form=AboutForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-about-us')
    
    context={'form':form,'about':about}
    return render(request,'admin/admin-about-us.html',context)
@login_required(login_url='adminlogin')
def admin_aboutus_edit(request,pk):
    about=aboutus.objects.get(id=pk)
    form=AboutForm(instance=about)
    if request.method=='POST':
        form=AboutForm(request.POST,request.FILES,instance=about)
        if form.is_valid():
            form.save()
            return redirect('admin-about-us')
    
    context={'form':form}
    return render(request,'admin/admin-about-us.html',context)
@login_required(login_url='adminlogin')
def admin_category(request):
    cate=category.objects.all()
    cate1=category_1.objects.all()
    cate2=category_2.objects.all()
    context={
        'cate':cate,
        'cate1':cate1,
        'cate2':cate2
    }
    
    return render(request,'admin/admin_category.html',context)
@login_required(login_url='adminlogin')
def admin_category1_edit(request,pk):
    cate=category.objects.all()
    category1=category.objects.get(id=pk)
    form=CateForm1(instance=category1)
    if request.method=='POST':
        form=CateForm1(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_category')
    
    context={'form':form,
             'cate':cate}
    return render(request,'admin/admin_category1.html',context)
@login_required(login_url='adminlogin')
def admin_category2_edit(request,pk):
    cate=category_1.objects.all()
    category1=category_1.objects.get(id=pk)
    form=CateForm2(instance=category1)
    if request.method=='POST':
        form=CateForm2(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_category')
    
    context={'form':form,
             'cate':cate}
    return render(request,'admin/admin_category2.html',context)
@login_required(login_url='adminlogin')
def admin_category3_edit(request,pk):
    cate=category_2.objects.all()
    category1=category_2.objects.get(id=pk)
    form=CateForm3(instance=category1)
    if request.method=='POST':
        form=CateForm3(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_category')
    
    context={'form':form,
             'cate':cate}
    return render(request,'admin/admin_category3.html',context)
@login_required(login_url='adminlogin')
def admin_contact_view(request):
    view=contact_us_view.objects.all()
    context={
        'view':view
    }
    return render(request,'admin/admin-contact-view.html',context)
def admin_contact_view_edit(request,pk):
    category1=contact_us_view.objects.get(id=pk)
    form=contactForm(instance=category1)
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin-contact-view')
    
    context={'form':form,}
    return render(request,'admin/admin_contact_view_edit.html',context)
@login_required(login_url='adminlogin')
def admin_contact_message(request):
    messages=contact_us_message.objects.all()
    context={
        'messages':messages
    }
    return render(request,'admin/admin_contact_message.html',context)
def admin_incollection_view(request):
    items=index_collection.objects.all()
    context={
        'items':items
    }
    return render(request,'admin/admin_incollection_view.html',context)
@login_required(login_url='adminlogin')
def admin_incollection_view_edit(request,pk):
    category1=index_collection.objects.get(id=pk)
    form=IndexForm(instance=category1)
    if request.method=='POST':
        form=IndexForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_incollection_view')
    context={'form':form,}
    return render(request,'admin/admin_incollection_view_edit.html',context)
@login_required(login_url='adminlogin')
def admin_insta_view(request):
    insta=instagram.objects.all()
    context={
        'insta':insta
    }
    return render(request,'admin/admin_insta_view.html',context)
def admin_insta_view_edit(request,pk):
    category1=instagram.objects.get(id=pk)
    form=InstaForm(instance=category1)
    if request.method=='POST':
        form=InstaForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_insta_view')
    context={'form':form,}
    return render(request,'admin/admin_insta_view_edit.html',context)
def admin_latest_view(request):
    latest=latest_news.objects.all()
    context={'latest':latest}
    return render(request,'admin/admin_latest_view.html',context)
def admin_latest_view_edit(request,pk):
    category1=latest_news.objects.get(id=pk)
    form=LatestForm(instance=category1)
    if request.method=='POST':
        form=LatestForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_latest_view')
    context={'form':form,}
    return render(request,'admin/admin_latest_view_edit.html',context)
def admin_leave_comment_view(request):
    leave_comm=leave_comment.objects.all()
    context={
        'leave_comm':leave_comm
    }
    return render(request,'admin/admin_leave_comment_view.html',context)
def admin_leave_comment_edit(request,pk):
    category1=leave_comment.objects.get(id=pk)
    form=LeaveComForm(instance=category1)
    if request.method=='POST':
        form=LeaveComForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_leave_comment_view')
    context={'form':form,}
    return render(request,'admin/admin_leave_comment_edit.html',context)
def admin_newletter(request):
    email=newletter.objects.all()
    return render(request,'admin/admin_newletter.html',{'email':email})
def admin_saleof_view(request):
    sale=sale_of.objects.all()
    context={
        'sale':sale
    }
    return render(request,'admin/admin_saleof_view.html',context)
def admin_saleof_edit(request,pk):
    category1=sale_of.objects.get(id=pk)
    form=saleofForm(instance=category1)
    if request.method=='POST':
        form=saleofForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_saleof_view')
    context={'form':form,}
    return render(request,'admin/admin_saleof_edit.html',context)
def admin_send_comment(request):
    comment=send_comment.objects.all()
    return render(request,'admin/admin_send_comment.html',{'comment':comment})   
def admin_team_view(request):
    team=team_members.objects.all()
    context={
        'team':team
    }
    return render(request,'admin/admin_team_view.html',context)
def admin_team_add(request):
    about=team_members.objects.all()
    form=TeamForm()
    if request.method=='POST':
        form=TeamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_team_view')
    
    context={'form':form,'about':about}
    return render(request,'admin/admin_team_edit.html',context)
def admin_team_edit(request,pk):
    category1=team_members.objects.get(id=pk)
    form=TeamForm(instance=category1)
    if request.method=='POST':
        form=TeamForm(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_team_view')
    context={'form':form,}
    return render(request,'admin/admin_team_edit.html',context)
def delete_team_member(request,pk):
    team=team_members.objects.get(id=pk)
    team.delete()
    return redirect('admin_team_view')

def admin_product_view(request):
    items=Product.objects.all()
    context={
        'items':items
    }
    return render(request,'admin/admin_product_view.html',context)
def admin_product_add(request):
    about=Product.objects.all()
    form=FormProduct()
    if request.method=='POST':
        form=FormProduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_view')
    
    context={'form':form,'about':about}
    return render(request,'admin/admin_product_edit.html',context)
def admin_product_edit(request,pk):
    category1=Product.objects.get(id=pk)
    form=FormProduct(instance=category1)
    if request.method=='POST':
        form=FormProduct(request.POST,request.FILES,instance=category1)
        if form.is_valid():
            form.save()
            return redirect('admin_product_view')
    context={'form':form,}
    return render(request,'admin/admin_product_edit.html',context)

def delete_product(request,pk):
    team=Product.objects.get(id=pk)
    team.delete()
    return redirect('admin_product_view')
def admin_orders(request):
    orders=Order.objects.all()
    context={
        'orders':orders
    }
    return render(request,'admin/admin_orders.html',context)

def admin_orders_edit(request,pk):
    order=Order.objects.get(id=pk)
    form=pendingForm(instance=order)
    if request.method=='POST':
        form=pendingForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_orders')
    return render(request,'admin/admin_orders_edit.html',{'form':form})
def delete_orders(request,pk):
    team=Order.objects.get(id=pk)
    team.delete()
    return redirect('admin_orders')
def admin_order_item(request):
    items=Order_item.objects.all()
    context={
        'items':items
    }
    return render(request,'admin/admin_order_item.html',context)
def delete_order_item(request,pk):
    team=Order_item.objects.get(id=pk)
    team.delete()
    return redirect('admin_order_item')
def admin_shipping(request):
    item=shippingAddress.objects.all()
    context={
        'item':item
    }
    return render(request,'admin/admin_shipping.html',context)
def delete_shipping_address(request,pk):
    team=shippingAddress.objects.get(id=pk)
    team.delete()
    return redirect('admin_shipping')