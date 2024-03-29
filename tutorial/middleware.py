from django.conf import settings
from django.shortcuts import redirect
import re
from django.urls import reverse
from django.contrib.auth import logout

EXEMPT_URL = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URL'):
    EXEMPT_URL += [re.compile(url) for url in settings.LOGIN_EXEMPT_URL]
print(EXEMPT_URL)

class RequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        print(path)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URL)
        if path == reverse('tutorial:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)











