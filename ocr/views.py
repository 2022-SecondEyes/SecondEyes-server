import base64
import datetime
import kakao_ocr.kakao_ocr

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

    filename = "ocrIMG" + str(datetime.datetime.now().date()) + str(datetime.datetime.now().microsecond) + ".jpg"
    with open("media/" + filename, 'wb') as f:
        f.write(image_data)

    data = kakao_ocr.kakao_ocr.call_kakao_ocr("media/" + filename)

    return Response(data= data, status=status.HTTP_200_OK)


