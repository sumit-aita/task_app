<template>
  <v-app-bar dark app elevation="10">
    <v-menu v-if="false" offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-app-bar-nav-icon
          dark
          v-bind="attrs"
          v-on="on"
        >
        </v-app-bar-nav-icon>
      </template>
      <v-list>
        <v-list-item @click='$router.push("/")'>
          <v-list-item-title>A</v-list-item-title>
        </v-list-item>
        <v-list-item @click='$router.push("/")'>
          <v-list-item-title>B</v-list-item-title>
        </v-list-item>
        <v-list-item @click='$router.push("/")'>
          <v-list-item-title>C</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-toolbar-title>TO DO APP</v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {
  data(){
    return{
        
    }
  }
}
</script>