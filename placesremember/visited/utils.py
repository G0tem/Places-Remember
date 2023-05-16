menu = [{"title": 'Places Remember', 'url_name': 'home'},
        {"title": 'Добавить воспоминание', 'url_name': 'addpost'},
        {"title": 'Войти с помощью Google', 'url_name': 'login'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
                user_menu.pop(1)

        context['menu'] = user_menu
        return context