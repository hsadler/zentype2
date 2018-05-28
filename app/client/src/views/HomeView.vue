<template>
  <div class="home-container">
    <h1>Home page</h1>
    <p>You're home!</p>
    <p>Logged in: {{ isAuth }}</p>
    <p>Email: {{ userEmail }}</p>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'HomePage',
  data () {
    const userAuthService = services.use('userAuthService')
    const userService = services.use('userService')
    return {
      userAuthService,
      userService
    }
  },
  computed: {
    isAuth () {
      return this.userAuthService.getIsAuth()
    },
    userEmail () {
      return this.userService.getEmail()
    }
  }
}
</script>

<style scoped lang="scss">
  div.home-container {}
</style>
