# PJT 02 - 데이터분석, aladdin

### 이번 pjt 를 통해 배운 내용

* 영화 - 추출한 값을 json 형식으로 바꾼 후 데이터에서 나에게 필요한 데이터를 추출하는 법을 배웠다.

* 금융 - 전처리 과정에 대해 이해하고 데이터 분석 후 시각화 하는 법을 배웠다.


---

## A. 02_금융 

* 요구 사항 : 데이터 추출 후 시각화

* 결과 : ![Alt text](image.png)
  
```python
x = ave_df_2021['Date']  # x 좌표값
y = ave_df_2021['Close']  # y 좌표값

plt.plot(x, y)
plt.xticks(rotation = 45)

plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Average Close Price')

# 그래프 표시
plt.show()
``````

  * 이 문제에서 어려웠던점 : 데이터 분석을 처음 다루다 보니 생소해서 지피티와 친구의 도움 없이 해결하기 힘들었다.



## B. 01_알라딘

* 요구 사항 : 작가의 작품 조회 & 작품을 쓴 작가의 작품 & 알고리즘을 사용한 데이터 출력

* 결과 : 

```
'adult': False,
  'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
  'categoryId': 50920,
  'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
  'cover': 'https://image.aladin.co.kr/product/1303/6/coversum/8954616127_3.jpg',
  'customerReviewRank': 9,
  'description': '&lt;연금술사&gt; &lt;브리다&gt;의 작가 파울로 코엘료의 2011년 신작. 작가의 길에 들어선 지 '
                 '20여 년이 훌쩍 넘은 파울로 코엘료의 세계를 아우르는 동시에, 자신의 근본으로 회귀함으로써 새로운 출발을 '
                 '알리는 작품이다. 코엘료의 고국인 브라질을 시작으로, 포르투갈, 헝가리 등 20여 국에서 출간되어 출간 첫날 '
                 '즉시 베스트셀러 1위에 올라 변함없이 코엘료 신드롬을 일으켰다.',
  'fixedPrice': True,
  'isbn': '8954616127',
  'isbn13': '9788954616126',
  'itemId': 13030616,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=13030616&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 670,
  'priceSales': 12150,
  'priceStandard': 13500,
  'pubDate': '2011-09-23',
  'publisher': '문학동네',
  'salesPoint': 3071,
  'stockStatus': '',
  'subInfo': {},
  'title': '알레프'}]
``````
-----
-----

['연금술사', '11분', '흐르는 강물처럼', '브리다', '포르토벨로의 마녀']
  
---
  * 이 문제에서 어려웠던점 : 오픈api에서 원하는 데이터를 추출할때 순서를 짜는게 어려웠다. 특히 처음 받은 응답에 대해 또 다른 데이터를 추출하는 과정이 가장 어려웠다.


  * 내가 생각하는 이 문제의 포인트 : 딕셔너리 구조에 대한 이해 및 데이터 추출 후 접근이 포인트라고 생각.




# 후기

* 구글링과 gpt를 통해 해결을 했지만 문제를 그 결과에 대해 이해를 제대로 하지 못했다고 느꼈습니다. 하지만 이렇게 차근차근 프로젝트를 하다보면 익숙해져서 잘 다룰 수 있을거라 믿어 의심치 않습니다.

* 하지만 여전히 딕셔너리와 리스트에 많이 부족한 거 같습니다. 이번 프로젝트를 통해 제가 보완해야 할 점을 알게됐습니다.

* 우선 영화 프로젝트 1을 해보고 좀 더 역량을 기르고 다시 영화 프로젝트 2에 도전하겠습니다.
