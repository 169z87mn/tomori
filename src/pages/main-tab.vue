<template>
  <div>
    <v-tabs>
      <v-tab>
        Radio
      </v-tab>
      <v-tab-item>
        <RadioTab />
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import RadioTab from '../components/radio/radio-tab'

export default {
  components: {
    RadioTab
  },
  data: () => {
    
  }
}
</script>

<style lang="scss">
</style>
