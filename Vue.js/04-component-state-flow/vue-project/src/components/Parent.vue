<template>
  <div>
    <ParentChild 
    my-msg="message"
    :dynamic-props="name"
    @some-event="someCallback"
    @my-focus="someCallback2"
    @emit-args="getNumbers"
    @update-name="updateName"
    />

    <ParentItem
      v-for="item in items"
      :key="item.id"
      :my-prop="item"
    />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from '@/components/ParentItem.vue'

const name = ref('진영누나야 죽을래 ?')

const items = ref([
  {id: 1, name: '사과'},
  {id: 2, name: '배'},
  {id: 3, name: '바나나'}
])

const someCallback = function () {
  console.log('ParentChild가 발산한 이벤트를 수신한다.')
}

const someCallback2 = function () {
  console.log('defineEmits 방식으로 발산된 이벤트를 수신했다.')
}

const getNumbers = function (...args) {
  console.log(args)
}

const updateName = function () {
  name.value = 'Bella'
}

</script>

<style scoped>

</style>