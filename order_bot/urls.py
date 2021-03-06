"""order_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from order.views import new_order, follow
from slack_api.views import new_order_in#, follow_in


urlpatterns = [
    path('admin/', admin.site.urls),

    path('new_order', new_order),
    path('new_order/', new_order),

    path('follow', follow),
    path('follow/', follow),

    path('slack/new_order', new_order_in),
    path('slack/new_order/', new_order_in),

    # path('slack/follow', follow_in),
    # path('slack/follow/', follow_in),
]
