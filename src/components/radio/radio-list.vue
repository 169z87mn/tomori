<template>
  <div>
    <b-card-group deck>
      <RadioCard v-for="(radio, key) in radios" :key="key" :radio="radio">
      </RadioCard>
    </b-card-group>
  </div>
</template>

<script>
import axios from "axios"
import RadioCard from './radio-card'

export default {
  props: {
    tab: Number
  },
  components: {
    RadioCard
  },
  data: () => ({
    radios: Array
  }),
  created() {
    const api = process.env.VUE_APP_API_GATEWAY_URL
    let data = {"weekday": this.tab}
    axios.post(api, data).then((result) => {
      this.radios = result.data
    }).catch((err) => {
      console.log(err)
    });
  }
}
</script>

<style>
RadioCard {
  background-color: #F8F8F7;
}
</style>