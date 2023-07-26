from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def coin(request):
    side = ['avert', 'reverse'][randint(0, 1)]
    logger.info(f'coinplay requested; coin_side: {side}')
    return HttpResponse(f"Coin side: {side}")


def dice(request):
    cube_side = randint(1, 6)
    logger.info(f'diceplay requested; cube_side: {cube_side}')
    return HttpResponse(f"Cube side: {cube_side}")


def random_num(request):
    ran_num = randint(0, 100)
    logger.info(f'random_num requested; answer: {ran_num}')
    return HttpResponse(f"Random number: {ran_num}")
