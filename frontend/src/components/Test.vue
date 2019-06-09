<template>
  <div class="twitter-template">
    <v-carousel  height="100%" :cycle="false" v-model="carousel_index"
                hide-delimiters
                hide-controls>
      <v-carousel-item>
        <div class="twitter-container py-5">
            <v-layout row wrap class="main-container bg-dark">
              <v-flex lg12 md12 class="disease-container" style="text-align: center;">
                    <b-card bg-variant="dark"
                            header="스트레스 테스트"
                            text-variant="white"
                            id="card_boardwrite">
                      <div>
                        <b-form @submit="onSubmit" v-if="show">
                          <b-form-group id="contentInput"
                                        label="자유롭게 글을 적어주세요."
                                        label-for="contentInput">
                            <b-form-textarea id="contentInput"
                                            v-model="form.contents"
                                            placeholder="기본적으로 50자 이상 써주셔야 정확한 판별이 가능합니다."
                                            :rows="20"
                                            :max-rows="30">
                            </b-form-textarea>
                          </b-form-group>
                          <b-button type="submit" variant="secondary">검사</b-button>
                        </b-form>
                      </div>
                    </b-card>
              </v-flex>
            </v-layout>
        </div>
      </v-carousel-item>
      <v-carousel-item>
          <div class="twitter-container py-5">
            <v-layout row wrap class="main-container">
              <v-flex lg6 md6 class="disease-container">
                <v-card color="blue-grey darken-2" class="white--text">
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">사용자 게시글 데이터
                        <v-btn @click="press_button()">Fetch</v-btn>
                      </div>
                    </div>
                  </v-card-title>
                </v-card>
              
                <v-card color="blue-grey darken-2" class="white--text mt-3">
                  <v-card-title primary-title>
                    <div>
                      <span class="twitter_info">AJOU UNIV.
                      사용자의 게시글 데이터를 분석합니다.</span>
                    </div>
                  </v-card-title>
                </v-card>

                <v-tabs
                  v-model="active"
                  color="blue-grey darken-2"
                  class="mt-3"
                  centered
                >
              <v-tabs-items v-model="tab">
                <v-tab-item :key="basic">
                  <v-card color="blue-grey darken-2" class="white--text">
                      <v-card-title primary-title>
                        <div>
                            <span class="twitter_text twitter_info text_base">
                              {{this.form.contents}}
                            </span>
                        </div>
                      </v-card-title>
                    </v-card>
                </v-tab-item>
                <v-tab-item :key="sad">
                  <v-card color="blue-grey darken-2" class="white--text">
                      <v-card-title primary-title>
                        <div>
                            <span class="twitter_text twitter_info text_sad">
                              {{this.form.contents}}
                            </span>
                        </div>
                      </v-card-title>
                    </v-card>
                </v-tab-item>
                <v-tab-item :key="adhd">
                  <v-card color="blue-grey darken-2" class="white--text">
                      <v-card-title primary-title>
                        <div>
                            <span class="twitter_text twitter_info text_adhd">
                              {{this.form.contents}}
                            </span>
                        </div>
                      </v-card-title>
                    </v-card>
                </v-tab-item>
                <v-tab-item :key="schizophrenia">
                  <v-card color="blue-grey darken-2" class="white--text">
                      <v-card-title primary-title>
                        <div>
                            <span class="twitter_text twitter_info text_schizophrenia">
                              {{this.form.contents}}
                            </span>
                        </div>
                      </v-card-title>
                    </v-card>
                </v-tab-item>
              </v-tabs-items>
                <v-tabs-slider color="white"></v-tabs-slider>

                <v-tab :key="basic">
                  기본
                </v-tab>
                <v-tab :key="sad">
                  우울증
                </v-tab>
                <v-tab :key="adhd">
                  ADHD
                </v-tab>
                <v-tab :key="schizophrenia">
                  정신분열증
                </v-tab>
              </v-tabs>

                <v-card color="blue-grey darken-2" class="white--text mt-3">
                  <v-card-actions>
                    <v-btn flat dark href='https://software.ajou.ac.kr' target="_blank"><i class="material-icons">touch_app</i>소프트웨어</v-btn>
                  </v-card-actions>
                </v-card>
              </v-flex>
              <hr/>
              <v-flex lg3 md3 class="pie-container">
                <div class="out_graph mb-2">
                  <div class="in_graph">
                    <div class="graph_title">
                      각 질환별 Probabilty
                    </div>
                  </div>
                </div>
                <div class="out_graph mb-2">
                  <div class="in_graph">
                    <canvas id="test-pie-chart" class="pie-chart"></canvas>
                  </div>
                </div>
                <div class="out_graph mb-2">
                  <div class="in_graph">
                    <canvas id="test-pie-chart2" class="pie-chart"></canvas>
                  </div>
                </div>
                <div class="out_graph mb-2">
                  <div class="in_graph">
                    <canvas id="test-pie-chart3" class="pie-chart"></canvas>
                  </div>
                </div>
              </v-flex>
              <hr/>
              <v-flex lg3 md3 class="wordcloud-container">
                <div class="out_graph mb-2">
                  <div class="in_graph">
                    <div class="graph_title">
                      각 질환별 WordCloud
                    </div>
                  </div>
                </div>
                <div class="wordcloud mb-2">
                    <vue-word-cloud
                :words= sad_data.wordcloud
                :color="([, weight]) => weight > 2000 ? '#404fff' : weight > 1500 ? '#625cef' : weight > 1000 ? '#776ae0' : weight > 500 ? '#8677d0' :  weight > 200 ? '#9185c0' : weight > 100 ? '#9a92b0' : '#808080'"
                font-family="Yeon Sung"
                  />
              </div>
              <div class="wordcloud mb-2">
                <vue-word-cloud
                :words= adhd_data.wordcloud
                :color="([, weight]) => weight > 700 ? '#ff7f50' : weight > 400 ? '#f4875f' : weight > 350 ? '#e78f6e' : weight > 250 ? '#da967c' :  weight > 200 ? '#cb9c8b' : weight > 165 ? '#bba299' : '#808080'"
                font-family="Yeon Sung"
                />
              </div>
              <div class="wordcloud mb-2">
                  <vue-word-cloud
                :words= schizophrenia_data.wordcloud
                :color="([, weight]) => weight > 700 ? '#009900' : weight > 450 ? '#298c1d' : weight > 300 ? '#39802c' : weight > 200 ? '#427336' :  weight > 100 ? '#48663f' : weight > 50 ? '#4b5a46' : '#4b5a46'"
                font-family="Yeon Sung"
                />
              </div>
              </v-flex>
            </v-layout>
          </div>
        </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import Chart from 'chart.js'
import $ from 'jquery'

export default {
  name: 'Graph',
  data () {
    return {
      basic: 0,
      sad: 1,
      adhd: 2,
      schizophrenia: 3,
      carousel_index: 0,
      active: null,
      form: {
        contents: ''
      },
      sad_data: {
          graph:{
            type: 'pie',
              data: {
                labels: ["Depression", "Normal"],
                datasets: [{
                  backgroundColor: [
                    "#3498db",
                    "#95a5a6",
                  ],
                  data: []
                }]
              },
            options:{}
          },
          wordcloud: [],
          word_list: ['우울증', '죽도록', '생각', '고통', '자살', '병원', '정말', '마음', '시간', '정도', '하루', '기분', '혼자', '다른', '하나', '친구', '요즘', '잠', '자신',  '조금', '치료', '엄마', '진짜', '우울', '상태', '가족', '정신', '문제', '머리', '의사', '감정', '어제', '무기', '상담', '눈물', '스트레스', '증상', '느낌', '예전', '매일', '항상', '후회', '슬픈']
        },
        adhd_data: {
            graph:{
            type: 'pie',
              data: {
                labels: ["ADHD", "Normal"],
                datasets: [{
                  backgroundColor: [
                    "coral",
                    "#95a5a6",
                  ],
                  data: []
                }]
              },
            options:{}
          },
          wordcloud: [],
          word_list: ['사람', '생각', '다른', '자신', '문제', '치료', '도움', '병원', '효과', '방법', '집중', '마음', '이상', '보고', '다시', '성인', '행동', '사회', '하나', '계속', '가장', '결과', '정말', '한번', '증상', '생활', '정신', '처음', '내용', '동안', 'ADHD', '경험', '사실', '이야기', '상담', '통해', '상황', '현재', '대해', '상태', '복용', '다음', '하루', '모든']
        },
        schizophrenia_data: {
          graph:{
            type: 'pie',
              data: {
                labels: ["Schizophrenia", "Normal"],
                datasets: [{
                  backgroundColor: [
                    "#009900",
                    "#95a5a6",
                  ],
                  data: []
                }]
              },
            options:{}
          },
          wordcloud: [],
          word_list: ['사람', '약', '조현병', '병원', '생각', '고통', '너무', '시간', '마음', '가족', '치료', '때문', '정도', '다른', '우리', '다시', '입원', '자신', '상담', '정신', '환자', '의사', '생활', '문제', '복용', '이제', '증상', '이상', '보고', '도움', '모든', '계속', '사회', '모두', '한번', '이야기', '정말', '상태', '약물', '위해', '기도', '동안', '조금', '정신과', '방법', '혼자', '조울', '조울증', '슬픔']
        },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      alert("모델이 분석중입니다. 잠시만 기다려주세요.")
      this.$http
        .post('/api/test', {
          contents: this.form.contents
        })
        .then((res) => {
          this.sad_data.graph.data.datasets[0].data = JSON.parse(res.data.sad)
          this.adhd_data.graph.data.datasets[0].data = JSON.parse(res.data.adhd)
          this.schizophrenia_data.graph.data.datasets[0].data = JSON.parse(res.data.schi)
          this.carousel_index = 1
          this.find_list_text(this.sad_data.word_list, "sad")
          this.find_list_text(this.adhd_data.word_list, "adhd")
          this.find_list_text(this.schizophrenia_data.word_list, "schizophrenia")
        })
        .catch((err) => {
          alert(err)
        })
    },
    createChart (chartId, chartData) {
      const ctx = document.getElementById(chartId)
      const chart = this.myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      })
    },
    getData () {
      this.$http.get('/api/wordcloud/data')
        .then(res => {
          this.sad_data.wordcloud = Object.keys(res.data.sad).map((key) => [key, res.data.sad[key]]);
          this.adhd_data.wordcloud = Object.keys(res.data.adhd).map((key) => [key, res.data.adhd[key]]);
          this.schizophrenia_data.wordcloud = Object.keys(res.data.schizophrenia).map((key) => [key, res.data.schizophrenia[key]]);
        })
    },
    find_text (text, className) {
      $(".text_"+className+":contains("+text+")").each(function () {
        $(this).html($(this).html().split(text).join("<span class='"+className+"'>"+text+"</span>"));
      });
    },
    find_list_text (word_list, className){
      word_list.forEach(text => {
        this.find_text(text, className)
      });
    },
    press_button(){
      console.log(this.sad_data)
      console.log(this.adhd_data)
      console.log(this.schizophrenia_data)
      this.find_list_text(this.sad_data.word_list, "sad")
      this.find_list_text(this.adhd_data.word_list, "adhd")
      this.find_list_text(this.schizophrenia_data.word_list, "schizophrenia")
      this.createChart('test-pie-chart', this.sad_data.graph)
      this.createChart('test-pie-chart2', this.adhd_data.graph)
      this.createChart('test-pie-chart3', this.schizophrenia_data.graph)
    }
  },
  created () {
    this.getData()
  }
}
</script>
<style>
  div.out_boardwrite{
    text-align: center;
  }

  div.in_boardwrite{
    display: inline-block;
  }

  #card_boardwrite{
    height: 600px;
  }
  .twitter_info{
    white-space: pre-line;
    font-family: 'Nanum Myeongjo', serif;
  }
  .sad{
    color: blue !important;
  }
  .adhd{
    color: #ff7f50 !important;
  }
  .schizophrenia{
    color: #009900 !important;
  }
  .graph_title{
    background: #455a64;
    padding: 10px 30px;
    margin: 10px;
    box-shadow: 0px 2px 2px 0px rgba(0,0,0,0.3);
    border-radius: 10px;
    font-size: 1.5rem;
    color:white;
  }
  .main-container{
    margin: 60px;
    background: white;
    border-radius: 10px;
    box-shadow: 0px 2px 2px 0px rgba(0,0,0,0.3);
    padding:10px;
  }
  .disease-container{
  }
  .wordcloud-container{
    flex-direction: column;
  }
  .wordcloud{
    display: inline-block;
    height: 28%;
    width: 100%;
  }
  .pie-container{
  }
  .twitter-container{
    margin-top: 70px;
    background: rgba(0,0,0,0.4);
  }
  div.out_graph{
    text-align: center;
  }

  div.in_graph{
    display: inline-block;
  }
  .pie-chart{
    height: 100% !important;
    width: 100% !important;
  }
  div.out_boardwrite{
    text-align: center;
  }

  div.in_boardwrite{
    display: inline-block;
  }
  .wordcloud_layout{
    text-align: center;
    height: 100%;
  }
  .wordcloud_name{
    font-size: 50px;
    color: white;
  }
  .twitter-template{
    background-position: center center;
    background: url(https://images.unsplash.com/photo-1502657877623-f66bf489d236?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80) no-repeat center center fixed; 
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }
  .v-carousel{
    box-shadow: none;
  }
</style>
