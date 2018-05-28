
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
    const url = '/api/user/get-data'
    return this.httpService.get(url).then(res => {
      if (res.result && res.result.user_data) {
        this.userData = res.result.user_data
      }
    })
  }
  clearUserData () {
    this.userData = {}
  }
  getEmail () {
    return this.userData.email ? this.userData.email : null
  }
}

export default new UserService()
