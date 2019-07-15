from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseView)
router.register('category', views.CategoryView)
router.register('contacts', views.ContactView)
router.register('branches', views.BranchesView)





urlpatterns = [
    path('', include(router.urls)),
    re_path(
        r'^course/(?P<pk>[0-9]+)$',
        views.get_delete_update_course,
        name='get_delete_update_course'
    ),
    re_path(
        r'^course/$',
        views.get_post_course,
        name='get_post_course'
    )
]
