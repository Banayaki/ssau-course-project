import Vue from 'vue'
import vuetify from './plugins/vuetify'
import axios from 'axios'

import App from './App'
import router from './router'
import store from './store'

import '@mdi/font/css/materialdesignicons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'

// const child = require('child_process').execFile
// const executablePath = `resources/app.asar/dist/StartPythonBackend.exe`
//
// child(executablePath, function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }
//
//     console.log(data.toString())
// })

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    components: {App},
    template: '<App/>',
    vuetify,
    router,
    store
}).$mount('#app')
