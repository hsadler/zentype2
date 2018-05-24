
import BaseService from '@/services/BaseService'

class UserService extends BaseService {
  get injectServices () {
    return ['httpService']
  }
  createUser (email, password) {
    const url = '/api/user-auth/signup'
    const options = { email, password }
    return this.httpService.post(url, options)
  }
}

export default new UserService()
