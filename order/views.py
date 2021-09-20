from django.shortcuts import redirect
from django.views import generic
from .models import OrderMenu, OrderDetail, Patient
import json
from . import config
from . import data
# Create your views here.



class SelectView(generic.ListView):
    template_name = 'order/select.html'
    model = OrderMenu

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SelectView, self).get_context_data(**kwargs)
        context['category_name'] = OrderMenu.objects.values('category').distinct()
        return context

    def post(self, request, *args, **kwargs):
        # POSTデータ取得
        postordername = self.request.POST.getlist('ordername')
        last_order = OrderDetail.objects.order_by("id").last()
        last_order.ordername = postordername
        last_order.save()
        ordermenutable = OrderMenu.objects.all()

        # JSON作成
        def intivtype(ivtype): # ivtypeを整数に変換する
            return 1 if ivtype == '静脈注射' else 2 if ivtype == '筋肉注射' else 3 if ivtype == '皮下注射' else 4 if ivtype == '点滴注射' else 5 if ivtype == '皮内注射' else 6 if ivtype == 'その他注射' else ""

        array_data = {
            'fullname' : str(last_order.ptname),
            'kana' : str(last_order.kananame),
            "dob":"", 
            "gender":"",
            'patientno' : str(last_order.patientid), 
            'order' : []
        }
        
        for name in postordername:
            for order in ordermenutable:
                if order.name == name:
                    if order.type != None:
                        dic = {
                            'type' : order.type,
                            'detail' : {'code': "" if order.code == None else order.code, 'name': order.name, 'qty': 1, 'type': intivtype(order.ivtype),}
                            }
                        array_data['order'].append(dic)
                    else:
                        dic = {
                            'type' : "",
                            'detail' : {'code': "" if order.code == None else order.code, 'name': order.name, 'qty': 1}
                            }
                        array_data['order'].append(dic)

        # カルテへポスト
        data.make_request(clinic_id=config.CURRENT_CLINC,patient_data=array_data)
    
        # リダイレクト
        return redirect('/')


class IndexView(generic.ListView):
    template_name = 'order/index.html'
    model = OrderMenu

    def post(self, request, *args, **kwargs):
        fullname = self.request.POST['fullname']
        patientid = self.request.POST['patientid']
        kana = self.request.POST['kana']
        print(fullname, patientid,kana)
        od = OrderDetail(patientid=patientid, ptname=fullname, kananame=kana)
        od.save()
        return redirect('/select')


class GocounterView(generic.TemplateView):
    template_name = 'order/gocounter.html'

class ReturnptView(generic.TemplateView):
    template_name = 'order/returnpt.html'

class NewinputView(generic.TemplateView):
    template_name = 'order/newinput.html'

    def post(self, request, *args, **kwargs):
        fullname = self.request.POST['fullname']
        patientid = self.request.POST['patientid']
        kana = self.request.POST['kana']
        print(fullname, patientid,kana)
        od = OrderDetail(patientid=patientid, ptname=fullname, kananame=kana)
        od.save()
        return redirect('/order/select/')

class ReturninputView(generic.TemplateView):
    template_name = 'order/returninput.html'

    def post(self, request, *args, **kwargs):
        fullname = self.request.POST['fullname']
        patientid = self.request.POST['patientid']
        kana = self.request.POST['kana']
        print(fullname, patientid,kana)
        od = OrderDetail(patientid=patientid, ptname=fullname, kananame=kana)
        od.save()
        return redirect('/select')