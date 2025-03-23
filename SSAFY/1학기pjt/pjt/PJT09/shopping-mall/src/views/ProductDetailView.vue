<template>
  <div v-if="product.id">
    <h1>상품명: {{ product.title }}</h1>
    <img :src="product.image" alt="" width="200">
    <p>가격: {{ product.price }}</p>
    <p>카테고리: {{ product.category }}</p>
    <button @click="cartStore.addCart(product)">장바구니에 추가</button>
  </div>
  <p v-else>Loading 중...</p>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCartStore } from '@/stores/counter';
import axios from 'axios'
// 1. product Id 를 URL params 로 부터 가져온다.
const route = useRoute()
const productId = route.params.product_id
const cartStore = useCartStore()

// 2. product Id 를 이용해서 데이터를 가져온다.
// 2.1 store 에서 데이터를 가져오는 경우
// - 상품 디테일 페이지부터 접근하면 사용자가 데이터를 가져올 수 없다!

// 2.2 axios 로 상세 데이터를 호출하기
// 2.2.1 API 가 제공해주는 경우 OK

// 상품 상세 정보: detail 페이지에서만 사용함
// store 가 아니라 여기에 바로 구현
const product = ref({})
axios({
  method: 'get',
  url: `https://fakestoreapi.com/products/${productId}`
}).then((response) => {
  product.value = response.data
}).catch((error) => {
  console.log(error)
})


// 2.2.2 API 가 제공해주지 않는 경우
//  - App.vue 등 상위컴포넌트에서 호출
//    -> 대신, 데이터가 있다면 재호출을 하지 않도록 구현!

// 3. 화면에 그려준다.
</script>

<style scoped>

</style>
