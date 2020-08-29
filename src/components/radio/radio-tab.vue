<template>
  <div>
    <b-tabs pills card>
      <div v-for="(tab, i) in tabs" :key="i">
        <b-tab :title="tab">
          <RadioList :tab="i"/>
        </b-tab>
      </div>
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
    tabs: ["月", "火", "水", "木", "金", "土", "日"]
  })
}
</script>