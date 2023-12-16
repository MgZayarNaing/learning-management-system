from .imports import *
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def PermissionIndex(request):
    try:
        permission = PermissionModel.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(permission, request)
        seri = PermissionSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def PermissionStore(request):
    seri = PermissionSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def PermissionShow(request, pk):
    try:
        permission = PermissionModel.objects.get(pk=pk)
        seri = PermissionSerializer(permission)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def PermissionUpdate(request, pk):
    try:
        permission = PermissionModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = PermissionSerializer(permission, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def PermissionDelete(request, pk):
    try:
        permission = PermissionModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    permission.delete()
    return Response({"message":"Deleted Successfully"},status=200)