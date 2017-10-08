from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# from rest_framework import mixins
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreatModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#


    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #         serializer = SnippetSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     generics.GenericAPIView):
#
#     """
#         Retrieve, update, delete
#     """
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     #
    # def get_object(self, pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # def get(self,request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serialize.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BED_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return HttpResponse(status=HTTP_204_NO_CONTENT)
