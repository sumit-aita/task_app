<template>
  <v-app dark>
    <v-main>
      <WebHeader />
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import WebHeader from '@/views/web_header/WebHeader';
export default {
  name: 'App',
  components: {
    WebHeader
  },
  data() {
    return {

    }
  }
};
</script>
