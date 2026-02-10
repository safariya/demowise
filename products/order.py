from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order,Order_item,shippingAddress,newletter

def index(request):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/my-order.html')
    orders=Order.objects.filter(customer=request.user.customer)
    context={'orders':orders}
    return render(request,'my-order.html',context)
def vieworder(request,t_no):
    Newletter=newletter.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        form = newletter(email=email)
        form.save()
        messages.info(request,'email sended')
        return redirect('/checkout_view.html')
    order=Order.objects.filter(transaction_id=t_no).filter(customer=request.user.customer).first()
    shipping_address=shippingAddress.objects.filter(order=order).filter(customer=request.user.customer).first()
    orderitems=Order_item.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems,'shipping_address':shipping_address}
    return render(request,'checkout_view.html',context)


