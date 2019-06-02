<template>
  <div class="twitter-template">
    <v-carousel hide-delimiters height="100%" :cycle="false">
      <v-carousel-item>
        <div class="twitter-container py-5">
          <v-layout row wrap class="main-container">
            <v-flex lg6 md6 class="disease-container">
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div>
                    <div class="headline">우울증 관련 트위터</div>
                  </div>
                </v-card-title>
              </v-card>
            
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                    <span class="twitter_info">soo (@deambuler_blue)
                      은둔형 외톨이, 히키코모리입니다.
                      10년 넘게 우울증, 사회불안장애를 앓고 있습니다.
                      약물치료 중입니다. 살기 위해 치열하게 싸우고 있습니다.
                      제 글은 개인소장 외에 공유를 금지합니다.</span>
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
                          <span class="twitter_text twitter_info text_base">깊이 생각할수록 답이 없다는 걸 알았다 
                          인생을 살아가는 것이다 
                          비교적 삶이 짧거나 
                          너무 짧거나 너무 길어도 
                          내가 확신하는 것 하나는 쉽지 않다는 것이다

                          나는 살아가고 싶고 
                          갑자기 늙지 않는 느낌이다

                          나 자신을 지키는 것 외에 과거의 일은 상관없다 
                          내 삶
                          그리고 간절히 기도한다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="sad">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_sad">깊이 생각할수록 답이 없다는 걸 알았다 
                          인생을 살아가는 것이다 
                          비교적 삶이 짧거나 
                          너무 짧거나 너무 길어도 
                          내가 확신하는 것 하나는 쉽지 않다는 것이다

                          나는 살아가고 싶고 
                          갑자기 늙지 않는 느낌이다

                          나 자신을 지키는 것 외에 과거의 일은 상관없다 
                          내 삶
                          그리고 간절히 기도한다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="adhd">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_adhd">깊이 생각할수록 답이 없다는 걸 알았다 
                          인생을 살아가는 것이다 
                          비교적 삶이 짧거나 
                          너무 짧거나 너무 길어도 
                          내가 확신하는 것 하나는 쉽지 않다는 것이다

                          나는 살아가고 싶고 
                          갑자기 늙지 않는 느낌이다

                          나 자신을 지키는 것 외에 과거의 일은 상관없다 
                          내 삶
                          그리고 간절히 기도한다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="schizophrenia">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_schizophrenia">깊이 생각할수록 답이 없다는 걸 알았다 
                          인생을 살아가는 것이다 
                          비교적 삶이 짧거나 
                          너무 짧거나 너무 길어도 
                          내가 확신하는 것 하나는 쉽지 않다는 것이다

                          나는 살아가고 싶고 
                          갑자기 늙지 않는 느낌이다

                          나 자신을 지키는 것 외에 과거의 일은 상관없다 
                          내 삶
                          그리고 간절히 기도한다</span>
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
                  <v-btn flat dark href='https://twitter.com/deambuler_blue' target="_blank"><i class="material-icons">touch_app</i>방문하기</v-btn>
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
                  <canvas id="pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="pie-chart3" class="pie-chart"></canvas>
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
              :color="([, weight]) => weight > 700 ? '#fff000' : weight > 450 ? '#ebdc38' : weight > 300 ? '#d7c94e' : weight > 200 ? '#c3b65e' :  weight > 100 ? '#aea36b' : weight > 50 ? '#989176' : '#808080'"
              font-family="Yeon Sung"
              />
            </div>
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
                    <div class="headline">Unlimited music now</div>
                    <span>Listen to your favorite artists and albums whenever and wherever, online and offline.</span>
                  </div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Listen now</v-btn>
                </v-card-actions>
              </v-card>
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                      <span>깊이 생각할수록 답이 없다는 걸 알았다 
                      인생을 살아가는 것이다 
                      비교적 삶이 짧거나 
                      너무 짧거나 너무 길어도 
                      내가 확신하는 것 하나는 쉽지 않다는 것이다

                      나는 살아가고 싶고 
                      갑자기 늙지 않는 느낌이다

                      나 자신을 지키는 것 외에 과거의 일은 상관없다 
                      내 삶
                      그리고 간절히 기도한다</span>
                  </div>
                </v-card-title>
              </v-card>
            </v-flex>
            <hr/>
            <v-flex lg3 md3 class="pie-container">
              <div class="out_graph mt-2">
                <div class="in_graph">
                  <canvas id="pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="pie-chart3" class="pie-chart"></canvas>
                </div>
              </div>
            </v-flex>
            <hr/>
            <v-flex lg3 md3 class="wordcloud-container">
              <div class="wordcloud mb-2">
                  <vue-word-cloud
              :words= sad_data.wordcloud
              :color="([, weight]) => weight > 10000 ? '#404fff' : weight > 5000 ? '#625cef' : weight > 3000 ? '#776ae0' : weight > 1500 ? '#8677d0' :  weight > 1000 ? '#9185c0' : weight > 500 ? '9a92b0' : 'a0a0a0'"
              font-family="Roboto"
                />
            </div>
            <div class="wordcloud mb-2">
              <vue-word-cloud
              :words= adhd_data.wordcloud
              :color="([, weight]) => weight > 10000 ? '#ffd077' : weight > 5000 ? '#3bc4c7' : weight > 3000 ? '#3a9eea' : weight > 1500 ? '#ff4e69' :  weight > 1000 ? '#461e47' : weight > 500 ? 'primary' : 'secondary'"
              font-family="Roboto"
              />
            </div>
            <div class="wordcloud mb-2">
                <vue-word-cloud
              :words= adhd_data.wordcloud
              :color="([, weight]) => weight > 10000 ? '#ffd077' : weight > 5000 ? '#3bc4c7' : weight > 3000 ? '#3a9eea' : weight > 1500 ? '#ff4e69' :  weight > 1000 ? '#461e47' : weight > 500 ? 'primary' : 'secondary'"
              font-family="Roboto"
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
      active: null,
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
                data: [0.94846972, 0.05153028]
              }]
            },
          options:{}
        },
        wordcloud: [],
        word_list: ['너무', '우울증', '사람', '생각', '지금', '그냥', '병원', '오늘', '정말', '마음', '시간', '정도', '다시', '때문', '하루', '기분', '계속', '이제', '혼자', '다른', '하나', '친구', '요즘', '잠', '아침', '자신', '한번', '보고', '조금', '치료', '엄마', '진짜', '우울', '상태', '가족', '정신', '문제', '머리', '자꾸', '모든', '처음', '아직', '의사', '감정', '어제', '무기', '상담', '눈물', '스트레스', '증상', '느낌', '예전', '매일', '항상']
      },
      adhd_data: {
        type: 'pie',
          graph:{
          type: 'pie',
            data: {
              labels: ["ADHD", "Normal"],
              datasets: [{
                backgroundColor: [
                  "coral",
                  "#95a5a6",
                ],
                data: [0.74521778, 0.25478222]
              }]
            },
          options:{}
        },
        wordcloud: [],
        word_list: ['사람', '시간', '생각', '다른', '때문', '정도', '경우', '가지', '자신', '문제', '치료', '내', '지금', '너무', '도움', '우리', '병원', '효과', '방법', '집중', '마음', '이상', '대한', '보고', '다시', '성인', '행동', '사회', '위해', '자기', '하나', '계속', '가장', '결과', '정말', '한번', '증상', '생활', '정신', '처음', '내용', '동안', '일이', '경험', '사실', '이야기', '상담', '통해', '상황', '현재', '대해', '상태', '복용', '다음', '하루', '모든']
      },
      schizophrenia_data: {
        graph:{
          type: 'pie',
            data: {
              labels: ["Schizophrenia", "Normal"],
              datasets: [{
                backgroundColor: [
                  "#fff000",
                  "#95a5a6",
                ],
                data: [0.43503945, 0.56496055]
              }]
            },
          options:{}
        },
        wordcloud: [],
        word_list: ['사람', '약', '조현병', '병원', '생각', '지금', '너무', '시간', '마음', '가족', '치료', '때문', '정도', '다른', '우리', '다시', '입원', '자신', '상담', '정신', '환자', '의사', '생활', '문제', '오늘', '대한', '복용', '이제', '증상', '이상', '보고', '하루', '하나', '현재', '처음', '가지', '도움', '모든', '계속', '사회', '모두', '한번', '이야기', '정말', '상태', '약물', '위해', '기도', '동안', '조금', '자기', '아직', '사실', '정신과', '방법', '혼자', '아이']
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
    }
  },
  created () {
    this.getData()
  },
  mounted() {
    this.createChart('pie-chart', this.sad_data.graph)
    this.createChart('pie-chart2', this.adhd_data.graph)
    this.createChart('pie-chart3', this.schizophrenia_data.graph)
    this.find_list_text(this.sad_data.word_list, "sad")
    this.find_list_text(this.adhd_data.word_list, "adhd")
    this.find_list_text(this.schizophrenia_data.word_list, "schizophrenia")
  },
}
</script>
<style>
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
    color: #fff000 !important;
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

  #card_boardwrite{
    margin-top: 160px;
    width: 800px;
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
</style>
