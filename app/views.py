from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client, PointsHistoric
from .serializers import ClientSerializer, PointsHistoricSerializer


class InsertAPIView(APIView):
    """
    Programa de Pontos Ameixa
    """
    def get(self, request):
        company = Client.objects.all()
        serializer = ClientSerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        company = Client.objects.filter(company=data['company']).first()
        points_to_add = data['earned_points'] - data['spent_points']
        if company:
            company.balance += points_to_add
        else:
            company = Client()
            company.company = data['company']
            company.balance = points_to_add
        company.save()
        points = PointsHistoric()
        points.earned_points = data['earned_points']
        points.spent_points = data['spent_points']
        points.client_id = company.id
        points.save()
        return Response(status=200)

    def put(self, request):
        data = request.data
        company = Client.objects.filter(company=data['company']).first()
        if not company:
            return Response(status=404)
        points_to_add = data['earned_points'] - data['spent_points']
        company.balance += points_to_add
        company.save()
        points = PointsHistoric()
        points.earned_points = data['earned_points']
        points.spent_points = data['spent_points']
        points.client = company.id
        points.save()
        return Response(status=204)


    def delete(self, id):
        try:
            Client.objects.get(id=id).delete()
            return Response(status=204)
        except Exception as error:
            return Response(error, status=404)


class ResultAPIView(APIView):
    def get(self, request, id):
        try:
            company_points = PointsHistoric.objects.filter(client_id=id).all()
            data = PointsHistoricSerializer(company_points, many=True).data
            return Response(data, status=201)
        except Exception as error:
            return Response(error, status=404)

    # def get(self, request, id):
        

# class ResultPartialAPIView(APIView)
#     def get(self, request, id):
#         try:
#             company = Insert.objects.get(id=id)



# class InsertList(generics.ListAPIView):