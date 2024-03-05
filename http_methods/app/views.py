from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class DeptJsonData(APIView):
    def get(self,request,id):
        if id == 'all':
            DMO = Dept.objects.all()
            DJO = DeptModelSerializer(DMO,many = True)
            return Response(DJO.data)
        else:
            DMO = Dept.objects.get(deptid = id)
            DJO = DeptModelSerializer(DMO)
            return Response(DJO.data)
    # We can post multiple data at a time generally
    def post(self,request,id):
        DPO = request.data
        if id == 'all':
            DDS = DeptModelSerializer(data=DPO,many = True)
        else:
            DDS = DeptModelSerializer(data = DPO)
        if DDS.is_valid():
            DDS.save()
            return Response({"post":'Success'})
        return Response({'post':'Denied'})
    # Can put(update) one row (orm obj) at a time (need to specify all fields while updation of any or all fields)
    def put(self,request,id):
            if id != 'all':
                DMO = Dept.objects.get(deptid = id)
                DJO = DeptModelSerializer(DMO,request.data)
                if DJO.is_valid():
                    DJO.save()
                    return Response({'put':'Success'})
                return Response({'put':'Denied'})
            return Response({'put':'Denied'})
    # Can patch(update) one row (orm obj) at a time(specific fields updation)
    def patch(self,request,id):
            if id != 'all':
                DMO = Dept.objects.get(deptid = id)
                DJO = DeptModelSerializer(DMO,request.data,partial = True)
                if DJO.is_valid():
                    DJO.save()
                    return Response({'patch':'success'})
                return Response({'patch':'Denied'})
            return Response({'patch':'Denied'})
    def delete(self,request,id):
         if id != 'all':
              DMO = Dept.objects.filter(deptid = id).delete()
              return Response({'Delete':'Success'})
         else:
              DMO = Dept.objects.all().delete()
              return Response({'Delete':'Denied'})




     
              
    










