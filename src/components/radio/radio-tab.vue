<template>
  <div>
    <b-tabs pills card>
      <b-tab v-for="(tab, i) in tabs" :key="i" :title="tab">
        <RadioList :tab="i"/>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import RadioList from './radio-list'

export default {
  components: {
    RadioList
  },
  data: () => ({
    tabs: ["月"] //"火", "水", "木", "金", "土", "日"]
  })
}
</script>