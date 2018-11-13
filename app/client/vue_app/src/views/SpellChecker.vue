<template>
  <v-content>
    <v-toolbar fixed dark color="primary">
      <v-toolbar-title>Spell Checker</v-toolbar-title>
      <v-spacer></v-spacer>

    </v-toolbar>
    <v-container fill-height fluid>
      <v-layout justify-center align-center>
        <v-flex md7>
          <v-layout justify-end>
            <v-menu
                    v-model="menu"
                    :close-on-content-click="false"
                    :nudge-width="200"
                    offset-x
            >
              <v-btn color="indigo" dark class="mt-3" @click="check" slot="activator">Fix</v-btn>

              <v-card>
                <v-window v-model="step">
                  <v-window-item :value="1">
                    <v-card>
                      <v-card-actions>
                        <v-btn :disable="checking" @click="step++" flat>Start</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-window-item>
                  <!--<v-window-item :value="2">-->
                  <!--<v-card>abcde-->
                  <!--<v-card-actions>-->
                  <!--<v-btn @click="step++">Next</v-btn>-->
                  <!--</v-card-actions>-->
                  <!--</v-card>-->
                  <!--</v-window-item>-->
                  <!--<v-window-item :value="3">-->
                  <!--<v-card>abcde-->
                  <!--<v-card-actions>-->
                  <!--<v-btn @click="step++">Next</v-btn>-->
                  <!--</v-card-actions>-->
                  <!--</v-card>-->
                  <!--</v-window-item>-->

                  <v-window-item v-for="(correction, index) in corrections" :key="index" :value="index+2">

                    <v-card>
                      <v-card-title>{{correction.word}}</v-card-title>


                      <v-divider></v-divider>
                      <v-card-text>

                        <v-list>
                          <v-list-tile @click="fix(correction.index, idx, index)"
                                       v-for="(word, idx) in correction.fixes"
                                       :key="idx">
                            <v-list-tile-title>{{word}}</v-list-tile-title>
                          </v-list-tile>
                        </v-list>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" flat @click="ignore">Ignore</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-window-item>
                </v-window>
              </v-card>
            </v-menu>

          </v-layout>
          <div>
            <v-textarea
                    class="large elevation-3" :row-height="40"
                    auto-grow
                    solo
                    name="input-7-4"
                    placeholder="Enter your text ..."
                    flat
                    v-model="text"
            ></v-textarea>
          </div>

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
                corrections: null,
                fixedByDialog: false,
                checking: false,
                menu: false,
                step: 1
            }
        },
        methods: {
            check() {
                this.checking = true;
                $backend.post('/checker', {text: this.text})
                    .then(({data}) => {
                        console.log(data);
                        const words = this.text.split(" ");
                        const corrections = data.corrections;

                        this.corrections = _.compact(corrections.map((value, index, arr) => {
                            if (value !== 'OK') {
                                return {word: words[index], index: index, fixes: value}
                            } else {
                                return undefined
                            }
                        }));
                        this.checking = false;
                        this.step=1;
                    })
            },
            fix(wordIdx, fixIdx, correctionIdx) {
                const words = this.text.split(" ");
                words[wordIdx] = this.corrections[correctionIdx].fixes[fixIdx];
                this.fixedByDialog = true;
                this.text = words.join(" ");
                this.ignore();
            },
            ignore() {
                console.log(this.step);
                if (this.step >= this.corrections.length + 1) {
                    this.menu = false;
                } else {
                    this.step++;
                }
            }
        },
        watch: {
            text(value) {
                const check = _.debounce((text) => {
                    this.checking = true;


                }, 1500, {leading: true});

                //changed by fix dialog
                if (this.fixedByDialog) {
                    this.fixedByDialog = false;
                    return true;
                }

                //Already sent a request
                if (this.checking) {
                    return true;
                }

                check(value);

            }

        },

    }
</script>

<style>
  .v-textarea {
    font-size: 50px !important;

  }

  .v-textarea textarea {
    line-height: 80px !important;
  }

  .v-input--is-focused {
    box-shadow: 0px 6px 6px -3px rgba(0, 0, 0, 0.2), 0px 10px 14px 1px rgba(0, 0, 0, 0.14), 0px 4px 18px 3px rgba(0, 0, 0, 0.12) !important;
  }

  /*.v-textarea:focus {*/
  /*box-shadow: 0px 7px 8px -4px rgba(0, 0, 0, 0.2), 0px 12px 17px 2px rgba(0, 0, 0, 0.14), 0px 5px 22px 4px rgba(0, 0, 0, 0.12) !important;*/
  /*}*/

</style>