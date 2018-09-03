from django.contrib.auth.decorators import login_required
from kolibree_notif_API.utils import JSONResponse
from rest_framework.views import APIView
from devices.models import Device
from rest_framework import authentication, permissions

class AccountView(APIView):

    def get(self, request, account_id, profile_id):
        try:
            device = Device.objects.get(account_id=account_id, profile_id=profile_id)
        except Device.DoesNotExist:
            device = Device.objects.create(account_id=account_id, profile_id=profile_id, reg_id=request.data.get('reg_id'), dev_id=request.data.get('dev_id'))
        else:
            return JSONResponse(device.to_dict(), status=200)

    def post(self, request, account_id, profile_id):
        try:
            device = Device.objects.get(account_id=account_id, profile_id=profile_id)
        except Device.DoesNotExist:
            device = Device.objects.create(account_id=account_id, profile_id=profile_id, reg_id=request.data.get('reg_id'), dev_id=request.data.get('dev_id'))
        else:
            return JSONResponse({}, status=401)
        return JSONResponse(device.to_dict(), status=200)

class NotificationsView(APIView):

    def post(self, request):
        message = request.data.get('message')
        picture = request.data.get('picture')
        accounts = request.data.get('accounts')

        device = Device.objects.filter(account_id__in=accounts, reg_id__isnull=False)

        dict_ = {key: value for key, value in request.data.items() if key in ('message', 'picture')}

        s = device.send_message(dict_)
        print (s)

        return JSONResponse({}, status=204)
