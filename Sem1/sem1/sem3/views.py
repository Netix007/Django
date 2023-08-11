from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request
from sem3.forms import ChooseGameForm
from django import forms
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


def single_games_form(request):
    coin_sides = ('obverse', 'reverse')
    if request.method == 'POST':
        form = ChooseGameForm(request.POST)
        title = ['Coin play', 'Dice', 'Random number'][int(form.data['a_game'])]
        if form.is_valid():
            if title == 'Coin play':
                attempts_pack = [coin_sides[randint(0, 1)] for _ in range(form.cleaned_data['attempts'])]
            elif title == 'Dice':
                attempts_pack = [randint(1, 6) for _ in range(form.cleaned_data['attempts'])]
            else:
                attempts_pack = [randint(0, 99) for _ in range(form.cleaned_data['attempts'])]
        logger.info(f'Sending results for game {title}')
        return render(request,
                      'sem3/result_game.html',
                        {
                            'title': title,
                            'attempts': attempts_pack
                        })
    else:
        form = ChooseGameForm()
        logger.info(f'Sending game chooser')
        return render(request, 'sem3/choose_game_form.html',
                    {'form': form, 'title': 'Choose Game'
                     })

