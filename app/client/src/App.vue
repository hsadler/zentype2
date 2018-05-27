<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view/>
  </div>
</template>

<script>
import services from '@/services'
import Navigation from '@/components/Navigation'

export default {
  name: 'App',
  props: {},
  data () {
    return {
      userAuthService: services.use('userAuthService')
    }
  },
  components: {
    Navigation
  }
}
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;

    // testing
    * {
      // border: 1px dotted green;
    }

  }
</style>
