import Vue from 'vue'
import Router from 'vue-router'
import Mission from '@/components/Mission'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Mission
    }, {
      path: '/mission/:index',
      name: 'Mission',
      component: Mission
    }
  ]
})
