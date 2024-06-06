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