import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import JoinPage from '../views/JoinPage'
import QuizMainPage from '@/views/QuizMainPage';
import QuizStart from '@/views/QuizStart';

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
  },
  {
    path: '/quiz/:quizId/start',
    name: 'QuizStart',
    component: QuizStart
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
