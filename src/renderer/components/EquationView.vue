<template>
  <div class="body">
    <v-card class="m-2 p-2" color="background">
      <v-row class="mb-3" no-gutters>
        <v-spacer></v-spacer>
        <h2>Решение дифференциального уравнения</h2>
        <v-spacer></v-spacer>
      </v-row>
      <v-row class="mb-3" no-gutters>
        <img class="equation" src="../assets/equation.svg">
      </v-row>
    </v-card>

    <v-card class="m-2 p-2" color="background">
      <v-card-title>
        <v-spacer></v-spacer>
        <span>Параметры уравнения:</span>
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text>
        <v-card>
          <v-list>
            <v-list-item v-for="name in getEqParametersNames" v-bind:key="name">
              <v-row dense justify="center" no-gutters>
                <v-col class="align-self-center mr-5" cols="3">
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <span v-bind="attrs" v-on="on" class="font-weight-bold float-right">{{ name }}:</span>
                    </template>
                    <span>{{ parametersNaming[name] }}</span>
                  </v-tooltip>
                </v-col>
                <v-col cols="3">
                  <v-text-field v-model.number="parameters[name]"
                                :hint="hints[name]"
                                :rules="[rules.bigRule(name, parameters[name])]"
                                clearable
                                color="accent"
                                dense
                                filled
                                type="number"></v-text-field>
                </v-col>
                <v-col cols="2"></v-col>
              </v-row>
            </v-list-item>
          </v-list>
        </v-card>
      </v-card-text>
    </v-card>

    <v-card class="m-2 p-2" color="background">
      <v-card-title>
        <v-spacer></v-spacer>
        <span>Параметры численного решения:</span>
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text>
        <v-card>
          <v-row dense justify="center" no-gutters>
            <v-col align-self="center" class="ml-10" cols="5">
              <v-switch v-for="name in getAvailableSolvers" v-bind:key="name" v-model="parameters[name]"
                        :label="parametersNaming[name]" color="blue"
                        dense hide-details></v-switch>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <v-switch v-model="parameters['force_stability']" color="blue"
                              dense hide-details label="Коррекция"></v-switch>
                  </div>
                </template>
                <span>{{ parametersNaming['force_stability'] }}</span>
              </v-tooltip>
            </v-col>
            <v-col cols="6">
              <v-list class="pt-6">
                <v-list-item v-for="name in getNumericalParametersNames" v-bind:key="name">
                  <v-col class="align-self-center mr-5 mb-4" cols="3">
                    <v-tooltip top>
                      <template v-slot:activator="{ on, attrs }">
                        <span v-bind="attrs" v-on="on" class="font-weight-bold float-right">{{ name }}:</span>
                      </template>
                      <span>{{ parametersNaming[name] }}</span>
                    </v-tooltip>
                  </v-col>
                  <v-text-field v-model.number="parameters[name]"
                                :hint="hints[name]"
                                :rules="[rules.bigRule(name, parameters[name])]"
                                clearable
                                color="accent"
                                dense
                                filled
                                type="number"></v-text-field>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row>
        </v-card>
      </v-card-text>
    </v-card>

    <v-card class="m-2 p-2" color="background">
      <v-card-text v-if="errors" class="text-danger font-weight-bold text-center">
        Указаны некорректные значения коэффициентов дифференциального уравнения
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn :disabled="waitingForResponse" color="success" @click="solveEquation">
          <v-progress-circular
              v-if="waitingForResponse"
              color="black"
              indeterminate
          ></v-progress-circular>
          <span v-else>Вычислить</span>
        </v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>

    <v-card v-if="!getStabilityStatus.stable" class="m-2 p-2" color="background">
      <v-card-title>
        <span>Явная схема неустойчива</span><br>
        <span
            v-if="getStabilityStatus.newNt">Мелкость разбиения по времени была пересчитана. Используем Nt = {{
            getStabilityStatus.newNt
          }}</span>
      </v-card-title>
    </v-card>

  </div>
</template>

<script>
import {SET_PARAMETER_VALUE, SET_WAITING, SOLVE_EQUATION} from '../store/modules/Equation'

export default {
  name: 'EquationView',
  data () {
    return {
      parametersNaming: {
        'K': 'Коэффициент теплопроводности (k)',
        'C': 'Объемная теплоемкость (c)',
        'R': 'Раидус (R)',
        'T': 'Временной промежуток (T)',
        'Nx': 'Мелкость разбиения по X (Nx)',
        'Nt': 'Мелкость разбиения по T (Nt)',
        'Implicit': 'Неявная схема',
        'Explicit': 'Явная схема',
        'force_stability': 'Автоматическая коррекция мелкости при неудовлетворении условия устойчивости'
      },
      hints: {
        'K': 'K > 0',
        'C': 'C > 0',
        'R': 'R > 0',
        'T': 'T >= 0',
        'Nx': '0 < Nx < 2000',
        'Nt': '0 < Nt < 2000'
      },
      rules: {
        bigRule (name, value) {
          if (name === 'Implicit' || name === 'Explicit' || name === 'force_stability') {
            return true
          } else if (isNaN(parseFloat(value))) {
            return false
          } else if (name === 'T') {
            return value >= 0
          } else if (name === 'Nx' || name === 'Nt') {
            return value > 0 && value < 2000
          } else {
            return value > 0
          }
        }
      },
      errors: false,
      parameters: Object.assign({}, this.$store.getters.getParameters)
    }
  },
  created () {
    this.$store.dispatch(SET_WAITING, false)
    if (!this.checkParameters) {
      setTimeout(this.solveEquation, 2000)
    }
  },
  computed: {
    getEqParametersNames () {
      return this.$store.getters.getEqParametersNames
    },
    getNumericalParametersNames () {
      return this.$store.getters.getNumericalParametersNames
    },
    getAvailableSolvers () {
      return this.$store.getters.getAvailableSolvers
    },
    waitingForResponse () {
      return this.$store.getters.getWaitingStatus
    },
    getStabilityStatus () {
      return this.$store.getters.getStabilityStatus
    }
  },
  methods: {
    checkParameters () {
      for (const [key, value] of Object.entries(this.parameters)) {
        const check = this.rules.bigRule(key, value)
        if (!check) {
          return true
        }
      }
      return false
    },
    setParameterValues (name, value) {
      value = Number(value)
      this.$store.dispatch(SET_PARAMETER_VALUE, {name, value})
    },
    solveEquation () {
      this.errors = this.checkParameters()
      if (this.errors) {
        return
      }
      this.$store.dispatch(SOLVE_EQUATION, this.parameters)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>
.equation {
  width: 100%;
  height: 100px;
}

</style>
