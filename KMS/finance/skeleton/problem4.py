import pprint
import requests

# 전체 정기예금의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터에 모든 정보가 담겨 있습니다.
# 3. key 값이 "result" 인 데이터의 key 값만 출력합니다.

def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
    api_key = "64707c0cf5710d008e3f7986f61f3099"

  # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
 
    result = requests.get(url).json()

    result_len = len(result['result']['baseList'])

    result_opt = result['result']['optionList'][0]['fin_co_no']

    result_main = result['result']['baseList'][0]['fin_co_no']


    value = []
    for i in range(result_len):
        if result_opt == result_main:
        
            value.append({'저축 금리' : result['result']['optionList'][i]['intr_rate'], '저축 기간' : result['result']['optionList'][i]['intr_rate2'], '저축금리유형' : result['result']['optionList'][i]['intr_rate_type'], '저축금리유형명' : result['result']['optionList'][i]['intr_rate_type_nm'], '최대 우대금리' : result['result']['optionList'][i]['save_trm']})

    info = []

    for i in range(len(value)):
    
        info.append({'금리정보' : value, '금융상품명' : result['result']['baseList'][i]['fin_prdt_nm'], '금융회사명' : result['result']['baseList'][i]['kor_co_nm']})

    pprint.pprint(info)

    

# pprint.pprint(get_deposit_products())
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    # pprint.pprint(result)

# new_dict_main['금융회사명'] = result_main[i]['kor_co_nm']