import Vue from 'vue'
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Main from '@/components/main'
import Analysis from '@/components/analysis'
import Test from '@/components/Test'
import Twitter from '@/components/twitter'

Vue.use(BootstrapVue)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: Analysis
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/twitter',
      name: 'twitter',
      component: Twitter
    }
  ]
})
