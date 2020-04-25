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
            <canvas id="chart"></canvas>
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
                chart: null,
                planetChartData: planetChartData
            }
        },
        computed: {
            xValues () {
                return this.$store.getters.getXValues
            },
            yValues () {
                return this.$store.getters.getYValues
            }
        },
        watch: {
            yValues () {
                const chartData = {
                    type: 'line',
                    data: {
                        labels: this.xValues,
                        datasets: [{
                            label: 'f(x)',
                            data: this.yValues,
                            borderWidth: 3,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            fill: false,
                            pointRadius: 0
                        }]
                    },
                    options: {
                        width: 400,
                        height: 400,
                        responsive: true,
                        lineTension: 1,
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                    padding: 10
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: 'y'
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                    padding: 10
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: 'x'
                                }
                            }]
                        }
                    }
                }
                this.createChart(chartData)
            }
        },
        mounted () {
            this.chart = new Chart(document.getElementById('chart'), {type: 'line'})
        },
        methods: {
            createChart (chartData) {
                this.chart.data = chartData.data
                this.chart.options = chartData.options
                this.chart.update()
            }
        }
    }
</script>

<style scoped>

</style>
