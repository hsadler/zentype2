// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '@/App'
import router from '@/router'

// services
import services from '@/services'
import httpService from '@/services/httpService'
import localStorageService from '@/services/localStorageService'
import userAuthService from '@/services/userAuthService'
import userService from '@/services/userService'

Vue.config.productionTip = false

services.registerServices({
  httpService,
  localStorageService,
  userAuthService,
  userService
})

var buildVueApp = function () {
  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
}

// attempt to refresh user token and fetch user data before building app
const uaService = services.use('userAuthService')
const uService = services.use('userService')
uaService.refreshUserToken().then(tokenStatus => {
  if (tokenStatus) {
    uService.fetchAndSetUserData().then(status => {
      buildVueApp()
    })
  } else {
    buildVueApp()
  }
})
