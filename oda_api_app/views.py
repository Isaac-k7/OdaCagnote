from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payement
from .serializers import PayementSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView


# Create your views here.
'''
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer

class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer
'''

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_payements': 'payements/',
		'Add': 'payements/create',
		'Update': 'payements/update/id',
		'Delete': 'payements/id/delete'
	}
	return Response(api_urls)


@api_view(['POST'])
def add_payments(request):
	payment = PayementSerializer(data=request.data)

	# validating for already existing data
	if Payement.objects.filter(**request.data).exists():
		return Response({"status":"400"})

	try:
		if payment.is_valid():
			payment.save()
			return Response({"status":"200"})
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)
	except:
		return Response({"status":"400"})


class ListPayementAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Payement.objects.all()
    serializer_class = PayementSerializer



@api_view(['POST'])
def update_payments(request, id):
	payment = Payement.objects.get(id=id)
	datas = PayementSerializer(instance=payment, data=request.data)

	if datas.is_valid():
		datas.save()
		return Response(datas.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_payments(request, id):
	payment = get_object_or_404(Payement, id=id)
	payment.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
