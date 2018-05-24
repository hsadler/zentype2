
class Services {
  constructor () {
    this.registry = {}
  }
  registerServices (servicesToRegister) {
    // add services to registry
    for (var serviceName in servicesToRegister) {
      const service = servicesToRegister[serviceName]
      this.registry[serviceName] = service
    }
    // inject services into one another
    for (var sName in this.registry) {
      const service = this.registry[sName]
      service.inject(service.injectServices)
    }
  }
  use (serviceName) {
    return this.registry[serviceName]
  }
}

export default new Services()
