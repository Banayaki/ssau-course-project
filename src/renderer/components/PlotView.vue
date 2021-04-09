<template>
  <div class="body">
    <v-card class="m-2 p-2" color="background">
      <v-card-title>
        <v-spacer></v-spacer>
        <h2>График функции</h2>
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text>
        <v-card>
          <canvas id="chart"></canvas>
        </v-card>
      </v-card-text>
    </v-card>

    <v-card class="m-2 p-2" color="background">
      <v-card-title>
        <v-spacer></v-spacer>
        <span>Параметры визуализации:</span>
        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text>
        <v-card class="pb-5">
          <v-row dense justify="center" no-gutters>
            <v-col align-self="center" class="ml-10" cols="5">
              <v-switch v-model="lineSmoothing"
                        color="blue" dense
                        hide-details label="Сглаживание графиков"></v-switch>
            </v-col>
          </v-row>
        </v-card>
      </v-card-text>
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
      planetChartData: planetChartData,
      lineSmoothing: 1
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
      let settings = {
        label: name,
        data: yValues,
        borderWidth: 3,
        borderColor: color,
        fill: false,
        pointRadius: 0
      }
      console.log(this.lineSmoothing)
      if (this.lineSmoothing) {
        settings['cubicInterpolationMode'] = true
      } else {
        settings['lineTension'] = 0
      }
      return settings
    }
  }
}
</script>

<style scoped>

</style>
