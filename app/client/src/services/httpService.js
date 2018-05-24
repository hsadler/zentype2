
import axios from 'axios'
import BaseService from '@/services/BaseService'

class HttpService extends BaseService {
  get (url) {
    // TODO: update this to construct query param url from options dictionary
    return axios.get(url).then(res => {
      return res.data
    })
  }
  post (url, options) {
    return axios.post(url, options).then(res => {
      return res.data
    })
  }
}

export default new HttpService()
