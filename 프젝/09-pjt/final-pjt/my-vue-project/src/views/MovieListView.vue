<template>
    <div>
        <h1>전체 영화 목록</h1>
        <div class="movie-list">
            <MovieCard 
            v-for="movie in movieStore.movies.results"
            :key="movie.id"
            :movie = movie
            @click="goToDetail(movie.id)"
            />
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useRouter } from 'vue-router';


// 영화 단일 데이터 하위 컴포넌트에 넘겨주기
import MovieCard from '@/components/MovieCard.vue';



// 영화 전체 목록 데이터 가져오기
const movieStore = useMovieStore()
onMounted(()=>{
    movieStore.getMovies()
})


// 영화 상세 정보 페이지로 이동

const router = useRouter()

const goToDetail = function(movieId) {
    router.push({name : 'movie-detail', params:{movieId:movieId}})
}


</script>

<style scoped>

.movie-list{
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    padding : 10px

}
</style>