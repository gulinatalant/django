from django.http import Http404
from rest_framework.decorators import api_view

from .models import Category, Post, Tag
from .serializers import CategorySerializer, TagSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=200)
    except Category.DoesNotExist:
        return Response(f'This category with pk {pk} does not exist!', status=204)


@api_view(['PUT'])
def category_update(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(
            instance=category,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)
    except Category.DoesNotExist:
        return Response('category nooot found', status=204)


@api_view(['PATCH'])
def category_patch(requests, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=requests.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)
    except Category.DoesNotExist:
        return Response(f'category with {pk} not found!', status=204)


@api_view(['DELETE'])
def category_delete(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(
            'Category successfully deleted',
            status=204
        )
    except Category.DoesNotExist:
        return Response('not found', status=404)


class TagListCreateView(APIView):
    def get(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TagDetailView(APIView):
    def get_object(self, pk):
        try:
            return Tag.objects.get(id=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        tag = self.get_object(pk)
        serializer = TagSerializer(
            instance=tag,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)

    def delete(self, request, pk):
        tag = self.get_object(pk)
        tag.delete()
        return Response(
            'Successfully deleted',
            status=204
        )


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


