from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render   # Added for this stepfrom helpfor9_hse_ru import def_calculator as calc

def index(request):
    now = datetime.now()

    return render(
        request,
        "helpfor9_hse_ru/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "helpfor9.hse.ru",
            'message' : "Денис Сергеич, добрый день!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def calendar(request):
    return render(
        request,
        "helpfor9_hse_ru/index.html",
        {
            'title' : "Календарь событий",
            'message' : "Денис Сергеич, здесь будет календарь событий для девятиклассников."
        }
    )

def calculator(request):
    return render(
        request,
        "helpfor9_hse_ru/calculator.html",
        {
            'title' : "Калькулятор среднего балла",
        }
    )

def calc_results(request):

    val1 = request.GET['bal1']
    val2 = request.GET['bal2']
    val3 = request.GET['bal3']
    val4 = request.GET['bal4']
    val1 = float(val1)
    val2 = float(val2)
    val3 = float(val3)
    val4 = float(val4)
    res = (val1 + val2 + val3 + val4) / 4
    
    return render(
        request,
        "helpfor9_hse_ru/calc_results.html",
        {
            'result': res
            }
        )

def info(request):
    return render(
        request,
        "helpfor9_hse_ru/index.html",
        {
            'title' : "Информация о направлениях",
            'message' : "Денис Сергеич, здесь будет информация о направлениях для девятиклассников."
        }
    )

def faculties(request):
    return render(
        request,
        "helpfor9_hse_ru/index.html",
        {
            'title' : "Список факультативов",
            'message' : "Денис Сергеич, здесь будет список факультативов для девятиклассников."
        }
    )

