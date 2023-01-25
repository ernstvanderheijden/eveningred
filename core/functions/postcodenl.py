from django.conf import settings
from django.http import JsonResponse


def get_address(request):
    data = dict()
    data['form_is_valid'] = True
    strpostcode = ""
    lnghuisnr = 0
    strhuisnrtoevoeging = ""
    if request.GET.get('zkpostcode'):
        strpostcode = request.GET.get('zkpostcode').replace(" ", "")
    if request.GET.get('zkhuisnr'):
        lnghuisnr = int(request.GET.get('zkhuisnr'))
    if request.GET.get('zkhuisnrtoevoeging'):
        strhuisnrtoevoeging = request.GET.get('zkhuisnrtoevoeging')

    if strpostcode > "" and lnghuisnr > 0:
        import http.client
        conn = http.client.HTTPSConnection("api.postcode.eu")
        strb64 = settings.KEY_POSTCODENL
        headers = {"Authorization": "Basic " + strb64}
        searchstring = "/nl/v1/addresses/postcode/" + strpostcode + "/" + str(lnghuisnr) + "/" + strhuisnrtoevoeging
        conn.request("GET", searchstring, headers=headers)
        res = conn.getresponse()
        data['text'] = res.read().decode("utf-8")
    else:
        data['form_is_valid'] = False
    return JsonResponse(data)
