from django.shortcuts import render, get_object_or_404, redirect
from .models import Table, Order, Payment, Item, Manager
from django.http import HttpResponse

# Create your views here.
def table_list(request):
    tables= Table.objects.all()
    return render (request, 'restaurant/table_list.html', {'tables':tables})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'restaurant/order_details.html', {'order':order})

def create_order(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        order = Order.objects.create(table=table)
        table.occupy_table()
        return redirect('order_detail',order_id=order.id)
    return render(request,'restaurant/create_order.html',{'table':table})

def add_item_to_order(request,order_id,item_id):
    order = get_object_or_404(Order, id=order_id)
    item = get_object_or_404(Item, id=item_id)
    order.add_item(item)
    return redirect('order_detail', order_id=order.id)

def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        amount_paid = order.total_amount
        payment_method= request.POST.get('payment_method')
        payment = Payment.objects.create(order=order, amount_paid=amount_paid, payment_method=payment_method)
        payment.process_payment()
        order.order_status = 'Completed'
        order.save()
        order.table.free_table()
        return redirect('order_detail', order_id= order.id)
    return render(request,'restaurant/process_payment.html',{'order':order})

def homepage(request):
    return render(request,'restaurant/homepage.html')


    