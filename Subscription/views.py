from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import stripe
from .models import Customer 

# Create your views here.

stripe.api_key = "sk_test_51IQbkaB33Jmjg5KecX7IZgIl4XLGwAjhr5NktlTNRUSiRTw7NPIljBZFNho761QGGXQDCKiSIGSub5sz4SsYv84200qMxNjAKI"

def plan(request):
    return render(request,'subscription/plan.html')


@login_required(login_url='login')
def checkout(request):

    coupons = {'halloween':31, 'welcome':10}

    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, source=request.POST['stripeToken'])
        plan = 'price_1IQdBTB33Jmjg5KeVnYv7Sat'
        if request.POST['plan'] == 'yearly':
            plan = 'price_1IQdCAB33Jmjg5KeC4nFHnmG'
        if request.POST['coupon'] in coupons:
            percentage = coupons[request.POST['coupon'].lower()]
            try:
                coupon = stripe.Coupon.create(duration='once', id=request.POST['coupon'].lower(),percent_off=percentage)
            except:
                pass
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}], coupon=request.POST['coupon'].lower())
        else:
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}])
        
        customer = Customer()
        customer.user = request.user
        customer.stripeid = stripe_customer.id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = subscription.id
        customer.save()
        
        return redirect('home')
    else:
        plan = "monthly"
        coupon = 'none'
        price = 100
        og_dollar = 10
        coupon_dollar = 0
        final_dollar = 10
        if request.method == "GET" and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 1000
                og_dollar = 100
                final_dollar = 100
        if request.method == "GET" and 'coupon' in request.GET:
            if request.GET['coupon'].lower() in coupons:
                coupon = request.GET['coupon'].lower()
                percentage = coupons[coupon]
                coupon_price = int((percentage/100) * price)
                price = price - coupon_price
                coupon_dollar = str(coupon_price)[:-2] + '.' + str(coupon_price)[-2:]
                final_dollar = str(price)[:-2] + '.' + str(price)[-2:]
        return render(request, 'subscription/checkout.html', {'plan':plan, 'coupon':coupon, 'price':price,
         'og_dollar':og_dollar, 'coupon_dollar':coupon_dollar, 'final_dollar':final_dollar})