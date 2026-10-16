from django.urls import path

from employee import views

urlpatterns=[
    # path('',views.home)
    path("set-password/<uidb64>/<token>/",views.set_password,name='set_password'),
path("dashboard/",views.employee_dashboard,name="employee_dashboard"),
    path("profile/",views.my_profile,name='my_profile'),
    path("apply-leave/",views.apply_leave,name='apply_leave'),
    path("my-leaves/",views.my_leaves,name='my_leaves'),
path("leave_calendar/", views.leave_calendar, name="leave_calendar"),

]