<template>
  <div class="signup-view-container">
    <h1>Sign Up</h1>
    <label>email</label>
    <br>
    <input type="email" v-model="userEmail" autofocus>
    <br>
    <label>password</label>
    <br>
    <input type="password" v-model="userPassword">
    <br>
    <label>confirm password</label>
    <br>
    <input type="password" v-model="userConfirmPassword">
    <br>
    <button @click="createUser()">Submit</button>
    <br>
    <span>{{ errorMessage }}</span>
  </div>
</template>

<script>
import services from '@/services'

export default {
  name: 'SignupView',
  props: {},
  data () {
    return {
      httpService: services.use('httpService'),
      userAuthService: services.use('userAuthService'),
      userEmail: null,
      userPassword: null,
      userConfirmPassword: null,
      errorMessage: null
    }
  },
  created () {},
  methods: {
    createUser () {
      this.errorMessage = null
      if (
        this.userEmail && this.userPassword &&
        this.userPassword === this.userConfirmPassword
      ) {
        this.userAuthService.createUser(this.userEmail, this.userPassword)
          .then(status => {
            if (status) {
              // TODO: redirect the user to profile here...
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
  div.signup-view-container {
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
