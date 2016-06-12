from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect

# Default logout view

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
