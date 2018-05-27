<template>
  <div class="home-container">
    <h1>Home page</h1>
    <p>You're home!</p>
    <p>Logged in: {{ isAuth }}</p>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'HomePage',
  data () {
    const userAuthService = services.use('userAuthService')
    return {
      isAuth: userAuthService.isAuth
    }
  }
}
</script>

<style scoped lang="scss">
  div.home-container {}
</style>
