<template>
  <div>
    <b-button v-b-toggle.sidebar-1 variant="outline-info">
      <b-icon icon="list-nested" aria-label="list" aria-hidden="true" />
    </b-button>
    <b-sidebar
      id="sidebar-1"
      title="Sidebar"
      shadow
      backdrop
    >
      <div>a</div>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  
}
</script>

<style></style>