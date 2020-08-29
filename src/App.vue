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

<style></style>
