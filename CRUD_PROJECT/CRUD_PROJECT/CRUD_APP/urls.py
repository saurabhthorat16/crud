from django.urls import path
from . import views

urlpatterns = [
    path('st/', views.studentView, name='stuformurl'),
    path('fe/', views.feeView, name='feeformurl'),
    path('ss/', views.showStudentView, name='studataurl'),
    path('fs/', views.showFeeView, name='feesdataurl'),
    path('us/<int:id>/', views.updateStudentView, name='updatestuurl'),
    path('uf/<int:id>/', views.updateFeeView, name='updatefeeurl'),
    path('ds/<int:id>/', views.deleteStudentView, name='deletestuurl'),
    path('df/<int:id>/', views.deleteFeeView, name='deletefeeurl'),
]