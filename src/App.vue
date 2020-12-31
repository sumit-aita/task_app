<template>
  <v-app dark>
    <v-main>
      <WebHeader />
      <router-view></router-view>
    </v-main>
    <Loading v-show="$store.state.loadingFlg"></Loading>
  </v-app>
</template>

<script>
import WebHeader from '@/views/web_header/WebHeader';
import Loading from '@/views/components/Loading'
export default {
  name: 'App',
  components: {
    WebHeader,
    Loading
  },
  data() {
    return {

    }
  }
};
</script>
