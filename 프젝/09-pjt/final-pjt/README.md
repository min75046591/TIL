# 09-PJT
## 요구사항
> 이전 프로젝트에서 공통적으로 요구되었던 사항은 적지 않기로 한다.
- `.env` 파일을 사용해 `API Key`를 비롯한 중요한 정보를 제출하지 않음 
- 참고 : https://ko.vitejs.dev/guide/env-and-mode.html
    - Vite 환경변수 : Vite는 `import.meta.env` 객체를 이용해 환경 변수에 접근 가능, 문자열 형태로 접근할 수 있다. 
    -  Vite에서 접근 가능한 환경 변수는 일반 환경 변수와 구분을 위해 `VITE_` 라는 접두사를 붙여 나타낸다.
    - 예시 :
    ``` js
    // .env에 등록
    VITE_SOME_KEY=123
    DB_PASSWORD=foobar
    //따옴표를 감싸도 괜찮음 "foobar"
    // 출력 
    console.log(import.meta.env.VITE_SOME_KEY) // "123"
    console.log(import.meta.env.DB_PASSWORD) // undefined
    ```
    - ### `주의사항`
    - VITE_를 붙이지 않은 변수명은  **검색되지않아**사용할 수 없으니 주의한다. 
    - 환경변수 파일은 반드시 root directory (최상위 폴더)에 위치해야한다. => 그렇지 않으면 인식하지 못하니 주의한다.


- 기능
    1. 최고 평점 영화 조회
    2. 최고 평점 영화의 세부정보 조회
        - 영화 제목, 개봉일, 러닝타임, 평점, 장르, 줄거리
        - 공식 예고편 영상 조회 
    3. 영화 리뷰 영상 조회
    4. 현재 날씨에 따른 영화 추천하기


### 사전 준비
- `.env` 파일 최상위 폴더 내 생성 
    ![가상환경 설정 이미지](./images/가상환경%20설정.JPG)

- 뷰 생성시 기본 세팅 파일들 삭제 : components, main.js, APP.vue 등 
- pinia를 통한 state management 환경 세팅 
    ``` js
    // @/stores/store.js
    import { ref, computed } from 'vue'
    import { defineStore } from 'pinia'

    export const useMovieStore = defineStore('movie', () => {
    

    return {  }
    })

    ```

-  외부 데이터를 수집하기 위한 axios 설치 
    ```
    $ npm install axios
    ```
- 프로젝트 컴포넌트 구조 
    ![](./images/컴포넌트%20구조.JPG)
- router 관련 컴포넌트
    ![](./images/라우터%20관련%20컴포넌트.JPG)

## 진행
### A. 최고 평점 영화 조회
> 내비게이션바에서 영화조회링크(/movies)를 클릭하면 평점이 높은순으로 
정렬된 영화목록을 출력

> (TMDB API -MOVIES LISTS -Top Rated 활용)

> router에 등록하는 과정은 모든 과정에서 반복되기 때문에 이후에는 생략하도록한다. 

1. router 등록
``` js 
// @/router/index.js
    ...
    {
        path: '/movies',
        name: 'movies',
        component: MovieListView
        }
    ... 
```
2. 요구 명세서에 따른 컴포넌트 생성
    - MovieListView 생성 
        - 경로 : "@/views/MovieListView.vue"
        ``` js 
        <template>
            <div>
                <h1>전체 영화 목록</h1>
                <div class="movie-list">
                    <MovieCard 
                    v-for="movie in movieStore.movies.results"
                    :key="movie.id"
                    :movie = movie
                    />
                </div>
            </div>
        </template>

        <script setup>
        import { onMounted } from 'vue';
        import { useMovieStore } from '@/stores/movie';

        // 영화 단일 데이터 하위 컴포넌트에 넘겨주기
        import MovieCard from '@/components/MovieCard.vue';



        // 영화 전체 목록 데이터 가져오기
        const movieStore = useMovieStore()
        onMounted(()=>{
            movieStore.getMovies()
        })

        </script>

        <style scoped>

        .movie-list{
            display: flex;
            flex-wrap: wrap;
            gap: 25px;
            padding : 10px

        }
        </style>
        ```
        - css : 반응형 웹페이지 구조로 구현하도록 했다.
        - 전체 영화 데이터를 for문을 순회하며 하위 컴포넌트인 MoiveCard로 전달한다.
    - MovieCard 컴포넌트 생성
        ```js 
            <template>
                <div class = "movie-card">
                    <img :src="`${imgUrl}${movie.poster_path}`" alt="">
                    <h3>{{ movie.title }}</h3>
                    <p>{{ movie.overview }}</p>

                </div>
            </template>

            <script setup>
            import { defineProps } from 'vue';

            const props = defineProps({
                movie : Object
            })
            const movie = props.movie
            const imgUrl = "https://image.tmdb.org/t/p/original/"
            </script>

            <style scoped>

            .movie-card{
                width: 400px;
                border: 1px solid #ccc;
                padding: 10px;
            }

            img{
                width: 100%;
            }
            </style>
        ```
### B. 최고 평점 영화의 세부정보 조회

> MovieCard를 클릭하면 RouterLink를 통해 MovieDetailView(/:movieId)로 이동 후 MovieDetailInfo를 출력

- MovieListView 컴포넌트에서 클릭 이벤트를 작성한다.
    ``` js 
        <template>
            <div>
                <h1>전체 영화 목록</h1>
                <div class="movie-list">
                    <MovieCard 
                    v-for="movie in movieStore.movies.results"
                    :key="movie.id"
                    :movie = movie
                    @click="goToDetail(movie.id)" // 클릭 이벤트 작성
                    />
                </div>
            </div>
        </template>

        <script setup>
        ...
        {/* 영화 상세 정보 페이지로 이동 */}
        import { useRouter } from 'vue-router'
        const router = useRouter()

        const goToDetail = function(movieId) {
            router.push({name : 'movie-detail', params:{movieId:movieId}})
        }

        </script>
    ```
    - RouterLink를 통해 클릭하면 해당 view url에서 필요한 인자를 전달할 수 있도록 `router.push`를 작성하였다.

- MovieDetailView 컴포넌트 생성 
    ```js
    <template>
        <h3>영화 상세 페이지</h3>
        <div class="container">
            <h1>영화 세부정보 페이지</h1>
            <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`">
            <h2>{{ movie.title }}</h2>
            <p><h4>개봉일 :</h4> {{ movie.release_date }}</p>
            <p><h4>러닝타임 :</h4> {{ movie.runtime }} 분</p>
            <p><h3> 장르 </h3><span v-for="genre in movie.genres" style="margin-right:10px">{{ genre.name }} </span></p>
            <p><h3>줄거리</h3>{{ movie.overview }}</p>
            <p><h3>관련 영상</h3></p>
            <img src="@/assets/Youtube_logo.png" style ="width:10%" @click="modalOpen">
            
            <div class="modal" v-if="isModalOpen" @click="closeModal">
                <YoutubeTrailerModal :movieTitle="movie.title" :movieId="movie.id" class="modal-content"/>
            </div>
    </div>
    </template>

    <script setup>
    // 해당 영화 아이디를 찾는다. (주소를 통해서)
    import {useRoute} from 'vue-router'
    import {ref} from 'vue'
    import axios from 'axios'

    const route = useRoute()
    const movieId = route.params.movieId

    // 해당 영화 아이디로 영화 상세 목록 찾기 
    // 외부 데이터를 활용해야 한다. -> axios
    const movie = ref([])
    const tmdbKey = import.meta.env.VITE_TMDB_API_KEY
    axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/movie/${movieId}?language=ko-KR`,
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${tmdbKey}`
        }
    })
        .then((response) =>{
            movie.value = response.data
        })
        .catch((error) =>{
            console.log(error)
        })


    // 모달 팝업 띄우기

    // 모달 띄우기 상태 변수 설정
    const isModalOpen = ref(false)

    const modalOpen = function(){
        isModalOpen.value = true

    }

    const closeModal = function(){
        isModalOpen.value = false
    }


    // 하위 컴포넌트 불러오기 
    import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'

    </script>

    <style scoped>
    img {
    width: 200px
    }

    h4 {
    display: inline-block;
    }
    .container{
    display : flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    }


    /* modal css 적용하기  */
    .modal {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.5);
    }
    .modal-content {
        position: relative;
        background-color: white;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
        max-width: 700px;
    }

    </style>
    ```
    1. params로 받은 movie id를 조회한다.
        - route를 통해 params를 조회하여 필요한 id를 가져온다. 
        ``` js
        // 해당 영화 아이디를 찾는다. (주소를 통해서)
        import {useRoute} from 'vue-router'
        const route = useRoute()
        const movieId = route.params.movieId
        ```  
    2. API를 통해 해당 Id로 영화 상세 정보를 조회하여 데이터를 가져온다.
        ``` js 
        // 해당 영화 아이디로 영화 상세 목록 찾기 
        // 외부 데이터를 활용해야 한다. -> axios
        const movie = ref([])
        const tmdbKey = import.meta.env.VITE_TMDB_API_KEY
        axios({
            method: 'GET',
            url: `https://api.themoviedb.org/3/movie/${movieId}?language=ko-KR`,
            headers: {
                accept: 'application/json',
                Authorization: `Bearer ${tmdbKey}`
            }
        })
            .then((response) =>{
                movie.value = response.data
            })
            .catch((error) =>{
                console.log(error)
            })

        ```
        - .env에 등록했던 Api Key를 가져온다.
        - axios를 통해 외부 데이터를 조회한다. 
        - tmdb api 사이트에서 요청 사항에 따라 작성하였다. 
        - 에러 없이 잘 가져왔을 경우 movie를 업데이트 한다. 

    3. template에는 요구 명세서에 따라 영화 상세 정보를 작성하였다. 
    4. 유튜브 로고 이미지를 클릭하면 해당 영화의 예고편이 나올 수 있도록 작성한다. 
        - 트러블 슈팅이 가장 많았던 부분이다.
        - 이미지를 클릭하였을 때 모달 컴포넌트가 활성화될 수 있도록 값과 함수를 작성하였다.
        - 모달 컴포넌트에서 css를 통해 팝업창 ux를 고려한 ui 구조를 설계하였다.
        - 모달 컴포넌트를 클릭했을 경우 팝업 창이 닫힐 수 있도록 함수를 작성하였다.

        ### tmdb의 movie api 를 활용하여 유튜브에 등록되어 있는 메인 예고편을 조회하였다.
        ``` js
        // @/components/YoutubeModalTrailer.vue

        <template>
            <div style="background-color: white;" color:black>
                <h3>{{ movieTitle }} 메인 예고편</h3>
                <iframe  width="640" height="360"
                :src="youtubeUrl" frameborder="0" ></iframe>
                
            </div>
        </template>

        <script setup>

        const url = 'https://api.themoviedb.org/3/movie/129/videos?language=ko-KR';
        import { ref, defineProps } from 'vue'

        import axios from 'axios'
        const props = defineProps({
            movieId:Number,
            movieTitle:String
        })
        const tmdbKey = import.meta.env.VITE_TMDB_API_KEY
        // const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY
        const data = ref([])
        const youtubeUrl = ref('')
        axios({
            method: 'GET',
            url : `https://api.themoviedb.org/3/movie/${props.movieId}/videos?language=ko-KR`,
            headers: {
                accept: 'application/json',
                Authorization: `Bearer ${tmdbKey}`
            }
        })
            .then((response) =>{
                // 해당 비디오 정보 업데이트 
                data.value = response.data
                const youtubeId = data.value.results[0].key
                youtubeUrl.value = `http://www.youtube.com/embed/${youtubeId}`
            
            })
            .catch((error)=>{
                console.log(error)
            })


        </script>
        ```
        - axios를 통해 해당 vedio 정보를 조회하여 유튜브에 등록되어있는 key값을 조회하였다.
        - 참고한 api 사이트 : https://developers.google.com/youtube/iframe_api_reference?hl=ko
        - `iFrame` 속성을 통해 해당 url 사이트를 출력하였다.
            - iFrame : HTML Inline Frame 요소이며 inline frame의 약자이다. 
            - 특징 : 현재 페이지에 중첩된 브라우저를 제한 없이 불러와서 삽입할 수 있다.
            - 속성
                - src : 삽입 할 홈페이지 url  
                - name : 프레임 이름   
                - width : 프레임 가로 너비    
                - height : 프레임 세로 길이    
                - frameborder : 프레임 테두리 선 (0으로 설정하면 프레임의 테두리선 x, 1로 설정하면 프레임의 테두리선 o)   
                - scrolling : 스크롤바의 표시 여부를 나타냅니다. (yes로 설정하면 스크롤 바 무조건 표시, auto는 자동 표시)  
                - style 적용 가능
                - autoplay : 1일 경우 자동 재생
                - loop : 1일 경우 반복 
        
## 느낀점

1. 외부 데이터를 활용할 때 불러온 데이터를 읽을 줄 알아야 한다.   
    -> 원하는 특정 값이 어디에 어떻게 위치해 있으며, 해당 API가 제공하는 다양한 기능을 활용할 수 있어야겠다.
    - tmdb의 video API를 확인하지 못하고, youtube API로 바로 접근하려고 했었다.
    - 따라서 이 과정에서 API Key를 제대로 불러오지 못하는 이슈가 발생하였고, 그 결과 많이 헤맸다.
    - 또한 video API안에 있는 데이터가 어떤 값인지도 알아낼 수 있어야겠다.
    - 해당 데이터에서 key값이 존재했는데, 이것은 youtube에 등록되어 있는 값으로, Youtube iframe에 관한 문서를 읽고 활용하였다.
2. 다양한 API 문서를 읽고 관련 기능에 대한 문서들을 많이 읽었다. 
    - Vue와 axios를 동시에 작성하다 보니, 디버깅을 하는 과정에서 많이 헷갈렸다.
    - 그 과정에서 다양한 문서들을 많이 읽게 되었고, 앞으로 관통을 진행하면서 겪게 될 과정이라 생각하여 꼼꼼하게 함께 읽어 보았다.
3. 요구 명세서에 적혀있는 사항들을 꼼꼼하게 읽어야겟다.
    - 작성되어 있던 컴포넌트 트리 구조를 제대로 읽지 않아 다양한 곳에서 컴포넌트를 작성하지 않고 div로 데이터를 출력하였다.
    - 이후 다시 같이 하나씩 요구명세서를 읽으며 제대로 구현할 수 있도록 하였다.

