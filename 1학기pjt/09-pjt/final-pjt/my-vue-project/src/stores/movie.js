import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  // 전체 영화 목록을 받을 배열 생성
  const movies = ref([]) 

  // tmdb 에서 데이터 가져오기
  
  // API key 
  const tmdbKey = import.meta.env.VITE_TMDB_API_KEY
  const getMovies = function(){
    axios({
      method : 'get',
      url :  'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1',
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${tmdbKey}`
      }
    })
      .then((response) =>{
        movies.value = response.data
      }
        
      )
      .catch((error) =>{
        console.log(error)
      })
  }
  
  return { movies, getMovies  }
})

