import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect

# Create your views here. Send_repl
from maries_app.models import*

def About(request):
    return render(request,'about.html')

def Log(request):
    return render(request,'login_index.html')
def Login_post(request):
    unm = request.POST['name']
    psw = request.POST['password']
    res = login.objects.filter(username=unm, password=psw)
    if res.exists():
        res = res[0]
        request.session['lid'] = res.id
        if res.usertype == 'admin':
            return redirect('/home')
        if res.usertype == 'servpro':
            request.session['lid'] = res.id
            return redirect('/service_provider_home')
        else:
            return HttpResponse("invalid")
    else:
        return HttpResponse("wrong")




def home(request):
    return render(request,'admin/admin_index.html')

def Service_provider(request):
    res=service_provider.objects.filter(LOGIN__usertype='pending')
    return render(request,'admin/service provider.html',{'data':res})
# def view_approved_service_provider(request):
#     return render(request,'admin/view service provider.html')
def Service_subcat_manag(request):
    qry=service_type.objects.all()
    return render(request,'admin/service subcat mang.html',{"data":qry})

def approve_service_provider(request, id):
    login.objects.filter(id=id).update(usertype='service_proupdatevider')
    return HttpResponse('approved')

def reject_service_provider(request,id):
    login.objects.filter(id=id).update(usertype='reject')
    return HttpResponse('rejected')

def View_approved_service_provider(request):
    srv = service_provider.objects.filter(LOGIN__usertype='service_provider')
    return render(request,'admin/view approved service provider.html', {'data': srv})

def view_service_subcat_manag(request):
    sub=subcatogary.objects.all()
    return render(request, 'admin/view subcat.html', {'data': sub})


def add_service_subcat_post(request):
    servtype=request.POST['select2']
    subcat=request.POST['textfield2']
    obj=subcatogary()
    obj.SERVICE_TYPE_id=servtype
    obj.subcatogary_name=subcat
    obj.save()
    return HttpResponse("ok")

def Service_type_management(request):
    return render(request,'admin/service type management.html')

def add_service_post(request):
    ser=request.POST['textfield']
    obj=service_type()
    obj.type=ser
    obj.save()
    return HttpResponse("ok")
def view_Service_type_management(request):
    data=service_type.objects.all()
    return render(request,'admin/view service type.html',{'data':data})

def add_service_type(request):
    data=service_type.objects.all()
    return render(request,'admin/add service type.html',{'data':data})

def add_service_type_post(request):
    cat=request.POST['textfield']
    obj=service_type()
    obj.type=cat
    obj.save()
    return HttpResponse('ok')

def edit_subcat(request):
    return render(request,'admin/edit service type.html')









def View_complaint(request):
    com = complaint.objects.all()
    return render(request, 'admin/view complaint.html', {'data': com})

def Send_reply(request,id):
    return render(request,'admin/send rply.html',{"id":id})

def send_reply_post(request,id):
    replyy = request.POST['textfield']
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    complaint.objects.filter(id=id).update(reply=replyy,reply_date=dt)
    return HttpResponse('reply')





def View_rating(request):
    rat = rating.objects.all()
    return render(request, 'admin/view rating.html', {'data': rat})


def delete_service_type(request,id):
    service_type.objects.get(id = id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/view_Service_type_management'</script>")



def update_service_type(request):
    return render(request,"admin/edit service type.html")

def delete_subcategory(request,id):
    subcatogary.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/view_service_subcat_manag'</script>")


###############################################################
def service_provider_home(request):
    return render(request,"service provider/servicce_index.html")

def sevice_provider_register(request):
    return render(request,"register_index.html")

def service_provider_register_post(request):
    nm=request.POST['textfield']
    plc=request.POST['textfield2']
    pst=request.POST['textfield3']
    pn=request.POST['textfield4']
    eml=request.POST['textfield5']
    cnt=request.POST['textfield6']

    lati=request.POST['textfield7']
    logi=request.POST['textfield8']
    pas=request.POST['textfield9']
    pht = request.FILES['fileField']
    d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\ASUS\Desktop\maries\maries\maries_app\static\images\\" + d + '.jpg', pht)
    path = "/static/images/" + d + '.jpg'

    obj=login()
    obj.username=eml
    obj.password=pas
    obj.usertype="pending"
    obj.save()

    obj1=service_provider()
    obj1.name=nm
    obj1.place=plc
    obj1.post=pst
    obj1.pin=pn
    obj1.contact=cnt
    obj1.latitude=lati
    obj1.longitude=logi
    obj1.photo=path
    obj1.save()
    return HttpResponse("<script>alert('registered');window.location='/'</script>")


def view_profile(request):
    res=service_provider.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"service provider/view profile.html",{'data':res})
def view_profile_post(request):
    nm=request.POST['textfield']
    plc=request.POST['textfield2']
    pst=request.POST['textfield3']
    eml=request.POST['textfield5']
    cnt=request.POST['textfield6']
    if 'fileField' in request.FILES:
        pht=request.FILES['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ASUS\Desktop\maries\maries\maries_app\static\images\\" + d + '.jpg', pht)
        path = "/static/images/" + d + '.jpg'
        service_provider.objects.filter(LOGIN=request.session['lid']).update(photo=path)


    lati=request.POST['textField1']
    long=request.POST['textField']
    service_provider.objects.filter(LOGIN=request.session['lid']).update(name =nm,place=plc,post=pst,email=eml,contact=cnt,latitude=lati,longitude=long)
    return HttpResponse("<script>alert('updated sucessfully');window.location='/view_profile'</script>")


def edit_profile(request,id):
    res=service_provider.objects.get(id=id)
    return render(request,"service provider/edit profile.html",{'data':res})

def view_service_type_and_subcategories(request):
    res=service_type.objects.all()
    return render(request,"service provider/view service type.html",{'data':res})

def service_provider_view_subcat(request,id):
    sub=subcatogary.objects.filter(SERVICE_TYPE=id)
    return render(request,"service provider/view subcat.html",{'data':sub})


def add_service_management(request,id):

    res2=subcatogary.objects.all()
    return render(request,"service provider/add service mgnt.html",{'id':id,'data1':res2})

def add_service_management_post(request,id):
    sid=service_provider.objects.get(LOGIN=request.session['lid'])
    print(sid)
    # sty=request.POST['select']
    # ca=request.POST['select2']
    ph=request.FILES['fileField']
    des=request.POST['textfield4']
    pr=request.POST['textfield5']
    d=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\ASUS\Desktop\maries\maries\maries_app\static\images\\"+d+'.jpg',ph)
    p="/static/images/"+d+'.jpg'
    obj=service()
    obj.descrption=des
    obj.price=pr
    obj.photo=p
    obj.SERVICE_PROVIDER=sid
    obj.SUBCATEGORY_id=id
    obj.save()
    return HttpResponse("<script>alert('ok');window.location='/my_service'</script>")


def view_service_management(request,id):
    ser=service.objects.filter(SUBCATEGORY=id)
    return render(request,"service provider/view service mgnt.html",{'id':id,'data':ser})

def update_view_service_management(request,id):
    data = service.objects.get(id = id)
    return render(request,"service provider/edit service mgnt.html",{'id':id,"data":data})

def delete_view_service_management(request,id):
    service.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/service_provider_home'</script>")

def my_service(request):
    data=service.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request,"service provider/view service mgnt.html",{'data':data})

def edit_my_service(request):
    return render(request,"service provider/edit service mgnt.html")

def edit_my_service_post(request,id):
    try:

        pht=request.FILES['fileField']
        dis=request.POST['textfield4']
        pri=request.POST['textfield5']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\ASUS\Desktop\maries\maries\maries_app\static\images\\" + d + '.jpg', pht)
        path = "/static/images/" + d + '.jpg'
        service.objects.filter(id=id).update(photo=path,descrption=dis,price=pri)
        return HttpResponse("<script>alert('updated');window.location='/my_service'</script>")

    except Exception as e:
        dis = request.POST['textfield4']
        pri = request.POST['textfield5']
        service.objects.filter(id=id).update(descrption=dis,price=pri)
        return HttpResponse("<script>alert('updated');window.location='/my_service'</script>")

def view_rq_from_user_and_approve(request):
    res=request_service.objects.filter(status='pending')
    return render(request,"service provider/view rq from user.html",{'data':res})


def req_from_user_reject(request,id):
    request_service.objects.filter(id=id).update(status="reject")
    return HttpResponse("<script>alert('rejected');window.location='/view_rq_from_user_and_approve'</script>")

def req_from_user_approve(request,id):
    request_service.objects.filter(id=id).update(status="approve")
    return HttpResponse("<script>alert('approved');window.location='/view_rq_from_user_and_approve'</script>")


def view_approved_rq(request):
    req=request_service.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request,"service provider/view approved rq.html",{'data':req})


def view_rating(request):
    rtn = rating.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request,"service provider/view rating.html",{'data':rtn})


#..........................................................................................

def and_login(request):
    una=request.POST['uname']
    psw=request.POST['passw']
    log=login.objects.filter(username=una,password=psw)
    print(log)
    if log.exists():
        type=log[0].usertype
        lid=log[0].id
        return JsonResponse({"status":"ok","type":type,"lid":lid})
    return JsonResponse({"status":"no"})

def and_register(request):
    pic=request.FILES['pic']
    d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\ASUS\Desktop\maries\maries\maries_app\static\images\\" + d + '.jpg', pic)
    path = "/static/images/" + d + '.jpg'
    nm=request.POST['na']
    gnd=request.POST['gnd']
    plc=request.POST['pla']
    pt=request.POST['pos']
    pn=request.POST['pin']
    cnt=request.POST['phon']
    eml=request.POST['em']
    psw=request.POST['p']
    log = login(
        username=eml,
        password=psw,
        usertype='user'
    )
    log.save()
    obj=user()
    obj.LOGIN = log
    obj.name=nm
    obj.gender=gnd
    obj.email=eml
    obj.photo=path
    obj.place=plc
    obj.post=pt
    obj.pin=pn
    obj.contact=cnt
    obj.save()
    return JsonResponse({"status": "ok"})


def and_view_profile(request):
    lid=request.POST["lid"]
    res=user.objects.get(LOGIN_id=lid)
    return JsonResponse({"status": "ok",
                         "name":res.name,"gender":res.gender,"place":res.place,
                         "post":res.post,"pin":res.pin,"contact":res.contact,
                         "email":res.email,"photo":res.photo})

def and_view_service_provider(request):
    res=service_provider.objects.all()
    data=[]
    for i in res:
        data.append(
            {
                "name":i.name,"place":i.place,"post":i.post,"email":i.email,
                "contact":i.contact,"photo":i.photo,"latitude":i.latitude,"longitude":i.longitude
            }
        )
        print(data)
    return JsonResponse({"status":"ok","data":data})


def and_view_service(request):
    sid=request.POST['sid']
    res=service.objects.filter(SUBCATEGORY__SERVICE_TYPE=sid)
    li = []
    for i in res:
        li.append({
            'descrption':i.descrption,
            'price':i.price,
            'photo':i.photo
        })
    print(li)
    return JsonResponse({"status":"ok","data":li})

def and_view_service_type(request):
    res = service_type.objects.all()
    li = []
    for i in res:
        li.append({
            'id': i.id,
            'type': i.type
        })
    print(li)
    return JsonResponse({"status":"ok","users":li})

def and_send_request(request):
    request=request.POST['request']
    lid=request.POST['lid']
    sid=request.POST['sid']
    obj = request_service()
    obj.date=datetime.datetime.now().date()
    obj.status='pending'
    obj.payment_status='pendind'
    obj.payment_date='pending'
    obj.amount=''
    obj.USER=user.objects.get(LOGIN=lid)
    obj.SERVICE_PROVIDER_id=sid
    obj.save()
    return JsonResponse({"status": "ok"})

def and_feed_back(request):
    res = feed_back.objects.all()
    li = []
    for i in res:
        li.append({
            'date': i.date,
            'name': i.name
        })
    print(li)
    return JsonResponse({"status": "ok", "data": li})

def and_view_request_status(request):
   lid=request.POST['lid']
   print(lid)
   data=request_service.objects.filter(USER__LOGIN_id=lid)
   li = []
   for i in data:
       li.append({
           'date': i.date,
           'status': i.status,
           'payment_date':i.payment_date,
           'payment_status':i.payment_status,
           'amount':i.amount
       })
       print(li)
       return JsonResponse({"status": "ok", "data": li})



