from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from user.models import user
from photographer.models import photographer
from other.models import other
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.files import File
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
    find_user = user.objects.get(user_name=username)
    if request.method == 'POST':
        img = request.POST['img']
        try:
            savepath = os.path.join(settings.MEDIA_ROOT,username)
            with open(savepath,"wb") as f:
                save_icon = File(f)
                save_icon.write(img)
                print("saved")
            find_user.pic = savepath
            find_user.save()
        except:
            return HttpResponse("icon update failed")
    return HttpResponse("icon updated")

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
