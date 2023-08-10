from django.shortcuts import render, get_list_or_404
from homework2.models import Client, Item, Order
from datetime import date, timedelta
import logging

logger = logging.getLogger(__name__)


def get_items_by_client(request, client_id):
    orders = get_list_or_404(Order, customer=client_id)
    all_items = {}
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in all_items:
                all_items[product] = order.date_ordered.date()

    context = {
        'title': 'Заказанные товары',
        'client': client_id,
        'time': [date.today() - timedelta(7),
                 date.today() - timedelta(30),
                 date.today() - timedelta(365)
                 ],
        'products': all_items
    }

    logger.info(
        f"Access to all items page from {request.META.get('REMOTE_ADDR')}, "
        f"user agent: {request.META.get('HTTP_USER_AGENT')}"
    )

    return render(request, template_name='homework2/items.html', context=context)
