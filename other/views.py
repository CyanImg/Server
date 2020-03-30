from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from other.models import other
from django.core.exceptions import ObjectDoesNotExist
import json


def sendPic(pic):
    return HttpResponse(pic, content_type="image/png")


def login(request):
    get_email = request.GET['email']
    get_password = request.GET['password']
    response = {
        "error_code": 20000,
        "message": "service not available",
    }
    try:
        try:
            find_user = other.objects.get(email=get_email)
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
    get_identification = request.GET.get('identification',None)
    get_experience = request.GET.get('experience',None)
    get_album = request.GET.get('album',None)
    get_device = request.GET.get('device',None)
    try:
        if other.objects.filter(other_name=get_username).count() > 0:
            response = {
                "error_code": 10000,
                "message": "user already exists",
            }
        elif other.objects.filter(other_name=get_username).count() == 0:
            other.objects.create(other_name=get_username, other_password=make_password(get_password),
                                        other_school=get_schoolname,
                                        email=get_email,other_identification=get_identification,
                                        experience=get_experience,album=get_album,other_device=get_device)
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
