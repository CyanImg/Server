from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from user.models import user
from django.core.exceptions import ObjectDoesNotExist
import json


def sendPic(pic):
    return HttpResponse(pic, content_type="image/png")


def login(request):
    get_username = request.GET['username']
    get_password = request.GET['password']
    try:
        try:
            find_user = user.objects.get(user_name=get_username)
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
                sendPic(find_user.small_pic)
            elif get_username is None or get_password is None:
                response = {
                    "error_code": 10001,
                    "message": "blank username or password",
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
            response = {
                "error_code": 10000,
                "message": "user created",
            }
    except:
        response = {
            "error_code": 20000,
            "message": "service not available",
        }
    return HttpResponse(json.dumps(response), content_type="application/json")
