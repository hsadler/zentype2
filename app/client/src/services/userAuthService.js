
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
        return true
      } else {
        return false
      }
    })
  }
  loginUser (email, password) {}
}

export default new UserAuthService()
