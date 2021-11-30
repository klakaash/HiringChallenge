from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MedicineName
import csv, json
from rest_framework.response import Response
from .utils import get_medicine_name
from .serializers import MedicineNameSerializer

# Create your views here.

@api_view(['POST'])
def populate_table(request):
    """ Read the CSV file and upload the data into the table to be queried later """
    with open("medname/meddata.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for i, line in enumerate(csv_reader):
            if i == 0:
                continue
            medicine = MedicineName(name=line[2], price=line[3], manufacturer=line[4], salt_name=line[5],
                                    drug_form=line[6], pack_size=line[7], strength=line[8])

            try:
                medicine.save()
            except:
                print("error in uploading")
                break

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

@api_view(['POST'])
def get_medicine(request):
    """ From the sentence entered by the user extract the medicine name and return the details """
    data = json.loads(request.body)
    sentence = data.get("sentence")

    extracted_name = get_medicine_name(sentence)
    if not extracted_name:
        return Response([])

    found_medicine = MedicineName.objects.filter(name__contains=extracted_name)
    serializer = MedicineNameSerializer(found_medicine, many=True)

    return Response(serializer.data)
