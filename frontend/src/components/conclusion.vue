<template>
    <div class="conclusion">
      <v-card dark
              height="490px">
        <v-img
          src="https://images.unsplash.com/photo-1512389098783-66b81f86e199?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=788&q=80"
          aspect-ratio="2.75"
        ></v-img>

        <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">스트레스 검출</h3>
            <div><br>모델이 스트레스가 있는 사람의 게시글이라고 판단하였습니다.<br>아래 분석은 어디까지나 모델에 의해 가장 근사한 정신질환을 나타낸것입니다.<br>어디까지나 참고만 해주세요!<br></div>
            <div v-if="result == 0"><br><br>추가적인 정신질환 판별 모델에 의해 <strong>'정서장애','ADHD','조현병','강박장애','인격장애'</strong> 그룹으로 판별되었습니다.</div>
            <div v-if="result == 1"><br><br>추가적인 정신질환 판별 모델에 의해 <strong>'외상후 스트레스장애','조울증(조증)','불안장애','공황장애'</strong> 그룹으로 판별되었습니다.</div>
            <div v-if="result == 2"><br><br>추가적인 정신질환 판별 모델에 의해 <strong>'우울증'</strong> 으로 판별되었습니다.</div>
          </div>
        </v-card-title>

        <v-card-actions>
          <v-btn @click.prevent="close" flat color="red">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </div>
</template>

<script>
export default {
  props: [
    'result'
  ],
  name: 'Conclusion',
  methods: {
    close () {
      this.$emit('close')
    }
  }
}
</script>

<style scoped>

</style>
