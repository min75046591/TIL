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
console.log(props.movieId)
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

<style  scoped>


</style>