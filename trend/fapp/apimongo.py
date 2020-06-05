import os
import sys
import urllib.request
import json
import collections
import pymongo
from pymongo import MongoClient


def doFiles(pKey, pColname, start, end):

    def getNavNews(pKey): # 값 불러오기
        client_id = "LUyi5j9ptG8gS_oTbOFJ"
        client_secret = "35wTDZgB2S"
        url = "https://openapi.naver.com/v1/datalab/search"

        # create json file
        with open('C:\\Users\7\Desktop\trend\trend', 'r') as json_file : # json파일에 json_file이라는 핸들을 만들고
            json_data = json_file.read() # 그 파일을 읽어들여 json_data로 저장


        bit_json = json.loads(json_data) # json_data를 json.loads를 하여 딕셔너리 형태로 받아오며

        # modify json file
        bit_json['keywordGroups'][0]['groupName'] = pKey
        bit_json['keywordGroups'][0]['keywords'][0] = pKey
        bit_json['keywordGroups'][0]['keywords'][1] = pKey
        bit_json['startDate'] = start
        bit_json['endDate'] = end

        # save json file
        with open('C:\\Users\7\Desktop\trend\trend', 'w', encoding='utf-8') as make_file:
            json.dump(bit_json, make_file, indent="\t")
        data = open('C:\\Users\7\Desktop\trend\trend', 'rt', encoding='UTF8').read()

        body = str(data) + '\n' 
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            u8_json = response_body.decode('utf-8')
            words = json.loads(u8_json)
            print(words)

            return words


        else:
            print("Error Code:" + rescode)

        
    def insertMongo(pWords):

        # 몽고디비 연결 클라이언트
        # 1.몽고디비 클라이언트 연결객체 생성
        client = MongoClient('mongodb://localhost:27017/')
        # -- 객체생성확인
        print('client.HOST: {0}'.format(client.HOST))

        # 2. 데이터베이스 생성
        mdb = client['mdb_py']
        # -- 디비 생성 확인
        print(mdb)

        # 3. 컬렉션 객체 생성
        mdb[pColname].remove()
        keys = mdb[pColname]

        print("------------------------------------------------------------------------------------")
        period = []
        for i in range((len(pWords['results'][0]['data']))):
            result = pWords['results'][0]['data'][i]['period']
            period.append(result)

        ratio = []
        for i in range((len(pWords['results'][0]['data']))):
            result = pWords['results'][0]['data'][i]['ratio']
            ratio.append(result)


        keys_cs = [ {'periods': period ,'ratios': ratio} ]

        #5. 여러개의 데이터 입력
        rst_keys = keys.insert_many(keys_cs)
        print(rst_keys)
        return rst_keys
        
        

    # 스크래핑후 몽고db저장
    words = getNavNews(pKey)
    insertMongo(words)

    return words


#doFiles('유재석','유재석','2017-01-01','2018-01-01')
#doFiles('검색값','컬렉션이름','시작기간','끝기간')

print("end code")




