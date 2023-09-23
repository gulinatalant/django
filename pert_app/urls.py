from django.urls import path
from .views import (category_list, category_create,category_detail,
                    category_update,category_patch, category_delete,TagListCreateView,TagDetailView,
                    PostListCreateView,PostDetailView, CategoryDetailView,CategoryListCreateView)


urlpatterns = [
    path('categories/', category_list),
    path('category-create/', category_create),
    path('categories/<int:pk>/', category_detail),
    path('category_update/<int:pk>/', category_update),
    path('category_delete/<int:pk>/', category_delete),
    path('category_patch/<int:pk>/', category_patch),
    path('tags/', TagListCreateView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),

]
