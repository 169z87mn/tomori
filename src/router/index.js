import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/page/HomePage'
import NotFound from '@/page/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    { path: '*', component: NotFound }
  ]
})