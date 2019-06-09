<template>
  <div class="twitter-template">
    <v-carousel height="100%" :cycle="false" v-model="carousel_index">
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
                v-model="active_1"
                color="blue-grey darken-2"
                class="mt-3"
                centered
              >
            <v-tabs-items v-model="tab">
              <v-tab-item :key="basic_1">
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
              <v-tab-item :key="sad_1">
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
              <v-tab-item :key="adhd_1">
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
              <v-tab-item :key="schizophrenia_1">
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

              <v-tab :key="basic_1">
                기본
              </v-tab>
              <v-tab :key="sad_1">
                우울증
              </v-tab>
              <v-tab :key="adhd_1">
                ADHD
              </v-tab>
              <v-tab :key="schizophrenia_1">
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
              :color="([, weight]) => weight > 700 ? '#009900' : weight > 450 ? '#298c1d' : weight > 300 ? '#39802c' : weight > 200 ? '#427336' :  weight > 100 ? '#48663f' : weight > 50 ? '#4b5a46' : '#4b5a46'"
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
                    <div class="headline">우울증 관련 트위터
                      <v-btn @click="press_button(2)">Fetch</v-btn>
                    </div>
                  </div>
                </v-card-title>
              </v-card>
            
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                    <span class="twitter_info">시다 (@9uenchth1rst)
                  우울증, 불안 장애, 공황 장애를 치료 중인 성인 퀴어 여성.</span>
                  </div>
                </v-card-title>
              </v-card>

              <v-tabs
                v-model="active_3"
                color="blue-grey darken-2"
                class="mt-3"
                centered
              >
            <v-tabs-items v-model="tab_2">
              <v-tab-item :key="basic">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_base">나는 누군가가 원하는 대로
                             뚝딱뚝딱 만들어진
                              인형이 아니라 

                              내 스스로가 바라고 원하는 대로 
                              내 속도에 맞춰 
                              조금씩 형태를 만들어 나가는 
                              나라는 사람이다

                               그 사실을 잊어버리지 않으려고 애쓴다
                                나를 위한
                                 내가 되기 위해서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="sad">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_sad">나는 누군가가 원하는 대로
                             뚝딱뚝딱 만들어진
                              인형이 아니라 

                              내 스스로가 바라고 원하는 대로 
                              내 속도에 맞춰 
                              조금씩 형태를 만들어 나가는 
                              나라는 사람이다

                               그 사실을 잊어버리지 않으려고 애쓴다
                                나를 위한
                                 내가 되기 위해서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="adhd">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_adhd">나는 누군가가 원하는 대로
                             뚝딱뚝딱 만들어진
                              인형이 아니라 

                              내 스스로가 바라고 원하는 대로 
                              내 속도에 맞춰 
                              조금씩 형태를 만들어 나가는 
                              나라는 사람이다

                               그 사실을 잊어버리지 않으려고 애쓴다
                                나를 위한
                                 내가 되기 위해서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="schizophrenia">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_schizophrenia">나는 누군가가 원하는 대로
                             뚝딱뚝딱 만들어진
                              인형이 아니라 

                              내 스스로가 바라고 원하는 대로 
                              내 속도에 맞춰 
                              조금씩 형태를 만들어 나가는 
                              나라는 사람이다

                               그 사실을 잊어버리지 않으려고 애쓴다
                                나를 위한
                                 내가 되기 위해서</span>
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
                  <v-btn flat dark href='https://twitter.com/9uenchth1rst' target="_blank"><i class="material-icons">touch_app</i>방문하기</v-btn>
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
                  <canvas id="sad-pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="sad-pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="sad-pie-chart3" class="pie-chart"></canvas>
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
      <v-carousel-item>
        <div class="twitter-container py-5">
          <v-layout row wrap class="main-container">
            <v-flex lg6 md6 class="disease-container">
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div>
                    <div class="headline">조울증 관련 트위터
                      <v-btn @click="press_button(3)">Fetch</v-btn>
                    </div>
                  </div>
                </v-card-title>
              </v-card>
            
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                    <span class="twitter_info">도현 (@domohyun___)
                    폐쇄병동 입원 했었음///조울증 자해중독🔪</span>
                  </div>
                </v-card-title>
              </v-card>

              <v-tabs
                v-model="active_2"
                color="blue-grey darken-2"
                class="mt-3"
                centered
              >
            <v-tabs-items v-model="tab_3">
              <v-tab-item :key="basic_3">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_base">갑자기 생각났는데ㅋㅋㅋㅋㅋ 병원 입원했을 때
                             기억은 안 나지만 뭐때매 화가 나서 
                             불꺼진 병동에서 손톱으로 다리를 벅벅 그어서
                              자해를 했는데(칼이 없으니까,,,)
                               본명이 HE라서 HE로 자해를 하고 
                               그걸 다음날 간호사 샘들이 알아서
                                의사 샘한테 바로 얘기하니까,,, 
                                그 날 회진 오셔서 하는 말씀이
                                다리에 왜 HE로 새겼냐고 help 새기려고 한 거냐고 해서 아뇨
                                 제 이름인데요(당당) 이러니까 당황하셔서 아...... 
                                 이러셨던 게 생각난다ㅋㅋㅋㅋㅋㅋ 
                                 병원생활도 재밌었는데......(급추억)</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="sad_3">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_sad">갑자기 생각났는데ㅋㅋㅋㅋㅋ 병원 입원했을 때
                             기억은 안 나지만 뭐때매 화가 나서 
                             불꺼진 병동에서 손톱으로 다리를 벅벅 그어서
                              자해를 했는데(칼이 없으니까,,,)
                               본명이 HE라서 HE로 자해를 하고 
                               그걸 다음날 간호사 샘들이 알아서
                                의사 샘한테 바로 얘기하니까,,, 
                                그 날 회진 오셔서 하는 말씀이
                                다리에 왜 HE로 새겼냐고 help 새기려고 한 거냐고 해서 아뇨
                                 제 이름인데요(당당) 이러니까 당황하셔서 아...... 
                                 이러셨던 게 생각난다ㅋㅋㅋㅋㅋㅋ 
                                 병원생활도 재밌었는데......(급추억)</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="adhd_3">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_adhd">갑자기 생각났는데ㅋㅋㅋㅋㅋ 병원 입원했을 때
                             기억은 안 나지만 뭐때매 화가 나서 
                             불꺼진 병동에서 손톱으로 다리를 벅벅 그어서
                              자해를 했는데(칼이 없으니까,,,)
                               본명이 HE라서 HE로 자해를 하고 
                               그걸 다음날 간호사 샘들이 알아서
                                의사 샘한테 바로 얘기하니까,,, 
                                그 날 회진 오셔서 하는 말씀이
                                다리에 왜 HE로 새겼냐고 help 새기려고 한 거냐고 해서 아뇨
                                 제 이름인데요(당당) 이러니까 당황하셔서 아...... 
                                 이러셨던 게 생각난다ㅋㅋㅋㅋㅋㅋ 
                                 병원생활도 재밌었는데......(급추억)</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="schizophrenia_3">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_schizophrenia">갑자기 생각났는데ㅋㅋㅋㅋㅋ 병원 입원했을 때
                             기억은 안 나지만 뭐때매 화가 나서 
                             불꺼진 병동에서 손톱으로 다리를 벅벅 그어서
                              자해를 했는데(칼이 없으니까,,,)
                               본명이 HE라서 HE로 자해를 하고 
                               그걸 다음날 간호사 샘들이 알아서
                                의사 샘한테 바로 얘기하니까,,, 
                                그 날 회진 오셔서 하는 말씀이
                                다리에 왜 HE로 새겼냐고 help 새기려고 한 거냐고 해서 아뇨
                                 제 이름인데요(당당) 이러니까 당황하셔서 아...... 
                                 이러셨던 게 생각난다ㅋㅋㅋㅋㅋㅋ 
                                 병원생활도 재밌었는데......(급추억)</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
            </v-tabs-items>
              <v-tabs-slider color="white"></v-tabs-slider>

              <v-tab :key="basic_3">
                기본
              </v-tab>
              <v-tab :key="sad_3">
                우울증
              </v-tab>
              <v-tab :key="adhd_3">
                ADHD
              </v-tab>
              <v-tab :key="schizophrenia_3">
                정신분열증
              </v-tab>
            </v-tabs>

              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-actions>
                  <v-btn flat dark href='https://twitter.com/domohyun___' target="_blank"><i class="material-icons">touch_app</i>방문하기</v-btn>
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
                  <canvas id="schi-pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="schi-pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="schi-pie-chart3" class="pie-chart"></canvas>
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
      <v-carousel-item>
        <div class="twitter-container py-5">
          <v-layout row wrap class="main-container">
            <v-flex lg6 md6 class="disease-container">
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div>
                    <div class="headline">조울증 관련 트위터
                      <v-btn @click="press_button(4)">Fetch</v-btn>
                    </div>
                  </div>
                </v-card-title>
              </v-card>
            
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                    <span class="twitter_info">함께해요 (@NowhereICanStay)
                    20대女/조울증/자해러 언젠가 우리에게도 봄 날이 오길</span>
                  </div>
                </v-card-title>
              </v-card>

              <v-tabs
                v-model="active_4"
                color="blue-grey darken-2"
                class="mt-3"
                centered
              >
            <v-tabs-items v-model="tab_4">
              <v-tab-item :key="basic_4">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_base">사람이 왜 떠나냐고요?
                          생각하건대, 자신이 생각했던 것과
                          다르니까 떠나는 게 아닐까요.

                          생각만큼
                          날 사랑해주지 않아서,

                          생각만큼 
                          내가 너에게 소중한 사람이 아니어서.

                          너와 나의 사랑이 생각처럼 되지 않아서.
                          그리고 그게 생각보다 아파서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="sad_4">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_sad">사람이 왜 떠나냐고요?
                          생각하건대, 자신이 생각했던 것과
                          다르니까 떠나는 게 아닐까요.

                          생각만큼
                          날 사랑해주지 않아서,

                          생각만큼 
                          내가 너에게 소중한 사람이 아니어서.

                          너와 나의 사랑이 생각처럼 되지 않아서.
                          그리고 그게 생각보다 아파서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="adhd_4">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_adhd">사람이 왜 떠나냐고요?
                          생각하건대, 자신이 생각했던 것과
                          다르니까 떠나는 게 아닐까요.

                          생각만큼
                          날 사랑해주지 않아서,

                          생각만큼 
                          내가 너에게 소중한 사람이 아니어서.

                          너와 나의 사랑이 생각처럼 되지 않아서.
                          그리고 그게 생각보다 아파서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="schizophrenia_4">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_schizophrenia">사람이 왜 떠나냐고요?
                          생각하건대, 자신이 생각했던 것과
                          다르니까 떠나는 게 아닐까요.

                          생각만큼
                          날 사랑해주지 않아서,

                          생각만큼 
                          내가 너에게 소중한 사람이 아니어서.

                          너와 나의 사랑이 생각처럼 되지 않아서.
                          그리고 그게 생각보다 아파서</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
            </v-tabs-items>
              <v-tabs-slider color="white"></v-tabs-slider>

              <v-tab :key="basic_4">
                기본
              </v-tab>
              <v-tab :key="sad_4">
                우울증
              </v-tab>
              <v-tab :key="adhd_4">
                ADHD
              </v-tab>
              <v-tab :key="schizophrenia_4">
                정신분열증
              </v-tab>
            </v-tabs>

              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-actions>
                  <v-btn flat dark href='https://twitter.com/NowhereICanStay' target="_blank"><i class="material-icons">touch_app</i>방문하기</v-btn>
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
                  <canvas id="schi2-pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="schi2-pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="schi2-pie-chart3" class="pie-chart"></canvas>
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
      <v-carousel-item>
        <div class="twitter-container py-5">
          <v-layout row wrap class="main-container">
            <v-flex lg6 md6 class="disease-container">
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div>
                    <div class="headline">ADHD 관련 트위터
                      <v-btn @click="press_button(5)">Fetch</v-btn>
                    </div>
                  </div>
                </v-card-title>
              </v-card>
            
              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-title primary-title>
                  <div>
                    <span class="twitter_info">병원일기 (@eniargim2)
                    군발성 두통, adhd이야기를 합니다</span>
                  </div>
                </v-card-title>
              </v-card>

              <v-tabs
                v-model="active_5"
                color="blue-grey darken-2"
                class="mt-3"
                centered
              >
            <v-tabs-items v-model="tab_5">
              <v-tab-item :key="basic_5">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_base">정말로 나는 안 하려고 그러는 게 아니라
                             왜 메일 알람이 어떨 때는 눈에 보이고 어떨 때는 눈에 안 보이는지 이해가 안 가고,
                             왜 똑같이 기상 알람설정을 한 기분이어도 어떨 때는 알람이 울리고
                             어떨 때는 울리지 않는지 이해가 안 간다.
                             왜 모든 문자를 체크한 것 같아도 놓치는 게 있는지
                             엑셀파일을 한 칸 한 칸 체크한 것 같아도 안 쓴 게 있는지.. 
                             왜 계산에 검산에 검산의 검산의 검산까지 해도 보란듯이 틀리는 게 있는지.
                             당연히 게을러서 검산을 안 하고 캘린더를 안 쓰고 파일을 한 번 덜 확인하고, 
                             매일을 제때 안 보는 사람으로 보이겠지만 정말 나는 내가 할 수 있는 건 다 해봤다. 
                             그런데도 왜 안 되는지 나도 이해가 안 가니 이해를 바라기도 힘들지만.. 
                             일상들을 조립하기가 너무 힘들다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="sad_5">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_sad">정말로 나는 안 하려고 그러는 게 아니라
                             왜 메일 알람이 어떨 때는 눈에 보이고 어떨 때는 눈에 안 보이는지 이해가 안 가고,
                             왜 똑같이 기상 알람설정을 한 기분이어도 어떨 때는 알람이 울리고
                             어떨 때는 울리지 않는지 이해가 안 간다.
                             왜 모든 문자를 체크한 것 같아도 놓치는 게 있는지
                             엑셀파일을 한 칸 한 칸 체크한 것 같아도 안 쓴 게 있는지.. 
                             왜 계산에 검산에 검산의 검산의 검산까지 해도 보란듯이 틀리는 게 있는지.
                             당연히 게을러서 검산을 안 하고 캘린더를 안 쓰고 파일을 한 번 덜 확인하고, 
                             매일을 제때 안 보는 사람으로 보이겠지만 정말 나는 내가 할 수 있는 건 다 해봤다. 
                             그런데도 왜 안 되는지 나도 이해가 안 가니 이해를 바라기도 힘들지만.. 
                             일상들을 조립하기가 너무 힘들다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="adhd_5">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_adhd">정말로 나는 안 하려고 그러는 게 아니라
                             왜 메일 알람이 어떨 때는 눈에 보이고 어떨 때는 눈에 안 보이는지 이해가 안 가고,
                             왜 똑같이 기상 알람설정을 한 기분이어도 어떨 때는 알람이 울리고
                             어떨 때는 울리지 않는지 이해가 안 간다.
                             왜 모든 문자를 체크한 것 같아도 놓치는 게 있는지
                             엑셀파일을 한 칸 한 칸 체크한 것 같아도 안 쓴 게 있는지.. 
                             왜 계산에 검산에 검산의 검산의 검산까지 해도 보란듯이 틀리는 게 있는지.
                             당연히 게을러서 검산을 안 하고 캘린더를 안 쓰고 파일을 한 번 덜 확인하고, 
                             매일을 제때 안 보는 사람으로 보이겠지만 정말 나는 내가 할 수 있는 건 다 해봤다. 
                             그런데도 왜 안 되는지 나도 이해가 안 가니 이해를 바라기도 힘들지만.. 
                             일상들을 조립하기가 너무 힘들다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
              <v-tab-item :key="schizophrenia_5">
                 <v-card color="blue-grey darken-2" class="white--text">
                    <v-card-title primary-title>
                      <div>
                          <span class="twitter_text twitter_info text_schizophrenia">정말로 나는 안 하려고 그러는 게 아니라
                             왜 메일 알람이 어떨 때는 눈에 보이고 어떨 때는 눈에 안 보이는지 이해가 안 가고,
                             왜 똑같이 기상 알람설정을 한 기분이어도 어떨 때는 알람이 울리고
                             어떨 때는 울리지 않는지 이해가 안 간다.
                             왜 모든 문자를 체크한 것 같아도 놓치는 게 있는지
                             엑셀파일을 한 칸 한 칸 체크한 것 같아도 안 쓴 게 있는지.. 
                             왜 계산에 검산에 검산의 검산의 검산까지 해도 보란듯이 틀리는 게 있는지.
                             당연히 게을러서 검산을 안 하고 캘린더를 안 쓰고 파일을 한 번 덜 확인하고, 
                             매일을 제때 안 보는 사람으로 보이겠지만 정말 나는 내가 할 수 있는 건 다 해봤다. 
                             그런데도 왜 안 되는지 나도 이해가 안 가니 이해를 바라기도 힘들지만.. 
                             일상들을 조립하기가 너무 힘들다</span>
                      </div>
                    </v-card-title>
                  </v-card>
              </v-tab-item>
            </v-tabs-items>
              <v-tabs-slider color="white"></v-tabs-slider>

              <v-tab :key="basic_5">
                기본
              </v-tab>
              <v-tab :key="sad_5">
                우울증
              </v-tab>
              <v-tab :key="adhd_5">
                ADHD
              </v-tab>
              <v-tab :key="schizophrenia_5">
                정신분열증
              </v-tab>
            </v-tabs>

              <v-card color="blue-grey darken-2" class="white--text mt-3">
                <v-card-actions>
                  <v-btn flat dark href='https://twitter.com/eniargim2' target="_blank"><i class="material-icons">touch_app</i>방문하기</v-btn>
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
                  <canvas id="adhd-pie-chart" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="adhd-pie-chart2" class="pie-chart"></canvas>
                </div>
              </div>
              <div class="out_graph mb-2">
                <div class="in_graph">
                  <canvas id="adhd-pie-chart3" class="pie-chart"></canvas>
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
      carousel_index: 0,
      active_1: null,
      active_2: null,
      active_3: null,
      active_4: null,
      active_5: null,
      sad:{
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
          }
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
                  data: [0.74521778, 0.25478222]
                }]
              },
            options:{}
          }
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
                  data: [0.43503945, 0.56496055]
                }]
              },
            options:{}
          }
        }
      },
      sad_2:{
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
                  data: [0.11155832, 0.88844168]
                }]
              },
            options:{}
          }
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
                  data: [0.16835789, 0.83164211]
                }]
              },
            options:{}
          }
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
                  data: [0.07832803, 0.92167197]
                }]
              },
            options:{}
          }
        }
      },
      schizophrenia:{
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
                  data: [0.92299293, 0.07700707]
                }]
              },
            options:{}
          }
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
                  data: [0.48169297, 0.51830703]
                }]
              },
            options:{}
          }
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
                  data: [0.58593908, 0.41406092]
                }]
              },
            options:{}
          }
        }
      },
      schizophrenia_2:{
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
                  data: [0.95304345, 0.04695655]
                }]
              },
            options:{}
          }
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
                  data: [0.52558249, 0.47441751]
                }]
              },
            options:{}
          }
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
                  data: [0.31934276, 0.68065724]
                }]
              },
            options:{}
          }
        }
      },
      adhd:{
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
                  data: [0.98762592, 0.01237408]
                }]
              },
            options:{}
          }
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
                  data: [0.94087367, 0.05912633]
                }]
              },
            options:{}
          }
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
                  data: [0.64410488, 0.35589512]
                }]
              },
            options:{}
          }
        }
      },
      sad_data: {
        wordcloud: [],
        word_list: ['우울증', '죽도록', '생각', '고통', '자살', '병원', '정말', '마음', '시간', '정도', '하루', '기분', '혼자', '다른', '하나', '친구', '요즘', '잠', '자신',  '조금', '치료', '엄마', '진짜', '우울', '상태', '가족', '정신', '문제', '머리', '의사', '감정', '어제', '무기', '상담', '눈물', '스트레스', '증상', '느낌', '예전', '매일', '항상', '후회', '슬픈']
      },
      adhd_data: {
        wordcloud: [],
        word_list: ['사람', '생각', '다른', '자신', '문제', '치료', '도움', '병원', '효과', '방법', '집중', '마음', '이상', '보고', '다시', '성인', '행동', '사회', '하나', '계속', '가장', '결과', '정말', '한번', '증상', '생활', '정신', '처음', '내용', '동안', 'ADHD', '경험', '사실', '이야기', '상담', '통해', '상황', '현재', '대해', '상태', '복용', '다음', '하루', '모든']
      },
      schizophrenia_data: {
        wordcloud: [],
        word_list: ['사람', '약', '조현병', '병원', '생각', '고통', '너무', '시간', '마음', '가족', '치료', '때문', '정도', '다른', '우리', '다시', '입원', '자신', '상담', '정신', '환자', '의사', '생활', '문제', '복용', '이제', '증상', '이상', '보고', '도움', '모든', '계속', '사회', '모두', '한번', '이야기', '정말', '상태', '약물', '위해', '기도', '동안', '조금', '정신과', '방법', '혼자', '조울', '조울증', '슬픔']
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
    },
    press_button(num){
      if(num == 2){
        this.createChart('sad-pie-chart', this.sad_2.sad_data.graph)
        this.createChart('sad-pie-chart2', this.sad_2.adhd_data.graph)
        this.createChart('sad-pie-chart3', this.sad_2.schizophrenia_data.graph)
      } else if(num == 3){
        this.createChart('schi-pie-chart', this.schizophrenia.sad_data.graph)
        this.createChart('schi-pie-chart2', this.schizophrenia.adhd_data.graph)
        this.createChart('schi-pie-chart3', this.schizophrenia.schizophrenia_data.graph)
      } else if (num == 4){
        this.createChart('schi2-pie-chart', this.schizophrenia_2.sad_data.graph)
        this.createChart('schi2-pie-chart2', this.schizophrenia_2.adhd_data.graph)
        this.createChart('schi2-pie-chart3', this.schizophrenia_2.schizophrenia_data.graph)
      } else if (num == 5){
        this.createChart('adhd-pie-chart', this.adhd.sad_data.graph)
        this.createChart('adhd-pie-chart2', this.adhd.adhd_data.graph)
        this.createChart('adhd-pie-chart3', this.adhd.schizophrenia_data.graph)
      }
    }
  },
  created () {
    this.getData()  
  },
  mounted() {
    this.createChart('pie-chart', this.sad.sad_data.graph)
    this.createChart('pie-chart2', this.sad.adhd_data.graph)
    this.createChart('pie-chart3', this.sad.schizophrenia_data.graph)
    this.find_list_text(this.sad_data.word_list, "sad")
    this.find_list_text(this.adhd_data.word_list, "adhd")
    this.find_list_text(this.schizophrenia_data.word_list, "schizophrenia")
    $('.v-carousel__controls').addClass('mb-5')
  }
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
</style>
