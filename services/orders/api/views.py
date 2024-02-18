from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        data = serializer.data
        for i, item in enumerate(data):
            order_id = item['id']
            order_items = Order.objects.get(id=order_id).order_items.all()
            order_item_serializer = OrderItemSerializer(order_items, many=True)
            data[i]['order_items'] = order_item_serializer.data

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        order_data = request.data
        order_items_data = order_data.pop('order_items', [])

        # Create the order
        order_serializer = OrderSerializer(data = order_data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()

        # Create the related order items
        for item_data in order_items_data:
            item_data['order'] = order.id
            order_item_serializer = OrderItemSerializer(data=item_data)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)


