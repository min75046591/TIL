<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <textarea  v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import {useRouter} from 'vue-router'

const title = ref(null)
const content = ref(null)

const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
  })
    .then(() => {
      // 성공한 경우 메인페이지로 이동
      router.push({ name: 'ArticleView' })
    })
    .catch(error => 
      console.log(error)
    )
}

</script>

<style>

</style>
