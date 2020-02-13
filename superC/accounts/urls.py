from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('account_info/',views.AccountView.as_view(),name='account_info'),
    path('account_info_list',views.AccountListView.as_view(),name='account_list'),
    path('account_info_list/<int:pk>/',views.AccountDetailView.as_view(),name='detail_account'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('<int:pk>/edit_personal/',views.AccountUpdatePersonalView.as_view(),name='update_personal'),
    path('<int:pk>/edit_medals/',views.AccountUpdateMedalsView.as_view(),name='update_medals'),
    path('<int:pk>/edit_trophies/',views.AccountUpdateTrophiesView.as_view(),name='update_trophies'),
    path('<int:pk>/edit_stickers/',views.AccountUpdateStickersView.as_view(),name='update_stickers'),
    path('<int:pk>/edit_roadmap/',views.AccountUpdateRoadmapView.as_view(),name='update_roadmap'),
    path('messages/',views.messages_list,name='messages_list'),
    path('messages/<int:pk>/',views.messages_content,name='messages_list_content'),
    path('messages/create/',views.messages_new,name='message_create'),
]
