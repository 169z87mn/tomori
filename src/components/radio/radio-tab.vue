<template>
  <b-card class="radioTab" no-body>
    <b-tabs pills card>
      <b-tab v-for="(tab, i) in tabs" :key="i" :title="tab" varient="Secondary">
        <RadioList :tab="i"/>
      </b-tab>
    </b-tabs>
  </b-card>
</template>

<script>
import RadioList from './radio-list'

export default {
  components: {
    RadioList
  },
  data: () => ({
    tabs: ["月", "火", "水", "木", "金", "土", "日"]
  })
}
</script>

<style lang="scss">
.radioTab {
  margin: 40px 20px 40px 20px;
}
.nav-pills .nav-link.active, .nav-pills .show > .nav-link {
  color: #000000;
  background-color: #B5D8CC;
}
.card-header {
  background-color: #232C33;
}
.card-header > ul > li > a {
  color: #F8F8F7;
  background-color: #232C33;
}
.nav-link {
    margin: 0rem 0.5rem;
    padding: 0.5rem 2rem;
}
</style>