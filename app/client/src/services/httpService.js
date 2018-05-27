
import axios from 'axios'
import BaseService from '@/services/BaseService'

class HttpService extends BaseService {
  get injectServices () {
    return ['localStorageService']
  }
  get (url) {
    const config = this.getRequestConfig()
    // TODO: update this to construct query param url from options dictionary
    return axios.get(url, config).then(res => {
      return res.data
    })
  }
  post (url, options) {
    const config = this.getRequestConfig()
    return axios.post(url, options, config).then(res => {
      return res.data
    })
  }
  getRequestConfig () {
    const config = {}
    const token = this.localStorageService.get('authToken')
    if (token) {
      config.headers = {
        'Authorization': 'Bearer ' + token
      }
    }
    return config
  }
}

export default new HttpService()
