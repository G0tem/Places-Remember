import os.path

import requests
from allauth import socialaccount
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount
from django.core.files.base import ContentFile, File
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_updated

from placesremember import settings
from visited.models import Profile


# @receiver(user_logged_in)
# def save_profile_picture(request, user, **kwargs):
#     u_id = user.id
#     a = SocialAccount.objects.get(user_id=u_id, provider='google')
#     b = a.extra_data["picture"]
#     if b:
#         avatar_name = user.username + '.png'
#         media_path = 'media\\users_avatars'
#         file_path = os.path.join(media_path, avatar_name)
#         with open(file_path, 'wb') as f:  # скачиваем и сохраняем фото в файл
#             response = requests.get(b)
#             f.write(response.content)
#         with open(file_path, 'rb') as f:  # создаем объект файла File из сохраненного файла
#             avatar_file = File(f)
#             # сохраняем файл в поле avatar

