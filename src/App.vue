<template>
  <div id="app">
    <NavBar/>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/header/nav-bar'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
* {
  font-family: Arial, Helvetica, sans-serif;
}
#app {
  background-color: #DEDEDE;
  height: 100rem;
}
</style>