from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from login.models import user
from django.core.exceptions import ObjectDoesNotExist
import json


def login(request):
    get_username = request.GET['username']
    get_password = request.GET['password']
    find_user = user.objects.get(user_name=get_username)
    print(get_password + " " + find_user.user_password)
    try:
        if check_password(get_password, find_user.user_password):
            response = {
                "error_code": 10000,
                "message": "success",
                "data": {
                    "user_id": find_user.id,
                    "group_id": find_user.group_id,
                    # "small_pic": find_user.small_pic,
                    "address_id": find_user.address_id,
                    "usercomment_id": find_user.usercomment_id,
                }
            }
            return HttpResponse(json.dumps(response), content_type="application/json")
        elif get_username is None or get_password is None:
            response = {
                "error_code": 10001,
                "message": "error",
            }
            return HttpResponse(json.dumps(response), content_type="application/json")
        elif not check_password(get_password, find_user.user_password):
            response = {
                "error_code": 10000,
                "message": "wrong password",
            }
            return HttpResponse(json.dumps(response), content_type="application/json")
    except ObjectDoesNotExist:
        response = {
            "error_code": 40004,
            "message": "error",
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
