<template>
  <div class="out_graph">
    <div class="in_graph">
      <h1 id="text" class="font-weight-thin">Stress Graph</h1>
      <v-btn @click="Popup">날짜별 사건보기</v-btn>
      <canvas id="planet-chart"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'
import SituationPopup from './situation'

export default {
  name: 'Graph',
  data () {
    return {
      ajouData: {
        type: 'line',
        data: { // 해당 일자와 해당 일자에 스트레스 받은 사람의 수
          labels: [],
          datasets: [
            { // another line graph
              label: 'Ajou University(dc-inside)',
              data: [],
              backgroundColor: [
                'rgba(71, 183,132,.5)' // Green
              ],
              borderColor: [
                '#47b784'
              ],
              borderWidth: 3
            }
          ]
        },
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
                padding: 25
              }
            }]
          }
        }
      }
    }
  },
  methods: {
    createChart (chartId, chartData) {
      const ctx = document.getElementById(chartId)
      const chart = this.myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      })
    },
    getData () {
      this.$http.get('/api/graph/data')
        .then(res => {
          console.log(res.data)
          this.ajouData.data.labels = res.data.date
          this.ajouData.data.datasets[0].data = res.data.data
          this.myChart.update()
        })
    },
    Popup () {
      this.$modal.show(SituationPopup, {
        modal: this.$modal
      }, {
        name: 'dynamic-modal',
        width: '600px',
        height: '500px',
        draggable: true,
        clickToClose: false
      })
    }
  },
  created () {
    this.getData()
  },
  mounted () {
    this.createChart('planet-chart', this.ajouData)
  },
  beforeRouteUpdate () {
    this.getData()
  }
}
</script>

<style scoped>
  div.out_graph{
    text-align: center;
  }

  div.in_graph{
    display: inline-block;
  }
  #planet-chart{
    height: 750px;
    width: 1400px;
  }
  #text{
    margin-top: 100px;
  }
</style>
