<template>
  <div class="home-container">
    <h1>Home page</h1>
    <p>You're home!</p>
    <p>Logged in: {{ authStatus }}</p>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'HomePage',
  data () {
    return {
      localStorageService: services.use('localStorageService'),
      authStatus: false
    }
  },
  created () {
    const authToken = this.localStorageService.get('authToken')
    if (authToken) {
      this.authStatus = true
    }
  },
  methods: {}
}
</script>

<style scoped lang="scss">
  div.home-container {}
</style>
