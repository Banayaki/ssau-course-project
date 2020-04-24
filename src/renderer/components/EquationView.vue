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
                    <v-list-item v-bind:key="name" v-for="(name, index) in eq_parameters_names">
                        <v-row dense justify="center" no-gutters>
                            <v-col class="align-self-center mr-5" cols="3">
                                <span class="font-weight-bold float-right">{{name}}:</span>
                            </v-col>
                            <v-col cols="3">
                                <v-text-field clearable
                                              color="accent" dense filled hide-details
                                              v-model="eq_parameters_values[index]"></v-text-field>
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
                    <v-list-item v-bind:key="name" v-for="(name, index) in script_parameters_names">
                        <v-row dense justify="center" no-gutters>
                            <v-col class="align-self-center mr-5" cols="3">
                                <span class="font-weight-bold float-right">{{name}}:</span>
                            </v-col>
                            <v-col cols="3">
                                <v-text-field clearable
                                              color="accent" dense filled hide-details
                                              v-model="script_parameters_values[index]"></v-text-field>
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
                <v-btn color="success">Вычислить</v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>

    </div>
</template>

<script>
    export default {
        name: 'EquationView',
        data () {
            return {
                eq_parameters_values: [0.59, 1.24, 5, 20],
                eq_parameters_names: ['K', 'C', 'R', 'T'],
                script_parameters_values: [0, 1, 1e-4],
                script_parameters_names: ['Левая граница', 'Правая граница', 'Погрешность']
            }
        },
        computed: {
            equationRender () {
                console.log('123')
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
