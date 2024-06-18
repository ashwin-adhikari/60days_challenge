from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from rest_framework import viewsets, status
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    @action(detail=True, methods=["post"])
    def assign_table(self, request, pk=None):
        manager = self.get_object()
        table_id = request.data.get("table_id")
        if table_id:
            table = Table.objects.get(id=table_id)
            manager.assign_table(table)
            return Response({"status": "table assigned"})
        return Response({"status": "table id not provided"}, status=400)

    @action(detail=True, methods=["get"])
    def view_order(self, request, pk=None):
        manager = self.get_object()
        order_id = request.query_params.get("order_id")
        if order_id:
            order = Order.objects.get(id=order_id)
            order_data = OrderSerializer(order).data
            return Response(order_data)
        return Response({"status": "Order id not provided"}, status=400)

    @action(detail=True, methods=["post"])
    def manage_payment(self, request, pk=None):
        manager = self.get_object()
        payment_id = request.data.get("payment_id")
        if payment_id:
            payment = Payment.objects.get(id=payment_id)
            manager.manage_payment(payment)
            return Response({"status": "payment processed"})
        return Response({"ststus": "payment id not provided"}, status=400)


class AuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @api_view(["POST"])
    def login(request):
        return Response()

    @api_view(["POST"])
    def signup(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data["username"])
            user.set_password(request.data["password"])
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": serializer.data},
                content_type="application/json",
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["GET"])
    def test_token(request):
        return Response()
