from django.shortcuts import redirect
from django.views import generic
from .models import OrderMenu, OrderDetail
import json

from . import config
from . import data
# Create your views here.



class SelectView(generic.ListView):
    template_name = 'order/select.html'
    model = OrderMenu

    def post(self, request, *args, **kwargs):
        # POSTデータ取得
        postordername = self.request.POST.getlist('ordername')
        last_order = OrderDetail.objects.order_by("id").last()
        last_order.ordername = postordername
        last_order.save()
        print(postordername)
        print(last_order.patientid)

        # JSON作成     
        array_data = {
            'patientno' : last_order.patientid, 
            'order' : []
        }
        ordermenutable = OrderMenu.objects.all()
        for name in postordername:
            for order in ordermenutable:
                if order.name == name:
                    # print(type(order.name))
                    code = str(order.code)
                    dic = None
                    dic = {
                        'type' : order.type,
                        'detail' : {
                            'code' : code,
                            'name' : order.name,
                            'qty' : 1
                            }
                        }
                    array_data['order'].append(dic)

        # print(array_data)
        
        json_data = json.dumps(array_data,ensure_ascii=False)
        print(json_data)
        # カルテへポスト
        # data.make_request(clinic_id=config.CURRENT_CLINC,patient_data=json_data.encode('utf-8'))
        data.make_request(clinic_id=config.CURRENT_CLINC,patient_data=array_data)
    
        # リダイレクト
        return redirect('/order/')


class IndexView(generic.ListView):
    template_name = 'order/index.html'
    model = OrderMenu

    def post(self, request, *args, **kwargs):
        postptid = self.request.POST['patientid']
        od = OrderDetail(patientid=postptid)
        od.save()
        print(postptid)

        return redirect('/order/select/')