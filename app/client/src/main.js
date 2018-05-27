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

// attempt to refresh user token before building app
const uaService = services.use('userAuthService')
uaService.refreshUserToken().then(res => {
  // TODO: also, will need to set user data here...
  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
})
