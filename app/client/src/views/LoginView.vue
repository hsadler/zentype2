<template>
  <div class="login-view-container">
    <h1>Log In</h1>
    <label>email</label>
    <br>
    <input type="email" v-model="userEmail" autofocus>
    <br>
    <label>password</label>
    <br>
    <input type="password" v-model="userPassword">
    <br>
    <button @click="loginUser()">Submit</button>
    <br>
    <span>{{ errorMessage }}</span>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'LoginView',
  data () {
    return {
      userAuthService: services.use('userAuthService'),
      userEmail: null,
      userPassword: null,
      errorMessage: null
    }
  },
  methods: {
    loginUser () {
      this.errorMessage = null
      if (this.userEmail && this.userPassword) {
        this.userAuthService.loginUser(this.userEmail, this.userPassword)
          .then(status => {
            if (status) {
              this.$router.push({ name: 'HomeView' })
            } else {
              this.errorMessage = 'Something went wrong..'
            }
          })
      }
    }
  }
}
</script>

<style scoped lang="scss">
  div.login-view-container {
    max-width: 400px;
    text-align: left;
    margin: 0 auto;
    input {
      margin-bottom: 10px;
    }
    button {
      margin-top: 10px;
    }
  }
</style>
