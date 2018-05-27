
import BaseService from '@/services/BaseService'

class UserAuthService extends BaseService {
  get injectServices () {
    return ['httpService', 'localStorageService']
  }
  createUser (email, password) {
    const url = '/api/user-auth/signup'
    const options = { email, password }
    return this.httpService.post(url, options).then(res => {
      if (res.result && res.result.token) {
        this.localStorageService.set('authToken', res.result.token)
        // TODO: also, will need to set user data here...
        return true
      } else {
        return false
      }
    })
  }
  loginUser (email, password) {
    const url = '/api/user-auth/login'
    const options = { email, password }
    return this.httpService.post(url, options).then(res => {
      if (res.result && res.result.token) {
        this.localStorageService.set('authToken', res.result.token)
        // TODO: also, will need to set user data here...
        return true
      } else {
        return false
      }
    })
  }
  logoutUser () {
    this.localStorageService.delete('authToken')
    // TODO: also, will need to unset user data here...
  }
  refreshUserToken () {
    const url = '/api/user-auth/refresh-token'
    return this.httpService.get(url).then(res => {
      if (res.result && res.result.token) {
        this.localStorageService.set('authToken', res.result.token)
        return true
      } else {
        return false
      }
    })
  }
}

export default new UserAuthService()
