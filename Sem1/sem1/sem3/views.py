from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from random import randint
import logging

logger = logging.getLogger(__name__)


def coin(request, count):

    context = {'title': 'Монетка', 'attempts': [['avert', 'reverse'][randint(0, 1)] for _ in range(count)]}

    logger.info(
        f"Access to main page from {request.META.get('REMOTE_ADDR')}, user agent: {request.META.get('HTTP_USER_AGENT')}"
    )
    return render(request, template_name='sem3/coin.html', context=context)


def dice(request, count):

    context = {'title': 'Кубик', 'attempts': [randint(1, 6) for _ in range(count)]}

    logger.info(
        f"Access to main page from {request.META.get('REMOTE_ADDR')}, user agent: {request.META.get('HTTP_USER_AGENT')}"
    )
    return render(request, template_name='sem3/dice.html', context=context)


def ran_num(request, count):

    context = {'title': 'Случайное число', 'attempts': [randint(0, 100) for _ in range(count)]}

    logger.info(
        f"Access to main page from {request.META.get('REMOTE_ADDR')}, user agent: {request.META.get('HTTP_USER_AGENT')}"
    )
    return render(request, template_name='sem3/ran_num.html', context=context)