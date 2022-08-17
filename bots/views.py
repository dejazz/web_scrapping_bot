from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
import time
import asyncio
from bots.bot import BotScraping


class botView(APIView):
    async def get(self, request):
      
        bot = BotScraping()
        response = asyncio.run(bot.scrapping())
        return Response(response,status.HTTP_200_OK)
   
