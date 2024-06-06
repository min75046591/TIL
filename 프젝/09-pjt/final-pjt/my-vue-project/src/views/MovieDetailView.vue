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