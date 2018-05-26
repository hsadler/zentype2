
import BaseService from '@/services/BaseService'

class UserAuthService extends BaseService {
  get injectServices () {
    return ['httpService']
  }
  createUser (email, password) {
    const url = '/api/user-auth/signup'
    const options = { email, password }
    return this.httpService.post(url, options).then(res => {
      // do more here
      return res
    })
  }
}

export default new UserAuthService()
