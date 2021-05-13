from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.db import connections


def index(request):
    return render(request, 'index.html')


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
