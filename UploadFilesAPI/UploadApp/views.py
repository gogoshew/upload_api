from django.db.models import Count
from django.http.multipartparser import MultiPartParser
from rest_framework import views, status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

import pandas as pd

from UploadApp.models import Client, Organization, Bills
from UploadApp.serializers import FileSerializer, ClientSerializer


class ClientUploadView(views.APIView):
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_serializer.is_valid():
            data = self.request.data.get('file')

            xls = pd.ExcelFile(data)
            client_sheet = pd.read_excel(xls, sheet_name='client')
            organization_sheet = pd.read_excel(xls, sheet_name='organization')
            client_columns = list(client_sheet.columns.values)
            client_title = client_columns[0]

            instances = [
                Client(
                    name=row[client_title]
                )
                for index, row in client_sheet.iterrows()
            ]

            Client.objects.bulk_create(instances)


            organization_columns = list(organization_sheet.columns.values)
            client_name_title, name_title = organization_columns[0], organization_columns[1]

            org_names = [
                Organization(
                    org_name=row[name_title],
                    client_name=Client.objects.get(name=row[client_name_title])
                             )
                for index, row in organization_sheet.iterrows()
            ]
            Organization.objects.bulk_create(org_names)



            return Response(
                {"message": "Upload Successfull"}, status=status.HTTP_200_OK)


class BillsUploadView(views.APIView):
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_serializer.is_valid():
            data = self.request.data.get('file')

            xls = pd.ExcelFile(data)
            bills_sheet = pd.read_excel(xls)
            bills_columns = list(bills_sheet.columns.values)
            client_org_title, n_title, sum_title, date_title = bills_columns[0], bills_columns[1], bills_columns[2], bills_columns[3]

            instances = [
                Bills(
                    bill_number=row[n_title],
                    bill_sum=row[sum_title],
                    date=row[date_title],
                    client_org=Organization.objects.get(name=row[client_org_title])
                )
                for index, row in bills_sheet.iterrows()
            ]
            Bills.objects.bulk_create(instances)

            return Response(
                {"message": "Upload Successfull"}, status=status.HTTP_200_OK)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = ClientSerializer

