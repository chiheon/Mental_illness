import Vue from 'vue'
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Main from '@/components/main'
import Graph from '@/components/Graph'
import Test from '@/components/Test'

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
      path: '/graph',
      name: 'graph',
      component: Graph
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})
