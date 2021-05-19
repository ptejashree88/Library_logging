from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.
logger = logging.getLogger('second')


def home(request):
    logger.debug('Enterd in Book 2')
    logger.info("12454362748")
    logger.warning("No entry")
    logger.error("No execution")
    try:
        l =[24,78,90,7,4,7,9,3,'sg']
        for i in l:
            logger.debug(f"{i}")
    except IndentationError as msg:
        logger.exception(msg)
        return HttpResponse('IndexError')
    return HttpResponse("Hello this is Second book detail ")
    