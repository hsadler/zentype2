
import BaseService from '@/services/BaseService'

class LocalStorageService extends BaseService {
  constructor () {
    super()
    this.localStorage = window.localStorage
  }
  set (key, val) {
    return this.localStorage.setItem(key, val)
  }
  get (key) {
    return this.localStorage.getItem(key)
  }
  delete (key) {
    return this.localStorage.removeItem(key)
  }
}

export default new LocalStorageService()
