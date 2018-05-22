
import services from '@/services'

class UserService {
  createUser (email, password) {
    var httpService = services.use('httpService')
    var url = '/api/user-auth/signup'
    var options = { email, password }
    return httpService.post(url, options)
  }
}

export default new UserService()
