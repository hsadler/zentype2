
import BaseService from '@/services/BaseService'

class UserAuthService extends BaseService {
  constructor () {
    super()
    this.isAuth = false
  }
  get injectServices () {
    return ['httpService', 'localStorageService', 'userService']
  }
  createUser (email, password) {
    /*
      attempt to create user and set token
      if successful, fetch and set user data on userService
    */
    const url = '/api/user-auth/signup'
    const options = { email, password }
    return this.httpService.post(url, options).then(res => {
      if (res.result && res.result.token) {
        this.isAuth = true
        this.localStorageService.set('authToken', res.result.token)
        this.userService.fetchAndSetUserData().then(status => {
          return true
        })
      } else {
        return false
      }
    })
  }
  loginUser (email, password) {
    /*
      attempt to log in user and set token
      if successful, fetch and set user data on userService
    */
    const url = '/api/user-auth/login'
    const options = { email, password }
    return this.httpService.post(url, options).then(res => {
      if (res.result && res.result.token) {
        this.isAuth = true
        this.localStorageService.set('authToken', res.result.token)
        this.userService.fetchAndSetUserData().then(status => {
          return true
        })
      } else {
        return false
      }
    })
  }
  logoutUser () {
    /*
      log out user, delete token clear user data from userService
    */
    this.isAuth = false
    this.localStorageService.delete('authToken')
    this.userService.clearUserData()
    return true
  }
  refreshUserToken () {
    /*
      attempt to fetch and set new token
    */
    const url = '/api/user-auth/refresh-token'
    return this.httpService.get(url).then(res => {
      if (res.result && res.result.token) {
        this.isAuth = true
        this.localStorageService.set('authToken', res.result.token)
        return true
      } else {
        return false
      }
    })
  }
}

export default new UserAuthService()
