from .imports import *
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def FilesIndex(request):
    try:
        files = FilesModel.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(files, request)
        seri = FilesSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def FilesStore(request):
    seri = FilesSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def FilesShow(request, pk):
    try:
        files = FilesModel.objects.get(pk=pk)
        seri = FilesSerializer(files)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def FilesUpdate(request, pk):
    try:
        files = FilesModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = FilesSerializer(files, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def FilesDelete(request, pk):
    try:
        files = FilesModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    files.delete()
    return Response({"message":"Deleted Successfully"},status=200)