# views.py
from django.shortcuts import render
import json
from user_model.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from UserService import service
from user_model.serializers import *

# View để đăng ký người dùng
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Kiểm tra dữ liệu trước khi cập nhật
        validation_errors = {}
        validation_errors = service.validate_data(data)
        check_password = service.check_password(data.get('password'), data.get('confirm_password'))
        if check_password != "":
            validation_errors['password'] = check_password
        if validation_errors:
            return JsonResponse(
                {'status'     : 'Failed',
                 'status_code': '400',
                 'message'    : validation_errors
                 }, status=400)

        # Kiểm tra sự tồn tại của username, email và phone
        existing_data = service.check_existing_data(data)
        if existing_data:
            return JsonResponse(
                {'status'     : 'Failed',
                 'status_code': '400',
                 'message'    : existing_data
                 }, status=400)

        try:
            # Tạo các đối tượng mới: Address, NameUser, Account, User
            address = Address.objects.create()
            name_user = NameUser.objects.create(
                fullname=data.get('lname') + ' ' + data.get('fname'),
                fname=data.get('fname'),
                lname=data.get('lname')
            )
            account = Account.objects.create(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
            )
            user = User.objects.create(
                account=account,
                address=address,
                name_user=name_user,
                phone=data.get('phone')
            )
            return JsonResponse(
                {
                    'status'     : 'Success',
                    'status_code': '200',
                    'message'    : 'User created successfully!',
                })
        except Exception as e:
            return JsonResponse(
                {
                    'status': 'Failed',
                    'status_code': '400',
                    'message': f"Failed to create user: {str(e)}"
                }, status=400)

# View để đăng nhập
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        try:
            # Kiểm tra sự tồn tại của tài khoản với username và password tương ứng
            account = Account.objects.get(username=username, password=password)
            user = account.user

            # Trả về thông tin của người dùng và tài khoản trong trường hợp đăng nhập thành công
            return JsonResponse(
                {
                    'status'     : 'Success',
                    'status_code': '200',
                    'message'    : 'Login successful!',
                    'data'       :
                        {
                            'user'     : UserSerializer(user).data,
                            'account'  : AccountSerializer(account).data,
                            'name_user': NameUserSerializer(user.name_user).data,
                            'address'  : AddressSerializer(user.address).data,
                        }
                })
        except Account.DoesNotExist:
            # Trả về thông báo lỗi nếu tài khoản không tồn tại hoặc thông tin đăng nhập không chính xác
            return JsonResponse({'status': 'Failed', 'status_code': '400', 'message': "Invalid username or password."}, status=400)
