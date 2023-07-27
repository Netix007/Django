from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html = """
    <h1>Главная страница</h1>
    <p>Это главная страница. Тут надо добавить какое-то описание.</p>
"""


def main_page(request):
    logger.info(f'Main page accessed.')
    return HttpResponse(html)

