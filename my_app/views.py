import datetime
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def forgot_password(request):
    return render(request,"forgot_password.html")

def forgot_password_post(request):
    email = request.POST['textfield']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("princyz873@gmail.com", "tcap lzzh lmrz afio")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "princyz873@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for Krishibhavan Website"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password sended');window.location='/'</script>")
    return HttpResponse("mail incorrect")

def log(request):
    return render(request,"login_index.html")

def log_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"
        if data.usertype == 'admin':
            return HttpResponse("<script>alert('Login success');window.location='/admin_home'</script>")
        elif data.usertype == 'agriculture_office':
            return HttpResponse("<script>alert('Login success');window.location='/officer_home'</script>")
        else:
            return HttpResponse("<script>alert('Invalid Authentication');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Wrong Details');window.location='/'</script>")


def admin_home(request):
    return render(request,"admin/admin_index.html")

def logout(request):
    request.session['lg'] = ""
    return redirect('/')


# ...AGRICULTURE OFFICE MANAGEMENT

def add_agriculture_office(request):
    return render(request, "admin/add_agriculture_office.html")

def add_agriculture_office_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    latitude = request.POST['textfield4']
    longitude = request.POST['textfield5']
    password = random.randint(0000,9999)
    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/add_agriculture_office'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'agriculture_office'
        log_obj.save()

        obj = agriculture_office()
        obj.name = name
        obj.email = email
        obj.contact = contact
        obj.latitude = latitude
        obj.longitude = longitude
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/add_agriculture_office'</script>")

def view_agriculture_office(request):
    data = agriculture_office.objects.all()
    return render(request, "admin/view_agriculture_office.html", {"data":data})

def update_agriculture_office(request,id):
    data = agriculture_office.objects.get(id=id)
    return render(request, "admin/update_agriculture_office.html", {"data":data, "id":id})

def update_agriculture_office_post(request,id):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    latitude = request.POST['textfield4']
    longitude = request.POST['textfield5']
    agriculture_office.objects.filter(id=id).update(name=name,email=email,contact=contact,latitude=latitude,longitude=longitude)
    return HttpResponse("<script>alert('Updated Successfully');window.location='/view_agriculture_office#ppp'</script>")

def delete_agriculture_office(request,id):
    agriculture_office.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/view_agriculture_office#ppp'</script>")


def send_notification_office(request):
    return render(request, "admin/send_notification_office.html")

def send_notification_office_post(request):
    notifications = request.POST['textfield']
    obj = notification_office()
    obj.notification = notifications
    obj.date = datetime.datetime.now().strftime("%Y/%m/%d-%H/%M/%S")
    obj.save()
    return HttpResponse("<script>alert('Notification Sended');window.location='/send_notification_office#ppp'</script>")

def view_notification_office(request):
    data = notification_office.objects.filter(AGRICULTURE_OFFICE__LOGIN=request.session['lid'])
    # data = notification_office.objects.all()
    return render(request, "admin/view_notification_office.html",{"data":data})

def delete_notification_office(request,id):
    notification_office.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Notification Deleted');window.location='/view_notification_office#ppp'</script>")

def view_complaint(request):
    data = complaint.objects.all()
    return render(request,"admin/view_complaint.html",{"data":data})

def send_reply(request,id):
    return render(request,"admin/send_reply.html",{"id":id})

def send_reply_post(request,id):
    reply = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply = reply,reply_date=datetime.datetime.now().strftime("%Y/%m/%d-%H/%M/%S"))
    return HttpResponse("<script>alert('Reply Sended');window.location='/view_complaint#ppp'</script>")

def view_feedback(request):
    data = feedback.objects.all()
    return render(request,"admin/view_feedback.html",{"data":data})

#.................................................................................................... AGRICULTURE OFFICER

def officer_home(request):
    return render(request,"Agriculture_office/officer_index.html")

def view_notification(request):
    data = notification_office.objects.filter(AGRICULTURE_OFFICE__LOGIN=request.session['lid'])
    return render(request,"Agriculture_office/view_notification_officer.html",{"data":data})

def add_subsidy(request):
    return render(request,"Agriculture_office/add_subsidy.html")

def add_subsidy_post(request):
    item_name = request.POST['textfield']
    details = request.POST['textarea']
    From = request.POST['textfield2']
    To = request.POST['textfield3']
    data = subsidy.objects.filter(item_name=item_name)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/add_subsidy#ppp'</script>")
    else:

        obj = subsidy()
        obj.item_name = item_name
        obj.details = details
        obj.From = From
        obj.To = To
        obj.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/add_subsidy#ppp'</script>")

def view_subsidy(request):
    data = subsidy.objects.all()
    return render(request,"Agriculture_office/view_subsidy.html",{"data":data})

def update_subsidy(request,id):
    data = subsidy.objects.get(id=id)
    return render(request,"Agriculture_office/update_subsidy.html",{"data":data,"id":id})

def update_subsidy_post(request,id):
    item_name = request.POST['textfield']
    details = request.POST['textarea']
    From = request.POST['textfield2']
    To = request.POST['textfield3']
    subsidy.objects.filter(id=id).update(item_name=item_name,details=details,From=From,To=To)
    return HttpResponse("<script>alert('updated successfully');window.location='/view_subsidy#ppp'</script>")

def delete_subsidy(request,id):
    subsidy.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/view_subsidy#ppp'</script>")


def add_stock(request):
    return render(request,"Agriculture_office/add_stock.html")

def add_stock_post(request):
    type = request.POST['textfield']
    name = request.POST['textfield2']
    price = request.POST['textfield3']
    quantity = request.POST['textfield4']
    image = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Krishibhavan\my_app\static\photo\\" +dt+'.jpg',image)
    path = '/static/photo/' + dt + '.jpg'
    data = stock.objects.filter(name=name)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists');window.location='/add_stock#ppp'</script>")
    else:

        obj = stock()
        obj.type = type
        obj.name = name
        obj.price = price
        obj.quantity = quantity
        obj.image = path
        obj.AGRICULTURE_OFFICE = agriculture_office.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/add_stock#ppp'</script>")




def view_stock(request):
    data = stock.objects.filter(AGRICULTURE_OFFICE__LOGIN=request.session['lid'])
    return render(request,"Agriculture_office/view_stock.html",{"data":data})

def update_stock(request,id):
    data = stock.objects.get(id=id)
    return render(request,"Agriculture_office/update_stock.html",{"data":data,"id":id})

def update_stock_post(request,id):
    try:
        type = request.POST['textfield']
        name = request.POST['textfield2']
        price = request.POST['textfield3']
        quantity = request.POST['textfield4']
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\Krishibhavan\my_app\static\photo\\" + dt + '.jpg', image)
        path = '/static/photo/' + dt + '.jpg'
        print(path)
        stock.objects.filter(id=id).update(type=type, name=name, price=price, quantity=quantity,image=path)
        return HttpResponse("<script>alert('updated successfullyy');window.location='/view_stock#ppp'</script>")
    except Exception as e:
        type = request.POST['textfield']
        name = request.POST['textfield2']
        price = request.POST['textfield3']
        quantity = request.POST['textfield4']
        stock.objects.filter(id=id).update(type=type, name=name, price=price, quantity=quantity)
        return HttpResponse("<script>alert('updated successfully');window.location='/view_stock#ppp'</script>")

def delete_stock(request,id):
    stock.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/view_stock#ppp'</script>")

def view_stock_request(request):
    data = orders.objects.filter(AGRICULTURE_OFFICE__LOGIN=request.session['lid'])
    return render(request,"Agriculture_office/view_stock_request.html",{"data":data})

def view_order_sub(request,id):
    data = order_sub.objects.filter(ORDERS=id)
    return render(request,"Agriculture_office/view_order_sub.html",{"data":data})


def add_fertilizer(request):
    return render(request,"Agriculture_office/add_fertilizer.html")

def add_fertilizer_post(request):
    name = request.POST['textfield']
    price = request.POST['textfield2']
    details = request.POST['textarea']
    data = fertilizer.objects.filter(name=name)
    if data.exists():
        return HttpResponse("<script>alert('Already Exist');window.location='/add_fertilizer#ppp'</script>")
    else:
        obj = fertilizer()
        obj.name = name
        obj.price = price
        obj.details = details
        obj.AGRICULTURE_OFFICE = agriculture_office.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added successfully');window.location='/add_fertilizer#ppp'</script>")


def view_fertilizer(request):
    data = fertilizer.objects.filter(AGRICULTURE_OFFICE__LOGIN=request.session['lid'])
    return render(request,"Agriculture_office/view_fertilizer.html",{"data":data})

def update_fertilizer(request,id):
    data = fertilizer.objects.get(id=id)
    return render(request,"Agriculture_office/update_fertilizer.html",{"data":data,"id":id})

def update_fertilizer_post(request,id):
    name = request.POST['textfield']
    price = request.POST['textfield2']
    details = request.POST['textarea']
    fertilizer.objects.filter(id=id).update(name=name,price=price,details=details)
    return HttpResponse("<script>alert('Updated successfully');window.location='/view_fertilizer#ppp'</script>")

def delete_fertilizer(request,id):
    fertilizer.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted successfully');window.location='/view_fertilizer#ppp'</script>")


def add_success_story(request):
    return render(request,"Agriculture_office/add_success_story.html")

def add_success_story_post(request):
    notes = request.POST['textarea']
    date = request.POST['textfield']
    data = success_story.objects.filter(notes=notes)
    if data.exists():
        return HttpResponse("<script>alert('Already noted');window.location='/add_success_story#ppp'</script>")
    else:

        obj = success_story()
        obj.notes = notes
        obj.date = date
        obj.AGRICULTURE_OFFICE = agriculture_office.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Story Added');window.location='/add_success_story#ppp'</script>")

def view_success_story(request):
    data = success_story.objects.all()
    return render(request,"Agriculture_office/view_success_story.html",{"data":data})

def delete_success_story(request,id):
    success_story.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Story Deleted');window.location='/view_success_story#ppp'</script>")



def send_notification(request):
    return render(request,"Agriculture_office/send_notification.html")

def send_notification_post(request):
    notifications = request.POST['textfield']
    data = notification.objects.filter(notifications=notifications)
    if data.exists():
        return HttpResponse("<script>alert('Already added');window.location='/send_notification#ppp'</script>")
    else:
        obj = notification()
        obj.notifications = notifications
        obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.save()
        return HttpResponse("<script>alert('Notification sended');window.location='/send_notification#ppp'</script>")

#...................WEB CHAT

def chatt(request,u):
    request.session['head']="CHAT"
    request.session['uid'] = u
    return render(request,'Agriculture_office/chat.html',{'u':u})


def chatsnd(request,u):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    # t=datetime.datetime.now().strftime("%H:%M:%S")
    c = request.session['lid']
    b=request.POST['n']
    # print(b)
    # print(u,"userrrrrrrrrr")
    m=request.POST['m']
    cc = agriculture_office.objects.get(LOGIN__id=c)
    uu = user.objects.get(id=request.session['uid'])
    obj=chat()
    obj.date=d
    obj.type='agriculture_officer'
    obj.AGRICULTURE_OFFICE=cc
    obj.USER=uu
    obj.chat=m
    obj.save()
    # print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r
    # else:
    #     return redirect('/')

def chatrply(request):
    # if request.session['log']=="lo":
    c = request.session['lid']
    cc=agriculture_office.objects.get(LOGIN__id=c)
    uu=user.objects.get(id=request.session['uid'])
    res = chat.objects.filter(AGRICULTURE_OFFICE=cc,USER=uu)
    # print(res)
    v = []
    if len(res) > 0:
        # print(len(res))
        for i in res:
            v.append({
                'type':i.type,
                'chat':i.chat,
                'name':i.USER.name,
                'dtime':i.date,
                'tname':i.AGRICULTURE_OFFICE.name,
            })
        # print(v)
        return JsonResponse({"status": "ok", "data": v, "id": cc.id})
    else:
        return JsonResponse({"status": "error"})


#......................................................................................................USER module

def and_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].usertype
        res = user.objects.get(LOGIN=lid)
        name = res.name
        email = res.email
        return JsonResponse({"status":"ok","lid":lid,"type":type,"name":name,"email":email})
    else:
        return JsonResponse({"status":None})

def and_user_registration(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']

    data = login.objects.filter(username=email,password=password)
    if data.exists():
        return JsonResponse({"status":None})
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'user'
        log_obj.save()

        obj = user()
        obj.name = name
        obj.email = email
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({"status":"ok"})


def and_view_profile(request):
    lid = request.POST['lid']
    res = user.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","name":res.name,"place":res.place,"post":res.post,"pin_code":res.pin,
                         "email":res.email,"phone_no":res.contact})


def and_view_agriculture_office(request):
    res = agriculture_office.objects.all()
    ar =[]
    for i in res:
        ar.append(
            {
                "aid":i.id,
                "name":i.name,
                "email":i.email,
                "contact":i.contact,
                "latitude":i.latitude,
                "longitude":i.longitude
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def and_view_notification(request):
    res = notification.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "nid":i.id,
                "notification":i.notifications,
                "date":i.date
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_view_fertilizer(request):
    aid = request.POST['aid']
    res = fertilizer.objects.filter(AGRICULTURE_OFFICE=aid)
    ar = []
    for i in res:
        ar.append(
            {
                "fid":i.id,
                "name":i.name,
                "price":i.price,
                "details":i.details
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_view_reply(request):
    res = complaint.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "complaint":i.complaint,
                "date":i.date,
                "reply":i.reply,
                "reply_date":i.reply_date,
                "user_info":i.USER.name
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_send_complaint(request):
    complaints = request.POST['complaint']
    lid = request.POST['lid']
    obj = complaint()
    obj.complaint = complaints
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.reply = 'pending'
    obj.reply_date = 'pending'
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def and_view_success_story(request):
    aid = request.POST['aid']
    res = success_story.objects.filter(AGRICULTURE_OFFICE=aid)
    ar = []
    for i in res:
        ar.append(
            {
                "sid":i.id,
                "story":i.notes,
                "date":i.date,
                "name":i.AGRICULTURE_OFFICE.name,
                "email":i.AGRICULTURE_OFFICE.email
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_send_Feedback(request):
    feedbacks = request.POST['feedback']
    lid = request.POST['lid']
    obj = feedback()
    obj.feedback = feedbacks
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})


#......................ANDROID CHAT

def android_add_chat(request):
    lid = request.POST['lid']
    aid = request.POST['toid']
    message = request.POST['message']
    print(lid)
    print(aid)
    obj = chat()
    obj.chat = message
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.type = 'user'
    obj.USER = user.objects.get(LOGIN=lid)
    obj.AGRICULTURE_OFFICE_id = aid
    obj.save()

    return JsonResponse({"status":"Inserted"})

def android_view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    res = chat.objects.filter(Q(USER_id=user.objects.get(LOGIN_id=lid)),Q(id__gt=lastid))
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


def and_view_stock(request):
    aid = request.POST['aid']
    res = stock.objects.filter(AGRICULTURE_OFFICE=aid)
    ar = []
    for i in res:
        ar.append(
            {
                "stk_id":i.id,
                "name":i.name,
                "type":i.type,
                "price":i.price,
                "quantity":i.quantity,
                "image":i.image,
                "agri_name":i.AGRICULTURE_OFFICE.name,
                "contact":i.AGRICULTURE_OFFICE.contact
            }

        )
    return JsonResponse({"status":"ok","data":ar})

# ............CART..........................

def and_add_quantity(request):
    stk_id = request.POST['stk_id']
    lid = request.POST['lid']
    print(stk_id)
    print(lid)

    quantity = request.POST['quantity']
    res = cart.objects.filter(USER__LOGIN=lid,STOCK=stk_id)
    if res.exists():
        cart.objects.filter(id=res[0]).update(quantity=res[0].quantity + int(quantity))
        return JsonResponse({"status":"no"})
    else:
        obj = cart()
        obj. STOCK_id = stk_id
        obj.USER  = user.objects.get(LOGIN=lid)
        obj.quantity = quantity
        obj.save()
        return JsonResponse({"status":"ok"})


def and_view_cart(request):
    lid = request.POST['lid']
    res = cart.objects.filter(USER__LOGIN=lid)
    ar = []
    amount = 0
    t = 0
    for i in res:
        # stock_price = i.STOCK.price
        amount = int(i.quantity) * int(i.STOCK.price)
        t = int(t) + int(amount)
        print(t)
        ar.append(
            {
                "cart_id":i.id,
                "stock_name":i.STOCK.name,
                "type":i.STOCK.type,
                "price":i.STOCK.price,
                "image":i.STOCK.image,
                "name":i.USER.name,
                "contact":i.USER.contact,
                "officer_name":i.STOCK.AGRICULTURE_OFFICE.name,
                "officer_contact":i.STOCK.AGRICULTURE_OFFICE.contact,
                "quantity":i.quantity
            }
        )

    return JsonResponse({"status":"ok","data":ar,"amount":amount,'t':t})

def and_offline_payment(request):
    mode = request.POST['mode']
    lid = request.POST['lid']
    amount = request.POST['amount']

    officer_list = []
    data = cart.objects.filter(USER__LOGIN=lid)
    for i in data:
        officer_id = i.STOCK.AGRICULTURE_OFFICE_id
        if officer_id not in officer_list:
            officer_list.append(officer_id)

    for j in officer_list:
        data1 = orders.objects.filter(AGRICULTURE_OFFICE=str(j),USER__LOGIN=lid,payment_status='pending')
        if data1.exists():
            order_id = data1[0].id
            data2 = cart.objects.filter(USER__LOGIN=lid,STOCK__AGRICULTURE_OFFICE=j)
            for k in data2:
                obj1 = order_sub()
                obj1.STOCK_id = k.STOCK_id
                obj1.ORDERS_id = order_id
                obj1.quantity = k.quantity
                obj1.save()
        else:
            data3 = cart.objects.filter(USER__LOGIN=lid,STOCK__AGRICULTURE_OFFICE=j)
            obj = orders()
            obj.USER = user.objects.get(LOGIN=lid)
            obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
            obj.payment_status = 'offline'
            obj.amount = 0
            obj.AGRICULTURE_OFFICE_id = j
            obj.save()
            total_amount = 0
            order_id = obj.id
            for r in data3:

                orders.objects.get(id=order_id)
                # amounts = data4.amount
                total_amount += int(r.quantity)*int(r.STOCK.price)
                print(total_amount,"hiii")
                obj1 = order_sub()
                obj1.STOCK_id = r.STOCK_id
                obj1.ORDERS = obj
                obj1.quantity = r.quantity
                obj1.save()

                new_stock_quantity = int(r.STOCK.quantity)-int(r.quantity)
                stock.objects.filter(id=r.STOCK.id).update(quantity=new_stock_quantity)

            orders.objects.filter(id=order_id).update(amount=total_amount)
            print(orders.objects.filter(id=order_id).update(amount=total_amount))


    # orders.objects.filter(USER__LOGIN=lid).update(payment_status=mode)
    cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status":"ok"})

def android_online_payment(request):
    mode = request.POST['mode']
    lid = request.POST['lid']
    amount = request.POST['amount']

    officer_list = []
    data = cart.objects.filter(USER__LOGIN=lid)
    for i in data:
        officer_id = i.STOCK.AGRICULTURE_OFFICE_id
        if officer_id not in officer_list:
            officer_list.append(officer_id)

    for j in officer_list:
        data1 = orders.objects.filter(AGRICULTURE_OFFICE=str(j),USER__LOGIN=lid,payment_status='pending')
        if data1.exists():
            order_id = data1[0].id
            data2 = cart.objects.filter(USER__LOGIN=lid,STOCK__AGRICULTURE_OFFICE=j)
            for k in data2:
                obj1 = order_sub()
                obj1.STOCK_id = k.STOCK_id
                obj1.ORDERS_id = order_id
                obj1.quantity = k.quantity
                obj1.save()
        else:
            data3 = cart.objects.filter(USER__LOGIN=lid,STOCK__AGRICULTURE_OFFICE=j)
            obj = orders()
            obj.USER = user.objects.get(LOGIN=lid)
            obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
            obj.payment_status = 'online'
            obj.amount = 0
            obj.AGRICULTURE_OFFICE_id = j
            obj.save()
            total_amount = 0
            order_id = obj.id
            for r in data3:

                orders.objects.get(id=order_id)
                # amounts = data4.amount
                total_amount += int(r.quantity)*int(r.STOCK.price)
                print(total_amount,"hiii")
                obj1 = order_sub()
                obj1.STOCK_id = r.STOCK_id
                obj1.ORDERS = obj
                obj1.quantity = r.quantity
                obj1.save()
                new_stock_quantity = int(r.STOCK.quantity)-int(r.quantity)
                stock.objects.filter(id=r.STOCK.id).update(quantity=new_stock_quantity)

            orders.objects.filter(id=order_id).update(amount=total_amount)
            print(orders.objects.filter(id=order_id).update(amount=total_amount))


    cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status":"ok"})


def and_cart_cancel(request):
    cart_id = request.POST['cart_id']
    cart.objects.get(id=cart_id).delete()
    return JsonResponse({"status":"ok"})

#...........................................................................

def and_view_orders(request):
    lid = request.POST['lid']
    res = order_sub.objects.filter(Q(ORDERS__payment_status='online')|Q(ORDERS__payment_status='offline'),ORDERS__USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "order_id": i.id,
                "stock_name":i.STOCK.name,
                "stock_image":i.STOCK.image,
                "amount":i.ORDERS.amount,
                "date":i.ORDERS.date,
                "name":i.STOCK.AGRICULTURE_OFFICE.name,
                "contact":i.STOCK.AGRICULTURE_OFFICE.contact,
                "quantity":i.quantity
            }
        )

    return JsonResponse({"status":"ok","data":ar})







