from django.core.validators import validate_email
from accounts.models import User
from django.contrib.auth.hashers import check_password

def validate_signup(signup_data):
    username = signup_data.get('username')
    password = signup_data.get('password')
    nickname = signup_data.get('nickname')
    birth = signup_data.get('birth')
    first_name = signup_data.get('first_name')
    last_name = signup_data.get('last_name')
    email = signup_data.get('email')

    err_msg_list = []

    # validate username
    if len(username) < 5 or len(username) > 20:
        err_msg_list.append({'username': 'username은 5~20자로 입력하세요.'})
    if User.objects.filter(username=username).exists():
        err_msg_list.append({'username': '이미 존재하는 username 입니다.'})

    # validate nickname
    if len(nickname) > 20:
        err_msg_list.append({'nickname': 'nickname은 20자 이하로 입력하세요'})
    if User.objects.filter(nickname=nickname).exists():
        err_msg_list.append({'nickname': '이미 존재하는 nickname 입니다.'})

    # validate email
    try:
        validate_email(email)
    except:
        err_msg_list.append({'email': '올바른 email형식을 입력해주세요.'})

    if err_msg_list:
        return False, err_msg_list
    else:
        return True, err_msg_list


def validate_password_change(user, current_password, new_password):
    err_msg_list = []

    # Check if current password matches
    if not check_password(current_password, user.password):
        err_msg_list.append({"current_password": "현재 비밀번호가 올바르지 않습니다."})

    # Add additional password validation if necessary (e.g., length, complexity)

    if err_msg_list:
        return False, err_msg_list
    return True, err_msg_list
