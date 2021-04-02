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
    },
    ExplicitYValues () {
      return this.$store.getters.getExplicitYValues
    },
    ImplicitYValues () {
      return this.$store.getters.getImplicitYValues
    }
  },
  watch: {
    yValues () {
      let _datasets = []
      _datasets.push(this.createFunctionObject(this.yValues, 'Аналитическое', 'rgb(75, 192, 192)'))
      if (this.ExplicitYValues.length !== 0) {
        _datasets.push(this.createFunctionObject(this.ExplicitYValues, 'Явная', 'rgb(192, 75, 163)'))
      }
      if (this.ImplicitYValues.length !== 0) {
        _datasets.push(this.createFunctionObject(this.ImplicitYValues, 'Неявная', 'rgb(39, 255, 0)'))
      }
      const chartData = {
        type: 'line',
        data: {
          labels: this.xValues,
          datasets: _datasets
        },
        options: {
          width: 400,
          height: 400,
          responsive: true,
          lineTension: 1,
          tooltips: {
            mode: 'index',
            intersect: false
          },
          hover: {
            mode: 'nearest',
            intersect: true
          },
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false,
                padding: 10
              },
              scaleLabel: {
                display: true,
                labelString: 'Температура, К'
              }
            }],
            xAxes: [{
              ticks: {
                beginAtZero: true,
                padding: 10
              },
              scaleLabel: {
                display: true,
                labelString: 'Широта, θ'
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
    },
    createFunctionObject (yValues, name, color) {
      return {
        label: name,
        data: yValues,
        borderWidth: 3,
        borderColor: color,
        fill: false,
        pointRadius: 0
      }
    }
  }
}
</script>

<style scoped>

</style>
