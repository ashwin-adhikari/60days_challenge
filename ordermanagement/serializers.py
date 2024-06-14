from rest_framework import serializers
from .models import Table, Order, Payment, Item, Manager

class TableSerializer(serializers.ModelSerializer):
    reservetable = serializers.SerializerMethodField()
    freetable = serializers.SerializerMethodField()
    
    class Meta:
        model = Table
        fields = ['table_number','capacity','is_occupied']


    def reserve_table(self,obj):
        return obj.reserve_table()
    
    def free_table(self,obj):
        return obj.free_table()


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name','item_price']
    

class OrderSerializer(serializers.ModelSerializer):
    
    table = TableSerializer()
    items = ItemSerializer(source='item_name', many=True)

    class Meta:
        model = Order
        fields = ['table','items','total_amount','status']
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create()
        for item_data in items_data:
            item = Item.objects.get(pk=item_data['id'])
            order.add_item(item)
        return order



class PaymentSerializer(serializers.ModelSerializer):
    processpayment = serializers.SerializerMethodField(method_name='process_payment')
    order = OrderSerializer()
    class Meta:
        model = Payment
        fields = ['order','payment_choices','payment_method','payment_status','amount_paid']

    def process_payment(self,obj):
        payment_status = 'Done'
        return obj.process_payment(payment_status)
    

class ManagerSerializer(serializers.ModelSerializer):
    assigntable = serializers.SerializerMethodField()
    vieworder = serializers.SerializerMethodField()
    managepayment = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ['name']
    
    # def assign_table(self,obj):
    #     order = 
    
    
    






    