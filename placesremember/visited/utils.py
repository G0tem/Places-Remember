menu = [{'title': 'Places Remember', 'url_name': 'home'},
        {'title': 'Добавить воспоминание', 'url_name': 'addpost'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            context['avatar'] = self.request.user.socialaccount_set.first().get_avatar_url()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
                user_menu.pop(1)
        context['menu'] = user_menu
        return context