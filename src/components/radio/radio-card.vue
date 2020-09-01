<template>
  <b-card
    class="radioCard"
    :title=radio.screen_title
  >
    <b-card-text>
      <li v-for="(psn, i) in radio.personality" :key="i">{{psn}}</li>
    </b-card-text>
  </b-card>
</template>

<script>
export default {
  props: {
    radio: Object
  },
  data: () => ({
  }),
  created() {
    console.log(this.radio)
  }
}
</script>

<style>
.radioCard {
  max-width: 25rem;
}
</style>