# users/views.py
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import UserDetails

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = UserDetails(**data)
            user.save()
            return JsonResponse({'message': 'User added successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UserListView(View):
    def get(self, request):
        users = UserDetails.objects()
        data = []
        for user in users:
            data.append({
                'name': user.name,
                'email': user.email,
                'mobile': user.mobile,
                'address': user.address
            })
        return JsonResponse(data, safe=False, status=200)
