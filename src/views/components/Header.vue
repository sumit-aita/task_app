<template>
  <v-card tile class="pa-2">
    <div
      grey 
      class ="text-h5 ma-2 title-style"
      v-text="title"
       />
  </v-card>
</template>

<script>
export default {
  props: {
    title: {type: String, required: true}
  },
  data() {
    return {

    }
  }
}
</script>

<style scoped>
.title-style {
  padding: 0 0 0px 20px;
  /* border-bottom: inset 2px #E4264E; */
  border-left: inset 4px #E4264E;
}
</style>