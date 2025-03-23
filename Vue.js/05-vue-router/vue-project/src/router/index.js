import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
// 중첩된 라우팅 활용
// 두 컴포넌트 import
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'

import UserHome from '@/components/UserHome.vue'

import LoginView from '@/views/LoginView.vue'

// 실습을 위해 항상 로그인이 되어있다고 가정
const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      
      // beforeEnter: (to, from) => {
      //   console.log(to)
      //   console.log(from)
      // },
      children: [
        { path: '', name: 'user', component: UserHome},
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts}
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다')
          return {name: 'home'}
        }
      }
    }
  ]
})

// 전역 가드
// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from) 
//   const isAuthenticated = false
  
//   // 로그인이 되어있지 않고 + 이동하는 곳이 login이 아니라면
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return {name: 'login'}
//   }
// })


export default router
