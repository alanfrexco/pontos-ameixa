from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import models
from app import serializers
from app.models import Insert
from app.serializers import InsertSerializer


class InsertViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InsertSerializer
    queryset = models.Insert.objects.all()


@api_view(['GET', 'POST', 'DELETE'])
def points(request):
    if request.method == 'GET':
        _points = Insert.objects.filter(empresa='Chupa Cabra').all()
        print(_points)
        results = InsertSerializer(_points, many=True).json
        for item in results:
            print(item)
            # item = request.json()['pontos_ganhos']
            # total = sum(it['pontos_ganhos'] for it in pontos_ganhos)
            # print(total)



        return Response({'results': results})
