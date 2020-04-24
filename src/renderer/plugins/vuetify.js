import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify, {})

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#e1f5fe',
                secondary: '#ffffff',
                accent: '#afc2cb',
                background: '#f5f5f6'
            }
        }
    }
})
