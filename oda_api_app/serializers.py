from rest_framework import serializers

from oda_api_app.models import Payement


class PayementSerializer(serializers.ModelSerializer):
    id_academicien = serializers.IntegerField()
    id_motif = serializers.IntegerField()
    date = serializers.DateField()
    heure = serializers.TimeField()
    montant = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Payement
        fields = ('__all__')