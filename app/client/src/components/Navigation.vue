<template>
  <div class="navigation-container">
    <router-link to="/">Home</router-link> |
    <router-link to="/signup">Sign Up</router-link> |
    <router-link to="/login">Log In</router-link> |
    <span @click="logout()">Log Out</span>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'Navigation',
  data () {
    return {
      userAuthService: services.use('userAuthService')
    }
  },
  methods: {
    logout () {
      this.userAuthService.logoutUser()
      this.$router.push({ name: 'LoginView' })
    }
  }
}
</script>

<style scoped lang="scss">
  div.navigation-container {
    padding: 30px;
    a, span {
      font-weight: bold;
      color: #2c3e50;
      cursor: pointer;
      text-decoration: underline;
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>
