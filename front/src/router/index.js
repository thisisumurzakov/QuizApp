import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import JoinPage from '../views/JoinPage'
import QuizMainPage from '@/views/QuizMainPage';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/join',
    name: 'Join',
    component: JoinPage
  },
  {
    path: '/quiz/:quizId/home',
    name: 'QuizMainPage',
    component: QuizMainPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
