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
                <v-span>Параметры уравнения:</v-span>
                <v-spacer></v-spacer>
            </v-card-title>
            <v-card-text>
                <v-list>
                    <v-list-item v-bind:key="name" v-for="name in getEqParametersNames">
                        <v-row dense justify="center" no-gutters>
                            <v-col class="align-self-center mr-5" cols="3">
                                <span class="font-weight-bold float-right">{{name}}:</span>
                            </v-col>
                            <v-col cols="3">
                                <v-text-field :value="getParameterValue(name)" @input="setParameterValues(name, $event)"
                                              clearable color="accent" dense
                                              filled
                                              hide-details></v-text-field>
                            </v-col>
                            <v-col cols="2"></v-col>
                        </v-row>
                    </v-list-item>
                </v-list>
            </v-card-text>
        </v-card>

        <v-card class="m-2 p-2" color="background">
            <v-card-title>
                <v-spacer></v-spacer>
                <v-span>Параметры вычислений:</v-span>
                <v-spacer></v-spacer>
            </v-card-title>
            <v-card-text>
                <v-list>
                    <v-list-item v-bind:key="name" v-for="name in getScriptParametersNames">
                        <v-row dense justify="center" no-gutters>
                            <v-col class="align-self-center mr-5" cols="3">
                                <span class="font-weight-bold float-right">{{name}}:</span>
                            </v-col>
                            <v-col cols="3">
                                <v-text-field :value="getParameterValue(name)" @input="setParameterValues(name, $event)"
                                              clearable color="accent" dense
                                              filled
                                              hide-details></v-text-field>
                            </v-col>
                            <v-col cols="2"></v-col>
                        </v-row>
                    </v-list-item>
                </v-list>
            </v-card-text>
        </v-card>

        <v-card class="m-2 p-2" color="background">
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="solveEquation" color="success">Вычислить</v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>

    </div>
</template>

<script>
    import {SET_PARAMETER_VALUE, SOLVE_EQUATION} from '../store/modules/Equation'

    export default {
        name: 'EquationView',
        data () {
            return {}
        },
        computed: {
            getEqParametersNames () {
                return this.$store.getters.getEqParametersNames
            },
            getScriptParametersNames () {
                return this.$store.getters.getScriptParametersNames
            }
        },
        methods: {
            getParameterValue (name) {
                return this.$store.getters.getParameters[name]
            },
            setParameterValues (name, value) {
                value = Number(value)
                this.$store.dispatch(SET_PARAMETER_VALUE, {name, value})
            },
            solveEquation () {
                console.log('here')
                this.$store.dispatch(SOLVE_EQUATION)
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
