import Vue from 'vue'
import vuetify from './plugins/vuetify'
import axios from 'axios'

import App from './App'
import router from './router'
import store from './store'

import '@mdi/font/css/materialdesignicons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'

const {remote} = require('electron')
const {app} = remote // or `const app = remote.app`
const child = require('child_process').spawn
const executablePath = `resources/app/backend/dist/StartPythonBackend/StartPythonBackend.exe`

const pythonProcess = child(executablePath, [])

console.log('v20')
app.on('window-all-closed', function () {
    app.quit()
    pythonProcess.kill('SIGKILL')
})

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
