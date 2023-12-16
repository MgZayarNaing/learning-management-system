from .imports import *
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def RolesIndex(request):
    try:
        roles = RolesModel.objects.all()
        paginator = CustomPagination()
        page_obj = paginator.paginate_queryset(roles, request)
        seri = RolesSerializer(page_obj, many=True)
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def RolesStore(request):
    seri = RolesSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def RolesShow(request, pk):
    try:
        roles = RolesModel.objects.get(pk=pk)
        seri = RolesSerializer(roles)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
def RolesUpdate(request, pk):
    try:
        roles = RolesModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    seri = RolesSerializer(roles, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def RolesDelete(request, pk):
    try:
        roles = RolesModel.objects.get(pk=pk)
    except Exception:
        return Response({"errors":"Post Not Found!"}, status=204)
    roles.delete()
    return Response({"message":"Deleted Successfully"},status=200)