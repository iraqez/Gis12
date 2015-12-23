import json, requests
url_point = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url_data = 'http://212.26.144.110/kadastrova-karta/get-parcel-Info'

c='6810100000:11:003:0101'

def cnum(cadnum):
    params_point = dict(
        cadnum=cadnum,
    )

    params_data = dict(
        koatuu = cadnum.split(':')[0],
        zone = cadnum.split(':')[1],
        quartal = cadnum.split(':')[2],
        parcel = cadnum.split(':')[3],
    )

    resp = (json.loads(requests.get(url=url_point, params=params_point).text)['data'])[0]
    try:
        resp.update((json.loads(requests.get(url=url_data, params=params_data).text)['data'])[0])
    except:
        resp = str("Нет данных")
    return resp

if __name__ == '__main__':
    print(cnum(c))