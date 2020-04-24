<template>
    <div class="body">
        <v-card class="m-2 p-2" color="background">
            <v-row class="mb-3" no-gutters>
                <v-spacer></v-spacer>
                <h2>График функции</h2>
                <v-spacer></v-spacer>
            </v-row>
        </v-card>

        <v-card class="m-2 p-2" color="background">
            <canvas id="planet-chart"></canvas>
        </v-card>
    </div>
</template>

<script>
    import Chart from 'chart.js'
    import {planetChartData} from '../data/CharTestDataset'

    export default {
        name: 'PlotView',
        data () {
            return {
                planetChartData: planetChartData
            }
        },
        mounted () {
            this.createChart('planet-chart', this.planetChartData)
        },
        methods: {
            createChart (chartId, chartData) {
                const ctx = document.getElementById(chartId)
                // eslint-disable-next-line no-unused-vars
                const myChart = new Chart(ctx, {
                    type: chartData.type,
                    data: chartData.data,
                    options: chartData.options
                })
            }
        }
    }
</script>

<style scoped>

</style>
