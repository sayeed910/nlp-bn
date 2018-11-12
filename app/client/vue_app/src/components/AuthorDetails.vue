<template>
  <v-flex xs3>
    <v-card :style="styleObject" class="elevation-6">
      <v-card-title>
        <v-avatar size="40px"><img :src="details.image" alt=""></v-avatar>
        <span class="title text-uppercase ml-2">{{details.name}}</span></v-card-title>
      <v-card-text>
        <p class="body-2">4th Year Undergraduate Student</p>
        <p class="body-2">Dept. of Computer Science and Engineering</p>
        <p class="body-2">University of Dhaka</p>
        <p class="body-2">{{details.email}}</p>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
    export default {
        props: {
            details: Object
        },
        name: "AuthorDetails",
        computed: {
            styleObject(){
                return {
                    borderTop: `3px solid ${this.details.color}`
                }
            }
        }
    }
</script>

<style scoped>

  .body-2 {
    font-size: 16px !important;
  }

</style>