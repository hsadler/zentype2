
import Vue from 'vue'
import Router from 'vue-router'
import services from '@/services'

// views
import HomeView from '@/views/HomeView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import NotFoundView from '@/views/NotFoundView'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/signup',
      name: 'SignupView',
      component: SignupView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path: '*',
      name: 'NotFoundView',
      component: NotFoundView
    }
  ]
})

// handles 'requiresAuth' routes
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // redirect to login page if not authorized
    const userAuthService = services.use('userAuthService')
    if (!userAuthService.getIsAuth()) {
      next({
        name: 'LoginView'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
