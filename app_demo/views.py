from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.db import connections
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')
    # return render(request, 'login.html')


def get_analyse_demo(request):
    create_date_lst = []
    recharge_user_num_lst = []
    recharge_amount_num_lst = []

    with connections['default'].cursor() as cursor:
        cursor.execute("select create_date,recharge_user_num,recharge_amount_num from app_demo_dayrechargeuseramount")
        res = cursor.fetchall()

        for line in res:
            create_date, recharge_user_num, recharge_amount_num = line[0], line[1], line[2]
            # print(create_date, recharge_user_num, recharge_amount_num)
            create_date_lst.append(create_date)
            recharge_user_num_lst.append(recharge_user_num)
            recharge_amount_num_lst.append(recharge_amount_num)

    return render(request, 'analyse_demo.html',
                  {'create_date_lst': create_date_lst, 'recharge_user_num_lst': recharge_user_num_lst,
                   'recharge_amount_num_lst': recharge_amount_num_lst})


@login_required(login_url='/login')
def get_big_screen(request):
    return render(request, 'big_screen.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = auth.authenticate(username=username, password=password)
    if user_obj:
        return render(request, 'login.html')
    else:
        return render(request, 'login.html', {'error_msg': '密码错误'})


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# @login_required(login_url='/login')
# def login_check(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user_obj = auth.authenticate(username=username, password=password)
#
#         if user_obj:
#             # login(request, user_obj)
#             # return redirect("/demo/")
#             return render(request, 'big_screen.html')
#         else:
#             return redirect("/login")
#             # return render(request, 'login.html', {'error_msg': '密码错误'})
