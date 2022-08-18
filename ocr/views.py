import base64
import datetime

from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def image_upload(request):
    image = request.data.get("img")
    try:
        image_data = base64.b64decode(image)
    except TypeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    filename = "ocrIMG" + str(datetime.datetime.now()) + ".jpg"
    with open("media/" + filename, 'wb') as f:
        f.write(image_data)

    return Response(status=status.HTTP_200_OK)
