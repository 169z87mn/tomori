<template>
  <div id="app">
    <NavBar />
    <RadioTab />
  </div>
</template>

<script>
import NavBar from './components/header/nav-bar'
import RadioTab from './components/radio/radio-tab'

export default {
  name: 'App',
  components: {
    NavBar,
    RadioTab
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