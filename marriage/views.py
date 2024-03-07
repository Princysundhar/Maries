import datetime
import email
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def log(request):
    return render(request,"index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username = username,password = password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"

        if data.type == 'admin':
            return redirect('/admin_home')
        elif data.type == 'pending':
            return HttpResponse("<script>alert('wait for authentication');window.location='/'</script>")
        else:
            return redirect('/serviceprovider_home')

    else:
        return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")

def admin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"admin/index.html")

def serviceprovider_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"service provider/index.html")

def logout(request):
    request.session["lg"]=""
    return redirect('/')


# ..................... Admin module ..................

def view_service_provider(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    data = service_provider.objects.filter(LOGIN__type='pending')
    # print(data)
    return render(request,"admin/view_service_provider.html",{"data":data})

def view_approved_service_provider(request,id):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    login.objects.filter(id=id).update(type='serviceprovider')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Maries Verify")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))

    return redirect('/view_service_provider#ff')

def view_reject_service_provider(request,id):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    login.objects.filter(id=id).update(type='reject')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Maries Verify")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))

    return redirect('/view_service_provider#ff')

def approved_service_provider(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    data = service_provider.objects.filter(LOGIN__type='serviceprovider')
    return render(request,"admin/view_approved_serviceprovider.html",{"data":data})



def view_complaint(request):
    data = complaint.objects.all()
    return render(request,"admin/view_complaint.html",{"data":data})

def send_reply(request,id):
    return render(request,"admin/send_reply.html",{"id":id})

def send_reply_post(request,id):
    reply_date = datetime.datetime.now().strftime("%Y-%m-%d")
    reply = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply = reply,reply_date= reply_date)
    return HttpResponse("<script>alert('Reply sended');window.location='/view_complaint#ff'</script>")

def view_rating(request,id):
    data = rating.objects.filter(SERVICE_PROVIDER=id)
    return render(request,"admin/view_rating.html",{"data":data})

#.... service type management ...

def service_type_add(request):
    return render(request,"admin/service_type_add.html")

def service_type_add_post(request):
    service_types = request.POST['textfield']
    obj = service_type()
    obj.type = service_types
    obj.save()
    return HttpResponse("<script>alert('service type added');window.location='/service_type_add#ff'</script>")

def service_type_view(request):
    data = service_type.objects.all()
    return render(request,"admin/service_type_view.html",{"data":data})

def delete_service_type(request,id):
    service_type.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('service type deleted');window.location='/service_type_view#ff'</script>")

#....service sub category management ...

def service_subcategory_add(request):
    data = service_type.objects.all()
    return render(request,"admin/service_subcategory_add.html",{"data":data})

def service_subcategory_add_post(request):
    service_types = request.POST['select']
    subcategory_name = request.POST['textfield']
    obj = subcategory()
    obj.SERVICE_TYPE = service_type.objects.get(id=service_types)
    obj.subcategory_name = subcategory_name
    obj.save()
    return HttpResponse("<script>alert('success');window.location='/service_subcategory_add#ff'</script>")

def service_subcategory_view(request):
    data = subcategory.objects.all()
    return render(request,"admin/service_subcategory_view.html",{"data":data})

def service_subcategory_update(request,id):
    data = subcategory.objects.get(id=id)
    data1 = service_type.objects.all()
    return render(request,"admin/service_subcategory_edit.html",{"data":data,"id":id,"data1":data1})

def service_subcategory_update_post(request,id):
    service_types = request.POST['select']
    subcategory_name = request.POST['textfield']
    subcategory.objects.filter(id=id).update(SERVICE_TYPE=service_types,subcategory_name = subcategory_name)
    return HttpResponse("<script>alert('success');window.location='/service_subcategory_view#ff'</script>")

def delete_service_subcategory(request,id=id):
    subcategory.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('deleted success');window.location='/service_subcategory_view#ff'</script>")


##############################################################################

# service provider Module ........

def register(request):
    return render(request,"register_index.html")

def register_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    phone_no = request.POST['textfield6']
    password = request.POST['textfield7']
    lattitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\maries\marriage\static\photo\\"+dt+'.jpg',photo)
    path = '/static/photo/'+dt+'.jpg'

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already exist');window.location='/'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'pending'
        log_obj.save()

        obj = service_provider()
        obj.name = name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.phone_no = phone_no
        obj.photo = path
        obj.lattitude = lattitude
        obj.longitude = longitude
        obj.LOGIN = log_obj

        obj.save()
        return HttpResponse("<script>alert('Registration success');window.location='/register#aa'</script>")

def view_profile(request):
    data = service_provider.objects.get(LOGIN=request.session['lid'])
    return render(request,"service provider/view_profile.html",{"data":data})

def edit_profile(request,id):
    data = service_provider.objects.get(id=id)
    return render(request,"service provider/edit_profile.html",{"data":data,"id":id})

def edit_profile_post(request,id):
    try:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        phone_no = request.POST['textfield6']
        photo = request.FILES['fileField']

        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y-%m-%d")
        fs.save(r"C:\Users\DELL\PycharmProjects\maries\marriage\static\photo\\" + dt + '.jpg', photo)
        path = '/static/photo/' + dt + '.jpg'
        print(path)
        service_provider.objects.filter(id=id).update(name= name,place=place,post=post,pin=pin,email=email,phone_no=phone_no,photo=path)
        return HttpResponse("<script>alert('Your profile updated');window.location='/view_profile#ff'</script>")

    except Exception as e:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        phone_no = request.POST['textfield6']
        service_provider.objects.filter(id=id).update(name= name,place=place,post=post,pin=pin,email=email,phone_no=phone_no)
        return HttpResponse("<script>alert('Your profile updated');window.location='/view_profile#ff'</script>")

def view_service_type_subcategory(request,id):
    data = subcategory.objects.filter(SERVICE_TYPE=id)
    return render(request,"service provider/view_servicetype_subcategory.html",{"datas":data})

# service management .............

def add_service(request):
    data = subcategory.objects.all()
    data1 = service_type.objects.all()

    return render(request,"service provider/add_service.html",{"data":data,"data1":data1})

def add_service_post(request):
    subcategorys = request.POST['select']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\maries\marriage\static\photo\\" + dt + '.jpg', photo)
    path = '/static/photo/' + dt + '.jpg'
    print(path)

    description = request.POST['textarea']
    price = request.POST['textfield']
    obj = service()
    obj.photo = path
    obj.description = description
    obj.price = price
    obj.SERVICE_PROVIDER =service_provider.objects.get(LOGIN=request.session['lid'])
    obj.SUBCATEGORY = subcategory.objects.get(id=subcategorys)
    obj.save()
    return HttpResponse("<script>alert('service added');window.location='/add_service#ff'</script>")

def view_service(request):
    data = service.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])

    return render(request,"service provider/view_service.html",{"data":data})

def update_service(request,id,sid):
    data = subcategory.objects.filter(SERVICE_TYPE=sid)
    data1 = service.objects.get(id=id)
    return render(request,"service provider/update_service.html",{"data":data,"data1":data1})

def update_service_post(request,id,sid):
    try:
        subcategorys = request.POST['select']
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\maries\marriage\static\photo\\" + dt + '.jpg', photo)
        path = '/static/photo/' + dt + '.jpg'
        print(path)
        description = request.POST['textarea']
        price = request.POST['textfield']
        service.objects.filter(id=id).update(photo=path,description=description,price=price,SUBCATEGORY = subcategory.objects.get(id=subcategorys))
        return HttpResponse("<script>alert('updated Successfully');window.location='/view_service#ff'</script>")

    except Exception as e:
        subcategorys = request.POST['select']
        description = request.POST['textarea']
        price = request.POST['textfield']
        service.objects.filter(id=id).update(description=description, price=price,SUBCATEGORY = subcategory.objects.get(id=subcategorys))
        return HttpResponse("<script>alert('updated Successfully');window.location='/view_service#ff'</script>")

def delete_service(request,id):
    service.objects.get(id=id).delete()
    return HttpResponse("<script>alert('service deleted');window.location='/view_service#ff'</script>")


def view_request_from_user(request):
    data = req.objects.filter(status='pending',SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request,"service provider/view_request_from_user.html",{"data":data})

def view_service_for_request(request,id):
    data = req_sub.objects.filter(REQUEST=id)
    return render(request,"service provider/view_items.html",{"data":data})

def view_approved_request(request,rid):
    req.objects.filter(id=rid).update(status="approved")
    # return render(request,"service provider/view_approved_request.html",{"data":data})
    return redirect('/view_request_from_user#ff')

def view_request_approve(request):
    data = req.objects.filter(status='approved', SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request, "service provider/view_request_approve.html", {"data": data})

def view_reject_request(request,id):
    req.objects.filter(id=id).update(status='reject')
    # return render(request,"service provider/view_approved_request.html",{"data":data})
    return redirect('/view_request_from_user#ff')

def view_payment(request):
    data = req.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])
    return render(request,"service provider/view_payment.html",{"data":data})

def view_ratings(request):
    res = rating.objects.filter(SERVICE_PROVIDER__LOGIN=request.session['lid'])
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    data = []

    for rt in res:
        print(rt)
        a = float(rt.rate)
        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })
        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            data.append({
                'USER': rt.USER,
                'SERVICE_PROVIDER': rt.SERVICE_PROVIDER,
                'date': rt.date,
                'rate': ar,

            })
        print(data, "data")

    return render(request, "service provider/view_rating.html", {"data": data})

 #..... Chat

def chatt(request,u):
    request.session['head']="CHAT"
    request.session['uid'] = u
    return render(request,'service provider/chat.html',{'u':u})


def chatsnd(request,u):
        d=datetime.datetime.now().strftime("%Y-%m-%d")

        c = request.session['lid']
        b=request.POST['n']
        # print(b)
        # print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = service_provider.objects.get(LOGIN__id=c)
        uu = user.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.type='serviceprovider'
        obj.SERVICE_PROVIDER=cc
        obj.USER=uu
        obj.chat=m
        obj.save()
        # print(obj)
        v = {}
        if int(obj.id) > 0:
            v["status"] = "ok"
            return JsonResponse({"status":"ok"})
        else:
            v["status"] = "error"
            return JsonResponse({"status": "error"})



def chatrply(request):
    # if request.session['log']=="lo":
        c = request.session['lid']
        cc = service_provider.objects.get(LOGIN__id=c)
        uu = user.objects.get(id=request.session['uid'])
        res = chat.objects.filter(SERVICE_PROVIDER=cc,USER=uu)
        # print(res)
        v = []
        if len(res) > 0:
            # print(len(res))
            for i in res:
                v.append(
                    {
                    'type':i.type,
                    'chat':i.chat,
                    'nam':i.USER.name,
                    'spic':i.SERVICE_PROVIDER.photo,
                    'dtime':i.date,
                    'tname':i.SERVICE_PROVIDER.name,
                })
            print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})


#............................................................................................#

# user module(Android)

def android_login(request):
    username  = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username, password=password)
    if data.exists():
        lid = data[0].id
        print(lid)
        res = user.objects.get(LOGIN=lid)
        type = data[0].type
        name = res.name
        email = res.email
        photo = res.photo
        # print(photo)
        return JsonResponse({'status': "ok", 'lid': lid, 'type': type, 'name': name, 'email': email, 'photo': photo})
    else:
        return JsonResponse({"status": None})

def android_user_registration(request):
    name = request.POST['name']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['phone_no']
    password = request.POST['password']
    photo = request.FILES['pic']  # Image field
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\maries\marriage\static\photo\\" + d + '.jpg', photo)
    path = '/static/photo/' + d + '.jpg'
    # print(path)

    data = login.objects.filter(username=email)
    if data.exists():
        return JsonResponse({"status": None})
    else:

        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'user'
        log_obj.save()

        obj = user()
        obj.name = name
        obj.gender = gender
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.phone_no = contact
        obj.photo = path
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({'status': "ok"})

def android_view_profile(request):
    lid = request.POST['lid']
    res = user.objects.get(LOGIN=lid)
    return JsonResponse({"status": "ok", "name": res.name,"gender":res.gender, "place": res.place,
                         "post": res.post, "pin": res.pin, "email": res.email, "contact": res.phone_no,
                         "photo": res.photo})
    # print(photo)

def android_view_nearby_serviceprovider(request):
    qry = service_provider.objects.filter(LOGIN__type='serviceprovider')
    lati = request.POST['lati']
    longi = request.POST['longi']

    latitude = str(lati)
    longitude = str(longi)
    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"

    ar = []
    for i in qry:
        qs = service_provider.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.lattitude, i.longitude, i.lattitude))).order_by('distance')
        ar.append(
            {
                "spid": i.id,
                "name": i.name,
                "place": i.place,
                "post" :i.post,
                "pin":i.pin,
                "email": i.email,
                "phone_no": i.phone_no,
                "photo": i.photo,
                "lattitude": i.lattitude,
                "longitude": i.longitude,
                "serviceprovider_distance": qs[0].distance
            }
        )

    def serviceprovider_nearby_sort(e):
        return e['serviceprovider_distance']

    ar.sort(key=serviceprovider_nearby_sort)

    return JsonResponse({"status": "ok", "data": ar})

def android_view_rating(request):
    spid = request.POST['spid']
    res = rating.objects.filter(SERVICE_PROVIDER=spid)
    ar =[]
    for i in res:
        ar.append(
            {
                "rid":i.id,
                "rate":i.rate,
                "date":i.date,
                "name":i.USER.name,
                "email":i.USER.email
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_servicetype_subcategory(request):
    typeid = request.POST['type_id']
    # print(typeid)
    sid=request.POST['sid']
    res = subcategory.objects.filter(SERVICE_TYPE=typeid,service__SERVICE_PROVIDER=sid)
    ar = []
    for i in res:
        ar.append(
            {
                "sub_id": i.id,
                "sub_category_name": i.subcategory_name
            }
        )
    # print(ar)
    if len(ar)>0:
        # print("aaaaaaaaa")
        return JsonResponse({"status": "ok", "data": ar})
    else:
        # print("bbbbbbbbbbbbb")
        return JsonResponse({"status":"no"})

def and_view_category(request):
    res = service_type.objects.all()

    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "ctype":i.type
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_view_service(request):
    sub_id = request.POST['sub_id']
    sid = request.POST['sid']
    res = service.objects.filter(SUBCATEGORY=sub_id,SERVICE_PROVIDER=sid)
    ar =[]
    for i in res:
        ar.append(
            {
                "sid":i.id,
                "photo":i.photo,
                "description":i.description,
                "price":i.price
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_user_request(request):
    date = request.POST['date']
    sid = request.POST['sid']
    lid = request.POST['lid']
    logininstance = login.objects.get(id=lid)
    userinstance = user.objects.get(LOGIN=logininstance)
    data = service_cart.objects.filter(USER__LOGIN=lid,SERVICE=sid)
    if data.exists():
        return JsonResponse({"status":"no"})
    else:
        obj = service_cart()
        obj.request_date = date
        obj.SERVICE = service.objects.get(id=sid)
        obj.USER = userinstance
        obj.save()

        return JsonResponse({"status": "ok"})

def android_view_service_cart(request):
    lid = request.POST['lid']
    res = service_cart.objects.filter(USER__LOGIN=lid)
    amount=0

    ar = []
    for i in res:
        sprice=i.SERVICE.price
        amount = int(amount)+ int(sprice)
        ar.append(
            {
                "cart_id":i.id,
                "subcategory":i.SERVICE.SUBCATEGORY.subcategory_name,
                "description":i.SERVICE.description,
                "photo":i.SERVICE.photo,
                "price":i.SERVICE.price,
                "req_date":i.request_date,
                "serviceprovider_info":i.SERVICE.SERVICE_PROVIDER.name
            }
        )
    # print(amount)
    return JsonResponse({"status":"ok","data":ar,"am":amount})


def android_cart_placeorder(request):
    am = request.POST['am']
    lid = request.POST['lid']
    # print("ammmmmmmmmmmmmmm",am)
    provide_list=[]
    qry=service_cart.objects.filter(USER=user.objects.get(LOGIN=lid))

    for i in qry:
        provider_id=i.SERVICE.SERVICE_PROVIDER_id
        if provider_id  not in provide_list:
            provide_list.append(provider_id)
    for j in provide_list:
        # print("p1111111111",j)
        data = req.objects.filter(SERVICE_PROVIDER=str(j),USER__LOGIN=lid,status='pending')
        print("dataaaaaaaa",data)
        if data.exists():
            req_id=data[0].id
            qry1=service_cart.objects.filter(USER__LOGIN=lid,SERVICE__SERVICE_PROVIDER=j)
            # print("qry1111111111",qry1)
            for k in qry1:
                obj1 = req_sub()
                obj1.SERVICE_id = k.SERVICE_id
                obj1.request_date = k.request_date
                obj1.REQUEST_id = req_id
                obj1.save()

        else:
            qry2 = service_cart.objects.filter(USER__LOGIN=lid, SERVICE__SERVICE_PROVIDER=j)

            # print("qry22222222",qry2)
            obj = req()
            obj.USER = user.objects.get(LOGIN=lid)
            obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
            obj.status = 'pending'
            obj.payment_status = 'pending'
            obj.amount = 0
            obj.payment_date = datetime.datetime.now().strftime("%Y-%m-%d")
            obj.SERVICE_PROVIDER_id = j
            obj.save()
            for r in qry2:
                reqid=obj.id
                # print("reqid",reqid)
                qry3=req.objects.get(id=reqid)
                qamount=qry3.amount
                # print("qamount",qamount)
                amount_total=int(qamount)+int(r.SERVICE.price)
                # print("qry3",qry3)
                # print("amount_total",amount_total)
                obj1 = req_sub()
                obj1.SERVICE_id = r.SERVICE_id
                obj1.request_date = r.request_date
                obj1.REQUEST= obj
                obj1.save()
                req.objects.filter(id=reqid).update(amount=amount_total)

    data = service_cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status": "ok"})





def android_cancel_order(request):
    cart_id = request.POST['cart_id']
    service_cart.objects.get(id=cart_id).delete()
    return JsonResponse({"status":"ok"})

def android_view_request_status(request):
    lid = request.POST['lid']
    res = req_sub.objects.filter(REQUEST__USER__LOGIN=lid,REQUEST__status="approved",REQUEST__payment_status="pending")
    amount = 0
    ar = []
    for i in res:
        sprice = i.SERVICE.price
        amount = int(amount) + int(sprice)
        # print(sprice)
        ar.append(
            {
                "req_id":i.id,
                "req_date":i.request_date,
                "date":i.REQUEST.date,
                "description":i.SERVICE.description,
                "price":i.SERVICE.price,
                "photo":i.SERVICE.photo,
                "name":i.REQUEST.SERVICE_PROVIDER.name,
                "email":i.REQUEST.SERVICE_PROVIDER.email,
                "subcategory":i.SERVICE.SUBCATEGORY.subcategory_name


            }
        )
    # print("ammmmmmmm",amount)
    return JsonResponse({"status": "ok", "data": ar,"amount":amount})

def android_make_payment(request):                  # offline
    payment_mode = request.POST['mode']
    # rid = request.POST['req_id']
    lid = request.POST['lid']
    data = req.objects.filter(USER__LOGIN=lid,status = 'approved')
    for i in data:
        req_id = i.id

        req.objects.filter(id=req_id).update(payment_status=payment_mode)
    return JsonResponse({"status": "ok"})

def android_online_payment(request):                  # online
    payment_mode = request.POST['mode']
    bid = request.POST['bid']
    print("okkkkk",bid)
    lid = request.POST['lid']
    data = req.objects.filter(USER__LOGIN=lid,status = 'approved')
    for i in data:
        req_id = i.id

        req.objects.filter(id=req_id).update(payment_status='online')
    return JsonResponse({"status": "ok"})


def android_view_serviceprovider_history(request):
    lid = request.POST['lid']
    res = req.objects.filter(Q(payment_status='online')|Q(payment_status='offline'),USER__LOGIN=lid)
    ar =[]
    for i in res:
        ar.append(
            {
                "hid":i.SERVICE_PROVIDER_id,
                "name":i.SERVICE_PROVIDER.name,
                "email":i.SERVICE_PROVIDER.email,
                "contact":i.SERVICE_PROVIDER.phone_no,
                "photo":i.SERVICE_PROVIDER.photo,
                "amount":i.amount,
                "date":i.date
            }
        )
    return JsonResponse({"status":"ok","data":ar})

# def android_view_request_sub_items(request):
#
#     return  JsonResponse({"status":"ok"})

def android_send_rate(request):
    hid = request.POST['hid']
    lid = request.POST['lid']


    rate = request.POST['rate']
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj = rating()
    obj.rate = rate
    obj.date = date
    obj.USER = user.objects.get(LOGIN=lid)
    obj.SERVICE_PROVIDER_id = hid
    obj.save()
    return JsonResponse({"status": "ok"})

def android_add_chat(request):
    lid = request.POST['lid']
    hid = request.POST['toid']
    msg = request.POST['message']
    # print(lid)
    # print(hid)
    logininstance = login.objects.get(id=lid)
    userinstance = user.objects.get(LOGIN=logininstance)


    date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj = chat()
    obj.chat = msg
    obj.type ='user'
    obj.USER = userinstance
    obj.SERVICE_PROVIDER_id = hid
    obj.date = date
    obj.save()

    return JsonResponse({"status": "Inserted"})

def android_view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    res = chat.objects.filter(Q(USER_id=user.objects.get(LOGIN_id=lid)), Q(SERVICE_PROVIDER=service_provider.objects.get(id=toid)),
                              Q(id__gt=lastid))
    ar = []
    for i in res:
        ar.append(
            {
            "id": i.id,
            "date": i.date,
            "userid": i.USER.id,
            "sid": i.type,
            "chat": i.chat,

        })

    return JsonResponse({'status': "ok", 'data': ar})

def android_view_request_sub_items(request):
    hid = request.POST['hid']
    # req_sub_id = request.POST['req_sub_id']
    res = req_sub.objects.filter(SERVICE__SERVICE_PROVIDER=hid)
    ar = []
    for i in res:
        ar.append(
            {
                "req_sub_id":i.id,
                "description":i.SERVICE.description,
                "photo":i.SERVICE.photo,
                "price":i.SERVICE.price,
                "amount":i.REQUEST.amount,
                "subcategory":i.SERVICE.SUBCATEGORY.subcategory_name,
                "req_date":i.request_date
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_send_complaint(request):
    lid = request.POST['lid']
    # userinstance = user.objects.get(LOGIN=lid)
    complaints = request.POST['complaint']
    complaint_date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj1 = complaint()
    obj1.complaints = complaints
    obj1.complaint_date = complaint_date
    obj1.reply = 'pending'
    obj1.reply_date = '0000-00-00'
    obj1.USER = user.objects.get(LOGIN=lid)
    obj1.save()
    return JsonResponse({"status":"ok"})

def android_view_complaint(request):
    lid = request.POST['lid']
    # userinstance = user.objects.get(LOGIN = lid)
    res = complaint.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "complaint":i.complaints,
                "complaint_date":i.complaint_date,
                "reply":i.reply,
                "reply_date":i.reply_date
            }
        )
    return JsonResponse({"status":"ok","data":ar})













