from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path(
        'create-category/',
        views.create_event_category,
        name='create_event_category'
    ),

    path(
        'category-list/',
        views.category_list,
        name='category_list'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    path(
    'edit-category/<int:id>/',
    views.edit_category,
    name='edit_category'
),
]