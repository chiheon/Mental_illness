<template>
  <div id="app">
    <v-toolbar
      absolute
      color="grey darken-4"
      dark
      height="70px"
      scroll-off-screen
      scroll-target="#scrolling-techniques"
    >
      <v-toolbar-title>온라인 커뮤니티 내에서 Mental illness
        측정을 위한 모델 및 시각화 개발</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn to="/" flat>Main</v-btn>
        <v-btn @click="Popup" flat>Profile</v-btn>
        <v-btn to="/analysis" flat>Analysis</v-btn>
        <v-btn to="/twitter" flat>Twitter</v-btn>
        <v-btn to="/test" flat>Test</v-btn>
      </v-toolbar-items>

    </v-toolbar>
    <div>

      <modals-container/>
      <router-view></router-view>

    <v-footer dark
              height="auto">
      <v-card
        class="flex"
        flat
        tile
      >
        <v-card-actions class="rey darken-4 justify-center">
          &copy;2019 — <strong>자기주도연구2 - 김치헌</strong>
        </v-card-actions>
      </v-card>
    </v-footer>
    </div>
  </div>
</template>

<script>
import ProfilePopup from './../Profile'
export default {
  data: () => ({
  }),
  methods: {
    Popup () {
      this.$modal.show(ProfilePopup, {
        modal: this.$modal }, {
        name: 'dynamic-modal',
        width: '600px',
        height: '600px',
        draggable: true
      })
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Do+Hyeon|Noto+Serif+KR&display=swap');
@import url('https://fonts.googleapis.com/css?family=Nanum+Myeongjo|Yeon+Sung&display=swap');
html, body{
  /* font-family: 'Noto Serif KR', serif; */
}
</style>
