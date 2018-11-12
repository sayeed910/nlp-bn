import Vue from 'vue'
import Router from 'vue-router'

const Home = () => import('./views/Home');
const SpellChecker = () => import('./views/SpellChecker');
const HmmTagger = () => import('./views/HmmTagger');

Vue.use(Router);

export default new Router({
    routes: [

        {
            path: '/',
            name: 'Home',
            component: Home
        }, {
            path: '/spell-checker',
            name: 'SpellChecker',
            component: SpellChecker
        }, {
            path: '/hmm-tagger',
            name: 'HmmTagger',
            component: HmmTagger
        },

    ]
})
