<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{dynamicProps}}</p>

    <ParentGrandChild 
    :my-msg="myMsg"
    @update-name="updateName"
    />


    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">버튼2</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// 문자열 배열을 사용한 선언
// 내려받은 props를 선언
// - 을 기준으로 대문자로 바꿔서 쓴다
// defineProps(['myMsg'])

// 객체를 사용한 선언
const props = defineProps({
  myMsg: String,
  dynamicProps: String,
})
console.log(props)  // {myMsg: 'message'}
console.log(props.myMsg) // 'message'

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('myFocus')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>