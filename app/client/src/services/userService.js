
import BaseService from '@/services/BaseService'

class UserService extends BaseService {
  constructor () {
    super()
    this.userData = {}
  }
  get injectServices () {
    return ['httpService']
  }
  fetchAndSetUserData () {
    // TODO: implement
    console.log('fetching user data...')
  }
  clearUserData () {
    this.userData = {}
  }
}

export default new UserService()
