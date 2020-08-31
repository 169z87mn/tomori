<template>
  <div>
    <b-card
      :title=radio.title
    >
      {{radio}}
    </b-card>
  </div>
</template>

<script>
export default {
  props: {
    radio: Object
  },
  created() {
    console.log(this.radio)
  } 
}
</script>