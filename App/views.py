from django.shortcuts import render
from django.db.models import Sum 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import StudentInfo, TimeTable, Income
from .serializers import StudentInfoSerializer, TimeTableSerializer, IncomeSerializer

# Students Info... API
@api_view(['GET', 'POST'])
def student_list_create(request):
    try:
        if request.method == 'GET':
            students = StudentInfo.objects.all().order_by('-created_at')
            serializer = StudentInfoSerializer(students, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = StudentInfoSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Student update-delete.......API
@api_view(['PUT', 'DELETE'])
def student_update_delete(request, pk):
    try:
        student = StudentInfo.objects.get(pk=pk)
    except StudentInfo.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'PUT':
            serializer = StudentInfoSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            student.delete()
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Timetable... API
@api_view(['GET', 'POST'])
def timetable_list_create(request):
    try:
        if request.method == 'GET':
            timetable = TimeTable.objects.all()
            serializer = TimeTableSerializer(timetable, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'POST':
            serializer = TimeTableSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(
            {"error": str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Income ...... API
@api_view(['GET', 'POST'])
def income(request):
    try:
        if request.method == 'GET':

            income = Income.objects.all()

            fees = StudentInfo.objects.aggregate(total = Sum('fees'))['total'] or 0

            serializer = IncomeSerializer(income, many = True)

            persentage = 25
            result = (fees / 100) * 25

            return Response(
                {
                "total_fees":fees, 
                "percentage": persentage, 
                "income_amount": result, 
                "payments": serializer.data, 
                }, 
                status = status.HTTP_200_OK)
        
        elif request.method == 'POST': 
            serializer = IncomeSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(
            {"error": str(e)},
            status = status.HTTP_500_INTERNAL_SERVER_ERROR
        )
