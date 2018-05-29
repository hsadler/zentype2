
import services from '@/services'

class BaseService {
  get injectServices () {
    return []
  }
  inject (injectServices) {
    injectServices.forEach(serviceName => {
      this[serviceName] = services.use(serviceName)
    })
  }
}

export default BaseService
