from rest_framework import serializers
from .models import *


class TableSerializer(serializers.ModelSerializer):
    # reserve_table = serializers.SerializerMethodField()
    # free_table = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = ["id", "table_number", "capacity", "is_occupied"]

    # def get_reserve_table(self,obj):
    #     return obj.reserve_table()

    # def get_free_table(self,obj):
    #     return obj.free_table()
    "Excluding reserve_table and free_table Methods: These methods change the state of the object and should not be invoked during serialization. Instead, they should be called in views or viewsets where the business logic resides."


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "item_name", "item_price"]


class OrderSerializer(serializers.ModelSerializer):

    table = TableSerializer()
    item = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("item")
        table_data = validated_data.pop("table")
        table = Table.objects.get(table_number=table_data["table_number"])
        order = Order.objects.create(table=table, **validated_data)

        for item_data in items_data:
            item = Item.objects.get(pk=item_data["id"])
            order.item.add(item)
        order.calculate_total()
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)

        if items_data is not None:
            instance.items.clear()

            for item_data in items_data:
                item = Item.objects.get(id=items_data["id"])
                instance.items.add(item)

            instance.calculate_total()

        return super().update(instance, validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payment
        fields = "__all__"

    # def get_process_payment(self,obj):
    #     return obj.get_process_payment()

    def create(self, validated_data):
        order_data = validated_data.pop("order")
        order = Order.objects.get(id=order_data["id"])
        payment = Payment.objects.create(order=order, **validated_data)
        return payment

    def update(self, instance, validated_data):
        order_data = validated_data.pop("order", None)
        if order_data is not None:
            instance.order = Order.objects.get(id=order_data["id"])
        return super().update(instance, validated_data)


class ManagerSerializer(serializers.ModelSerializer):

    # table = TableSerializer(many=True)

    class Meta:
        model = Manager
        fields = "__all__"

