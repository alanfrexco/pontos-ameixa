from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Insert
from .serializers import InsertSerializer


class InsertAPIView(APIView):
    """
    Programa de Pontos Ameixa
    """
    def get(self, request):
        company = Insert.objects.all()
        serializer = InsertSerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        company = Insert.objects.filter(company=data['company']).first()
        if company:
            company.earned_points += data['earned_points']
            company.spent_points += data['spent_points']
        else:
            company = Insert()
            company.company = data['company']
            company.earned_points = data['earned_points']
            company.spent_points = data['spent_points']
        company.save()
        return Response(status=200)

    def put(self, request, id):
        data = request.data
        earned_points = data.get("earned_points")
        spent_points = data.get("spent_points")
        cash_back = Insert.objects.get(id=id)
        if earned_points:
            cash_back.earned_points += earned_points
        if spent_points:
            cash_back.spent_points += spent_points
        cash_back.save()
        return Response(status=204)


    def delete(self, request, id):
        try:
            Insert.objects.get(id=id).delete()
            return Response(status=204)
        except Exception as error:
            return Response(error, status=404)


class ResultAPIView(APIView):
    def get(self, request, id):
        try:
            company = Insert.objects.get(id=id)
            total = company.earned_points - company.spent_points
            return Response({
                "total": total
            }, status=201)
        except Exception as error:
            return Response(error, status=404)

# class ResultPartialAPIView(APIView)
#     def get(self, request, id):
#         try:
#             company = Insert.objects.get(id=id)



# class InsertList(generics.ListAPIView):