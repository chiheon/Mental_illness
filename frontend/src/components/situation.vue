<template>
  <div class="situation">
    <b-button class="popupBtn" @click="close">
      <v-icon v-text="$vuetify.icons.cancel"></v-icon>
    </b-button>
    <b-tabs card>
      <b-tab title="교내 일정" active>
        <v-card height="430px">
          <v-card-title primary-title>
            <b-container class="padding">
              <b-row>
                <b-col>
              <div>1.22(월)~1.24(수) 1학기 예비수강신청<br>
                   2.7(수)~2.13(화) 수강신청<br>
                   2.22(목)~2.28(수) 1학기 등록<br>
                   3.2(금) 1학기 개강<br>
                   3.7(수)~3.8(목) 1학기 수강정정<br>
                   3.22(목)~3.23(금) 수강신청포기<br>
                   4.12(목) 45주년 개교기념일<br>
                   4.20(금)~4.26(목) 1학기 중간시험<br>
                   5.24(목) 1학기 수업일수 3/4선<br>
                   6.18(월)~6.22(금) 1학기 기말시험<br>
                   6.18(월)~6.27(수) 성적공고기간<br>
                   6.25(월) 하계방학시작<br>
                   6.28(목)~6.29(금) 1학기 성적정정<br>
                   7.3(화)~7.23(월) 하계계절수업<br>
                   8.6(월)~8.10(금) 2학기 수강신청<br>
                   8.24(금)~8.30(목) 2학기 등록<br>
              </div>
                </b-col>
                <b-col>
                  <div>9.3(월) 2학기 개강<br>
                       9.6(목)~9.7(금) 2학기 수강정정<br>
                       10.22(월)~10.26(금) 2학기 중간시험<br>
                       11.26(월)~11.30(금) 전과 신청<br>
                       12.17(월) 보강일<br>
                       12.18(화)~12.24(월) 2학기 기말시험<br>
                       12.19(수)~12.28(금) 2학기 성적입력<br>
                  </div>
                </b-col>
              </b-row>
            </b-container>
          </v-card-title>
        </v-card>
      </b-tab>
      <b-tab title="국내 사건">
        <v-card height="430px">
          <v-card-title primary-title>
            <b-container class="padding">
              <b-row>
                <b-col>
                  <div>1.9 남북고위급회담<br>
                    1.16 암호화폐 대폭락<br>
                    2.9 평창 올림픽 개막<br>
                    2.11 포항 규모 4.6 지진<br>
                    3.5 안희정 성폭력 의혹<br>
                    3.6 남북정상회담 개최결정<br>
                    3.9 미투-조민기 자택 지하 자살<br>
                    3.23 이명박 수감<br>
                    4.2 방배초등학교 인질극<br>
                    4.6 박근혜-최순실 선고<br>
                    4.9 이명박 구속<br>
                    4.23 대북 확성기 중단<br>
                    4.27 1차 남북정상회담<br>
                    5.1~5.2 홍대 누드 크로키 도촬<br>
                    5.4 대진침대 라돈 검출<br>
                    5.23 밤토끼 사이트 폐쇄<br>
                    5.26 2차 남북정상회담<br>
                    6.2 페미니즘 단체 상의탈의 시위<br>
                  </div>
                </b-col>
                <b-col>
                  <div>6.12 북미정상회담<br>
                    6.13 지방,재보궐선거<br>
                    6.19 마산함 폭발사고<br>
                    6.28 양심적 병역거부 합헌<br>
                    7.1 아시아나 기내식 대란<br>
                    7.4 관악산 여고생 집단폭행<br>
                    7.23 드루킹 노회찬 의원 자살<br>
                    7.24 숙명여고 문제유출 의혹<br>
                    8.19 서울대공원 토막살인 시체<br>
                    8.23 태풍 솔릭 한반도 강타<br>
                    9.1 한국대표팀 일본 2-1 승리<br>
                    9.11 윤서인 김세의 구형<br>
                    9.19 평양공동선언 합의<br>
                    9.20 미미쿠키 사건<br>
                    9.28 인도네시아 규모 7.5 지진<br>
                    10.14 강서구 피시방 살인<br>
                    10.25 부산 일가족 4명 살인<br>
                    11.15 2019 수능<br>
                  </div>
                </b-col>
              </b-row>
            </b-container>
          </v-card-title>
        </v-card>
      </b-tab>

    </b-tabs>
  </div>
</template>

<script>
export default {
  name: 'Situation',
  methods: {
    close () {
      this.$emit('close')
    }
  }
}
</script>

<style scoped>
  .popupBtn{
    float: right;
    margin-top:5px;
    background-color: transparent;
    border: transparent;
  }
  .padding{
    padding-top: 0px;
  }
</style>
