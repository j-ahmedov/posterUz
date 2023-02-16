from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.db.models import ProtectedError


class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            posts = Post.objects.all()
            return Response({'posts': PostSerializer(posts, many=True).data})

        try:
            post = Post.objects.filter(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Object doesn't exist"})

        return Response({"posts": PostSerializer(post, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not allowed to this url"})

        try:
            instance = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Object doesn't exist"})

        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed to this url"})

        try:
            Post.objects.filter(pk=pk).delete()
        except ProtectedError:
            return Response({"error": "Object can't be deleted"})

        return Response({"post": f"deleted post {pk}"})

