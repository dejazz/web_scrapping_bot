from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
import time
import asyncio

from .bot import BotScraping


class botView(APIView):
    def get(self, request):

        bot = BotScraping()
        response = asyncio.run(bot.scraping())

        return Response(response, status.HTTP_200_OK)


class BotViewOnDeep(APIView):
    def get(self, request):

        bot = BotScraping()
        response = asyncio.run(bot.scraping(deep=True))

        return Response(response, status.HTTP_200_OK)
