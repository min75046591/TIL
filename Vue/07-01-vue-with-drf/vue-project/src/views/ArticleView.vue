<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink
    :to="{name: 'CreateView'}"
    >
    [CREATE]
    </RouterLink>
    <hr>
    <ArticleList/>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import { useCounterStore } from '@/stores/counter';
import ArticleList from '@/components/ArticleList.vue';
import {RouterLink} from 'vue-router'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
