<template>
  <v-content>
    <v-toolbar fixed dark color="primary">
      <v-btn icon dark @click.native="$router.go(-1)">
              <v-icon>keyboard_backspace</v-icon>
            </v-btn>
      <v-toolbar-title>HMM Tagger</v-toolbar-title>
      <v-spacer></v-spacer>

    </v-toolbar>
    <v-container fill-height fluid>
      <v-layout justify-center align-center>
        <v-flex md12>

          <v-layout justify-center class="mb-5">
            <v-btn v-if="status !== 'edit'" color="indigo" dark class="mt-3" @click="startEditing"><v-icon>edit</v-icon>Edit</v-btn>
            <v-btn v-if="status === 'edit'" color="indigo" dark class="mt-3" @click="getTags">Get Tags</v-btn>
          </v-layout>
          <v-layout justify-center>
            <v-flex md1 v-for="(item, index) in items" :key="index" v-if="status !== 'edit'">
              <v-card>
                <v-card-title>{{item.word}}</v-card-title>
                <v-card-text>{{item.tag}}</v-card-text>
              </v-card>
            </v-flex>
            <v-textarea
                    v-if="status === 'edit'"
                    class="large elevation-3" :row-height="40"
                    auto-grow
                    solo
                    name="input-7-4"
                    placeholder="Enter your text ..."
                    flat
                    v-model="text"
            ></v-textarea>
          </v-layout>

        </v-flex>

      </v-layout>

    </v-container>

  </v-content>
</template>

<script>
    import faker from 'faker';
    import _ from 'lodash';
    import $backend from '../backend'

    export default {
        name: "SpellChecker",
        data() {
            return {
                text: "",
                status: 'edit',
                items: [],
                fixedByDialog: false,
                checking: false,
                menu: false,
                step: 1
            }
        },
        methods: {
            getTags(){
                $backend.post('hmm', {text: this.text})
                    .then(({data}) => {
                        const words = this.text.split(" ");
                        this.items = words.map((value, index, arr) => ({word: value, tag: data.tags[index]}));
                        this.status = 'show'
                    });

            },
            startEditing(){
                this.text = "";
                this.status = 'edit';
                this.items = [];

            }
        },
        watch: {

        },

    }
</script>

<style>
  .v-card {
    font-size: 25px;
  }
  .v-textarea {
    font-size: 24px !important;

  }

  .v-textarea textarea {
    line-height: 50px !important;
  }

  .v-input--is-focused {
    box-shadow: 0px 6px 6px -3px rgba(0, 0, 0, 0.2), 0px 10px 14px 1px rgba(0, 0, 0, 0.14), 0px 4px 18px 3px rgba(0, 0, 0, 0.12) !important;
  }

  /*.v-textarea:focus {*/
  /*box-shadow: 0px 7px 8px -4px rgba(0, 0, 0, 0.2), 0px 12px 17px 2px rgba(0, 0, 0, 0.14), 0px 5px 22px 4px rgba(0, 0, 0, 0.12) !important;*/
  /*}*/

</style>