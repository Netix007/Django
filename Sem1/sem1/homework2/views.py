from django.shortcuts import render, get_list_or_404, get_object_or_404
from homework2.models import Client, Item, Order
from homework2.forms import ItemForms
from django.http import HttpResponse
from datetime import date, timedelta
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

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


def edit_item_by_id(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForms(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data.get('name')
            item.description = form.cleaned_data.get('description')
            item.price = form.cleaned_data.get('price')
            item.count = form.cleaned_data.get('count')
            item.save()
            return HttpResponse(f"Edited item id: {item_id}")

    form = ItemForms(initial={'name': item.name,
                              'description': item.description,
                              'price': item.price,
                              'count': item.count})

    return render(
        request=request,
        template_name='homework2/item_forms.html',
        context={'form': form, 'item_id': item_id, 'item_url': item.picture}
    )


def upload_image(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            obj = fs.save(image.name, image)
            item.picture = fs.url(obj)
            item.save()
            return HttpResponse(f"Add item picture: {item_id}")
    else:
        form = ImageForm()
    return render(request, 'homework2/upload_image.html', {'form': form, 'item_id': item_id})
