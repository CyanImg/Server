from smtplib import SMTPServerDisconnected
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from user.models import user,comments,order,make_forget_code
from photographer.models import photographer
from other.models import other
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.files import File
from django.utils.timezone import now
from django.core.mail import send_mail
from server.settings import EMAIL_FROM
import json
import os


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def sendPic(pic):
    return HttpResponse(pic, content_type="image/png")


def getPic(request):
    username = request.POST['username']
    try:
        find_user = user.objects.get(user_name=username)
    except ObjectDoesNotExist:
        return HttpResponse("No such user")
    if request.method == 'POST':
        img = request.POST['img']
        try:
            savepath = os.path.join(settings.MEDIA_ROOT,username)
            with open(savepath,"w") as f:
                save_icon = File(f)
                save_icon.write(img)
                print("saved")
            find_user.pic = username
            find_user.save()
        except:
            return HttpResponse("icon update failed")
        return HttpResponse("icon updated")
    else:
        return HttpResponse("only POST is accepted")


def login(request):
    get_email = request.GET['email']
    get_password = request.GET['password']
    response = {
        "error_code": 20000,
        "message": "service not available",
    }
    try:
        try:
            find_user = user.objects.get(email=get_email)
            if check_password(get_password, find_user.user_password):
                response = {
                    "error_code": 10000,
                    "message": "success",
                    "data": {
                        "user_id": find_user.id,
                        "group_id": find_user.group_id,
                        "address_id": find_user.address_id,
                        "usercomment_id": find_user.usercomment_id,
                    }
                }
                # sendPic(find_user.small_pic)
            elif get_email is None or get_password is None:
                response = {
                    "error_code": 10001,
                    "message": "blank email or password",
                }
            elif not check_password(get_password, find_user.user_password):
                response = {
                    "error_code": 10000,
                    "message": "wrong password",
                }
        except ObjectDoesNotExist:
            response = {
                "error_code": 40004,
                "message": "user not found",
            }
    except:
        response = {
            "error_code": 20000,
            "message": "service not available",
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def register(request):
    get_username = request.GET['username']
    get_password = request.GET['password']
    get_schoolname = request.GET['schoolname']
    get_email = request.GET['email']
    try:
        if user.objects.filter(user_name=get_username).count() > 0:
            response = {
                "error_code": 10000,
                "message": "user already exists",
            }
        elif user.objects.filter(user_name=get_username).count() == 0:
            user.objects.create(user_name=get_username, user_password=make_password(get_password),
                                user_school=get_schoolname,
                                email=get_email)
            find_user = user.objects.get(user_name=get_username)
            verify_code = find_user.verify_code
            try:
                title = "您的邮箱正在被用于注册CyanImg"
                body = "点击以下链接来验证您的邮箱"+"http://47.103.117.214:65535/api/user/verify?username="+get_username+"&verify="+verify_code
                if send_mail(title, body, EMAIL_FROM, [get_email]) == 1:
                    response = {
                        "error_code": 10000,
                        "message": "email sent"
                    }
                else:
                    response = {
                        "error_code": 20000,
                        "message": "email not sent"
                    }
            except:
                response = {
                    "error_code": 20000,
                    "message": "service not available",
                }
    except:
        response = {
            "error_code": 20000,
            "message": "service not available",
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def send_forget_code(request):
    get_user = request.GET['user']
    find_user = user.objects.get(user_name=get_user)
    forget_code = find_user.forget_code
    mail = find_user.user_email
    try:
        title = "找回您的CyanImg密码"
        body = "使用以下救援代码来重设您的CyanImg密码:"+forget_code
        if send_mail(title,body,EMAIL_FROM,[mail]) == 1:
            response = {
                "error_code":10000,
                "message":"email sent"
            }
        else:
            response = {
                "error_code":20000,
                "message":"email not sent"
            }
    except SMTPServerDisconnected:
        response = {
            "error_code":20000,
            "message":"Connection unexpectedly closed"
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def verify(request):
    get_user = request.GET['user']
    get_verify_code = request.GET['verify']
    try:
        find_user = user.objects.get(user_name=get_user)
        verify_code = find_user.verify_code
        if get_verify_code == verify_code and not find_user.is_verified:
            find_user.is_verified = True
            find_user.save()
            response = {
                "error_code":10000,
                "message":"verified"
            }
        else:
            response = {
                "error_code":10000,
                "message":"incorrect verify code or verified"
            }
    except Exception as e:
        print(e)
        response = {
            "error_code":20000,
            "message":"service not available"
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def forget(request):
    get_user = request.GET['user']
    get_forget_code = request.GET['forget']
    new_password = request.GET['newpassword']
    find_user = user.objects.get(user_name=get_user)
    forget_code = find_user.forget_code
    if get_forget_code == forget_code:
        find_user.update(user_password=make_password(new_password))
        find_user.update(forget_code=make_forget_code())
        response = {
            "error_code":10000,
            "message":"password reset"
        }
    else:
        response = {
            "error_code":10000,
            "message":"incorrect code"
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def search(request):
    get_graphername = request.GET.get('graphername', None)
    get_schoolname = request.GET.get('schoolname', None)
    get_othername = request.GET.get('othername', None)

    if get_graphername is not None:
        try:
            find_photographer = photographer.objects.get(graph_name=get_graphername)
            response = {
                "error_code": 10000,
                "data": {
                    "graph_id": find_photographer.graph_id(),
                    "graphcomment_id": find_photographer.graphcomment_id,
                    "graph_name": find_photographer.graph_name,
                    "graph_school": find_photographer.graph_name,
                    "email": find_photographer.email,
                    # "graph_identification":find_photographer.graph_identification,
                    "experience": find_photographer.experience,
                    "last_login_time": str(find_photographer.last_login_time),
                },
                "message": "photographer found",
            }
        except ObjectDoesNotExist:
            find_photographer = photographer.objects.filter(graph_name__contains=get_graphername)
            if len(find_photographer) > 0:
                response = {"error_code": 10000, "datalist": {}}
                for i in find_photographer:
                    newdata = {str(i.graph_id()): {
                        "graph_id": i.graph_id(),
                        "graphcomment_id": i.graphcomment_id,
                        "graph_name": i.graph_name,
                        "graph_school": i.graph_name,
                        "email": i.email,
                        # "graph_identification":i.graph_identification,
                        "experience": i.experience,
                        "last_login_time": str(i.last_login_time),
                    }}
                    response['datalist'].update(newdata)
                response.update({"message": "photographer found"})
            else:
                response = {
                    "error_code": 10000,
                    "message": "no such photographer",
                }
            # sendPic(find_photographer.pic)
            # sendPic(find_photographer.album)

    else:
        if get_othername is not None:
            try:
                find_other = other.objects.get(other_name=get_othername)
                response = {
                    "error_code": 10000,
                    "data": {
                        "graph_id": find_other.graph_id(),
                        "graphcomment_id": find_other.graphcomment_id,
                        "graph_name": find_other.graph_name,
                        "graph_school": find_other.graph_name,
                        "email": find_other.email,
                        # "graph_identification":find_other.graph_identification,
                        "experience": find_other.experience,
                        "last_login_time": str(find_other.last_login_time),
                    },
                    "message": "photographer found",
                }
            except ObjectDoesNotExist:
                find_other = photographer.objects.filter(other_name__contains=get_graphername)
                if len(find_other) > 0:
                    response = {"error_code": 10000, "datalist": {}}
                    for i in find_other:
                        newdata = {str(i.graph_id()): {
                            "graph_id": i.graph_id(),
                            "graphcomment_id": i.graphcomment_id,
                            "graph_name": i.graph_name,
                            "graph_school": i.graph_name,
                            "email": i.email,
                            # "graph_identification":i.graph_identification,
                            "experience": i.experience,
                            "last_login_time": str(i.last_login_time),
                        }}
                        response['datalist'].update(newdata)
                    response.update({"message": "other found"})
                else:
                    response = {
                        "error_code": 10000,
                        "message": "no such other",
                    }
                # sendPic(find_other.pic)
                # sendPic(find_other.album)

    return HttpResponse(json.dumps(response), content_type="application/json")


def makeComment(request):
    get_user = request.GET['username']
    content = request.GET['content']
    u = user.objects.get(user_name=get_user)
    user_name = u.user_name
    user_school = u.user_school
    group_id = u.group_id
    try:
        comments.objects.create(group_id=group_id,user_name=user_name,user_school=user_school,comment_content=content)
        return HttpResponse("comment updated")
    except:
        return HttpResponse("error")


def makeOrder(request):
    get_user = request.GET['username']
    get_graph = request.GET['graphname']
    # order_time = now()
    total = request.GET['total']
    # update_time = now()
    # order_status = False
    # payment_status = False
    meet_time = request.GET['meettime']
    address = request.GET['address']
    tel = request.GET['tel']
    try:
        find_user = user.objects.get(user_name=get_user)
        find_photographer = photographer.objects.get(graph_name=get_graph)
        order.objects.create(user_name=find_user.user_name,graph_name=find_photographer.graph_name,total=total,update_time=now(),meet_time=meet_time,address=address,tel=tel,user_school=find_user.user_school,graph_school=find_photographer.graph_school)
        response = {
            "error_code": 10000,
            "message": "order added",
        }
    except ObjectDoesNotExist:
        response = {
            "error_code": 10000,
            "message": "no such user/grapher",
        }
    return HttpResponse(json.dumps(response), content_type="application/json")


def changeOrder(request):
    get_order = request.GET['order']
    get_total = request.GET['total']
    get_order_status = request.GET['status']
    get_payment_status = request.GET['paymentstatus']
    get_meet_time = request.GET['meettime']
    get_address = request.GET['address']
    get_tel = request.GET['tel']
    try:
        find_order = order.objects.get(order_id=get_order)
        if get_total is not None:
            find_order.total = get_total
        if get_order_status is not None:
            find_order.order_status = get_order_status
        if get_payment_status is not None:
            find_order.payment_status = get_order_status
        if get_meet_time is not None:
            find_order.meet_time = get_meet_time
        if get_address is not None:
            find_order.address = get_address
        if get_tel is not None:
            find_order.tel = get_tel
        find_order.save()
        response = {
            "error_code": 10000,
            "message": "order updated",
        }
    except ObjectDoesNotExist:
        response = {
            "error_code": 10000,
            "message": "no such order",
        }
    return HttpResponse(json.dumps(response), content_type="application/json")