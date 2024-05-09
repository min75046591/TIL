<template>
  <div>
    <!-- <p>state : {{ newNumber }}</p>
    <p>{{ store.count }}</p>
    <button @click="store.increment()">+++</button>
    <p>{{ store.doubleCount }}</p> -->
      <h1>Todo Project</h1>
      <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
      <TodoList/>
      <TodoForm/>
  </div>
</template>

<script setup>
// import { useCounterStore } from '@/stores/counter'

// const store = useCounterStore()

// // state 참조 및 변경
// console.log(store.count)
// const newNumber = store.count + 1

// // getters
// console.log(store.doubleCount)

// // actions 호출
// store.increment()

import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>

</style>