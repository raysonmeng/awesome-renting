import requests

url = "http://www.ziroom.com/commute/room/list"

querystring = {
    "min_lng": "116.298019",
    "max_lng": "116.341137",
    "min_lat": "39.979847",
    "max_lat": "39.990959",
    "clng": "116.319578",
    "clat": "39.985403",
    "zoom": "16",
    "transport": "walk",
    "minute": "30",
<<<<<<< HEAD
    "price": '0,4500',
=======
    # "price": '0,4000',  # 价格区间
>>>>>>> 3b0b965fe84b306525f65e0fbd2b141e426e5dfd
    # "type": "1|10|29"
}

headers = {
    'Host': "www.ziroom.com",
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Accept': "*/*",
    'DNT': "1",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'Referer': "http://www.ziroom.com/map/",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    'Cookie': "gr_user_id=10b64ff4-1d39-4dd1-9898-eaaee5868bac; mapType=%20; CURRENT_CITY_CODE=110000; gr_session_id_8da2730aaedd7628=1ff5eb0b-1704-4d3d-bc4a-2bb55011d80f; gr_session_id_8da2730aaedd7628_1ff5eb0b-1704-4d3d-bc4a-2bb55011d80f=true; fixedApp=close; PHPSESSID=23qgia0st148cn036l52d5kgf4; CURRENT_CITY_NAME=%E5%8C%97%E4%BA%AC; BJ_nlist=%7B%2261708988%22%3A%7B%22id%22%3A%2261708988%22%2C%22sell_price%22%3A7630%2C%22title%22%3A%22%5Cu6d77%5Cu6dc0%5Cu4e2d%5Cu5173%5Cu675110%5Cu53f7%5Cu7ebf%5Cu82cf%5Cu5dde%5Cu8857%5Cu5927%5Cu6cb3%5Cu5e84%5Cu82d11%5Cu5c45%5Cu5ba4-%5Cu897f%5Cu5367%22%2C%22add_time%22%3A1539508568%2C%22usage_area%22%3A19%2C%22floor%22%3A%226%22%2C%22floor_total%22%3A%2218%22%2C%22room_photo%22%3A%22g2m1%5C%2FM00%5C%2F6F%5C%2F9D%5C%2FChAFB1uJNBWACtoiAA4KwtLbOV8558.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%7D; Hm_lvt_038002b56790c097b74c818a80e3a68e=1539508576; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1539508576",
    'cache-control': "no-cache",
}


def get_data(page=1):
    page = str(page)
    querystring['p'] = page
    print 'Get page: {}'.format(page)
    return requests.request("GET", url, headers=headers, params=querystring)


rooms = []
response_data = get_data().json()
rooms.extend(response_data['data']['rooms'])

total = response_data['data']['total']
page_count = int(total / 10) + 1
print 'Total rooms: {}'.format(total)
print 'Total pages: {}'.format(page_count)
for i in range(2, page_count+1):
    response_data = get_data(i).json()
    rooms.extend(response_data['data']['rooms'])

useful_infos = []
for room in rooms:
    useful_infos.append({
        'url': 'http:' + str(room['url']),
        'price': room['sell_price'],
        'usage_area': room['usage_area'],
        'rate': room['sell_price'] / room['usage_area'],  # less is better
    })
print len(useful_infos)
for i in sorted(useful_infos, key=lambda k: k['rate']):
    print i
