from django.views.generic import CreateView
from .models import Upload
import boto3
import time

dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')
client = boto3.client('dynamodb', region_name='eu-west-3')


class UploadView(CreateView):
    model = Upload
    fields = ["file", "table_name"]
    template_name = 'files/upload.html'
    success_url = "/"


def dynamoDB(request):
    table_name = request.POST['table_name']

    existing_tables = client.list_tables()['TableNames']

    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        time.sleep(5)

    table = dynamodb.Table(table_name)

    name_with_extension = request.FILES['file'].name.split('.')
    file_name = name_with_extension[0]
    if len(name_with_extension) > 1:
        file_extension = name_with_extension[1]
    else:
        file_extension = "no extension"

    table.put_item(
        Item={
                'name': file_name,
                'extension': file_extension,
                'size': request.FILES['file'].size,
                'upload date and time': time.ctime()
            }
    )

    return UploadView.as_view()(request)
