<template>
  <div>
    <v-card-group deck>
      <RadioCard v-for="(radio, key) in radios" :key="key" :radio="radio" />
    </v-card-group>
  </div>
</template>

<script>
import axios from "axios"
import RadioCard from './radio-card'

export default {
  components: {
    RadioCard
  },
  props: {
    tab: {
      type: Number,
      default: null
    }
  },
  data: () => ({
    radios: Array
  }),
  created() {
    const api = process.env.VUE_APP_API_GATEWAY_URL
    console.log("axios get")
    let data = {
      "weekday": this.tab
    }
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