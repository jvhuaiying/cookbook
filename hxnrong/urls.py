from django.urls import path
from . import views

urlpatterns = [
    path('xzcpu', views.xzcpu),
    path('xzcpunrong', views.xzcpunrong),
    path('cpxze', views.cpxze),
    path('hqcplbiao', views.hqcplbiao),
    path('hqcliao', views.hqcliao),
    path('clqdan', views.clqdan),
    path('getclqdan', views.getclqdan),
    path('chaocaiymian', views.chaocaiymian),
    path('kschaocai', views.kschaocai),
    path('hqbuzhou', views.hqbuzhou),
    path('yjrcpuljie', views.yjrcpuljie),
    path('yxzcpsjkschuang', views.yxzcpsjkschuang),
    # 输入框实时检索
    path('ssjsuo', views.ssjsuo),
    # 管理
    path('', views.gli),
    # 菜谱管理
    path('cpgli', views.cpgli),
    path('hqbucp', views.hqbucp),
    path('hqbucp1', views.hqbucp1),
    path('bjcpu1', views.bjcpu1),
    path('cpglxzcpu', views.cpglxzcpu),
    path('cpglbji', views.cpglbji),
]