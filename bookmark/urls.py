from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BookmarkListV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetailV.as_view(), name='detail')

    """
        정규표현식의 괄호는 그룹. 위의 괄호사이에 값은 이 패턴에서 어떤 키캆이 들어갈 것인지 결정해주는 정규표현식.
        ^는 시작 $는 끝을 의미
    """
]
