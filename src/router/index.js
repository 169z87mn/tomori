import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'RadioTab',
    component: () => import('@/components/radio/radio-tab')
  },
  { 
    path: '*', 
    component: () => import('@/components/not-found')
  }
]

export default new Router({
  mode: 'history',
  routes
})