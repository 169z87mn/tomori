<template>
  <div>
    <v-tabs v-model="tab" fixed-tabs background-color="indigo">
      <v-tab v-for="(tab, i) in tabs" :key="i">
        {{ tab }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item v-for="(tab, i) in tabs" :key="i">
        <RadioList :tab="i" />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import RadioList from './radio-list'

export default {
  components: {
    RadioList
  },
  data: () => ({
    tab: null,
    tabs: ["月", "火", "水", "木", "金", "土", "日"]
  })
}
</script>

<style lang="scss" scoped>
</style>