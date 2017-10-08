from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# @csrf_exempt
@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    INdex and Create
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """
        Retrieve, update, delete
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serialize.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BED_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)
