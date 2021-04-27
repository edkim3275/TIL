from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response  # 이전의 render
from rest_framework.decorators import api_view  # 이전의 require_http_methods
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # request.POST => HTML FormData 로 넘어온 데이터만 취급
        # request.GET => URL parmas (/?key1=value1&key2=value2)
        # request.data => 사용자가 제출한 JSON 데이터는 여기에!
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=400) => raise_exception=True 옵션이 대체


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {  # cutomize message
            'success': True,
            'message': f'{article_pk} 번 게시글이 삭제되었습니다.',
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_comment(reqeust, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=reqeust.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        comment.delete()
        data = {  # cutomize message
            'success': True,
            'message': f'{comment_pk} 번 댓글이 삭제되었습니다.',
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
