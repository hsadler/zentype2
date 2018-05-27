
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
    console.log('fetching user data...')
    // TODO: implement from stub
    return new Promise(resolve => {
      resolve(true)
    })

    // const url = '/'
  }
  clearUserData () {
    this.userData = {}
  }
}

export default new UserService()
