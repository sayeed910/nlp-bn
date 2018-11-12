<template>
  <v-content>
    <v-toolbar fixed dark color="primary">
      <v-toolbar-title>Natural Language Processing</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>

        <v-btn @click="aboutDialog=true" flat>About Us</v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-container fluid fill-height>
      <v-layout justify-center align-center>
        <v-flex md4 class="ma-4">
          <v-card class="tile" @click.native="goto('hmm-tagger')">
            <v-card-text class="text-md-center">
              <div class="large-text title-text">POS</div>
              <div class="text-uppercase mt-4 display-1">
                hmm tagger
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex md4 class="ma-4">
          <v-card class="tile" @click.native="goto('spell-checker')">
            <v-card-text class="text-md-center">
              <div class="mt-3">
                <v-icon color="#481f5c">search</v-icon>
              </div>

              <div class="text-uppercase mt-5 display-1">
                spell checker
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <div>
      <v-dialog v-model="aboutDialog" fullscreen hide-overlay transition="dialog-bottom-transition">
        <v-card>
          <v-toolbar dark color="primary">
            <v-btn icon dark @click.native="aboutDialog = false">
              <v-icon>keyboard_backspace</v-icon>
            </v-btn>
            <v-toolbar-title>About Us</v-toolbar-title>

          </v-toolbar>

          <v-container grid-list-xl>
            <v-layout align-center justify-center row>
              <author-details :details="authors[0]"></author-details>
            </v-layout>
            <v-layout align-center row wrap class="mt-5">


              <author-details :details="author" v-for="author in authors.slice(1)" :key="author.name"></author-details>

            </v-layout>
          </v-container>


        </v-card>
      </v-dialog>
    </div>


  </v-content>

</template>

<script>
  import AuthorDetails from '../components/AuthorDetails'
  import sayeedImage from '../assets/sayeed.jpg'
  import shohan from '../assets/shohan.jpg'
  import safayat from '../assets/safayat.jpg'
    export default {
        name: "Home",
        components: {
            authorDetails: AuthorDetails
        },
        data() {
            return {
                aboutDialog: false,
                authors: [
                    {name: 'tahsin al sayeed', email: 'tahsinalsayeed@gmail.com', color: '#2386e3', image: sayeedImage},
                    {name: 'safayat ullah', email: 'sumishu95@gmail.com', color: '#cc10ed', image:safayat},
                    {name: 'jishan hasnain', email: 'hasnainjishan@gmail.com', color: '#ed2045'},
                    {name: 'jobayed ullah shuvo', email: 'shuvo.pma@gmail.com', color: '#3a7645'},
                    {name: 'AN siddiky shohan', email: 'anssducse@gmail.com', color: '#1813ed', image: shohan},
                ]
            }
        },
        methods: {
            goto(route){
                console.log(route);
                this.$router.push(route);
            }
        }
    }
</script>

<style scoped>

  .tile .v-icon {
    font-size: 120px;
    text-align: center;
  }

  .large-text {
    font-size: 110px;
  }

  .title-text {
    color: #3a536b;
  }

  .tile {
    min-height: 300px;
    cursor: pointer;
  }

  .tile:hover {
    box-shadow: 0px 7px 8px -4px rgba(0, 0, 0, 0.2), 0px 12px 17px 2px rgba(0, 0, 0, 0.14), 0px 5px 22px 4px rgba(0, 0, 0, 0.12) !important;
  }

</style>