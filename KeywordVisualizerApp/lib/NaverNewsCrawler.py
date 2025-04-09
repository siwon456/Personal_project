import urllib.request
import json
import pandas as pd 
def searchNaverNews(keyword, start, display):
    
    client_id = "fJZdaHl9L2pxICMcjk_h"
    client_secret = "ApNrRszPZ9"
    # 한글 검색어 안전하게 변환
    encText = urllib.parse.quote(keyword)
    #query 생성
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

    #requeast 메세지 확인
    new_url = url+f"&start={start}&display={display}"
    request = urllib.request.Request(new_url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    resultJSON = None
    try :
        #requast 리스폰스 받기
       

    
        response = urllib.request.urlopen(request)

        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            resultJSON = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    except Exception as e:
        print(e)
        print(f"Error:{new_url}")
    return resultJSON

def setNewsSearchResult(resultAll, resultJSON):
    for result in resultJSON['items']:
        resultAll.append(result)

def saveSearchResult_CSV(json_list, filename):
    import pandas as pd
    data_df = pd.DataFrame(json_list)
    data_df.to_csv(filename)
    print(f"{filename}SAVED")

keyword = input("검색 :").strip()
# API 호출 결과 전송된 JSON이 없거나, 전송된 JSON에 검색 결과가 없을 때까지
# 검색 결과를 JSON의 list로 저장 후 검색 API 추가 호출


# 검색 결과를 저장할 list 초기화
resultAll = []

# 첫 검색 API 호출
start =1
display = 10
resultJSON = searchNaverNews(keyword, start, display)

while (resultJSON != None) and (resultJSON['display'] > 0):
     # 응답데이터 정리하여 리스트 저장
    setNewsSearchResult(resultAll, resultJSON)
    start +=display
    
    # 다음 검색 API 호출을 위한 파라미터 조정
    resultJSON = searchNaverNews(keyword, start, display)
    # API 호출 성공 여부 출력
    if resultJSON !=None:
        print(f"{keyword}[{start}]Serch Requaest Sucsess")
    else:
        print(f"{keyword}[{start}]Error")
# 리스트를 csv 파일로 저장
filename = f"./data/{keyword}_naver_news.csv"
saveSearchResult_CSV(resultAll,filename)
data_df = pd.read_csv(filename,index_col=0)
data_df.head()