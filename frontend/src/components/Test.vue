<template>
  <v-carousel height="850"
               hide-delimiters
               hide-controls>
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
      :src="item.src"
      class="carousel"
    >
    <div class="out_boardwrite">
      <div class="in_boardwrite">
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
                                 :rows="15"
                                 :max-rows="25">
                </b-form-textarea>
              </b-form-group>
              <b-button type="submit" variant="secondary">검사</b-button>
            </b-form>
          </div>
        </b-card>
      </div>
    </div>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import ConclusionPopup from './conclusion'
export default {
  data () {
    return {
      items: [{
        src: 'https://images.unsplash.com/photo-1502657877623-f66bf489d236?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
      }],
      form: {
        contents: ''
      },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      this.$http
        .post('/api/test', {
          contents: this.form.contents
        })
        .then((res) => {
          if (res.data.result === '0') {
            console.log(res.data)
            alert('당신은 스트레스가 검출되지 않았습니다.')
          } else {
            console.log(res.data)
            this.Popup(res.data.result_3)
          }
        })
        .catch((err) => {
          alert(err)
        })
    },
    Popup (result) {
      this.$modal.show(ConclusionPopup, {
        modal: this.$modal,
        result: result
      }, {
        name: 'dynamic-modal',
        width: '600px',
        height: '490px',
        draggable: true,
        clickToClose: false
      })
    }
  },
  created () {
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
    margin-top: 160px;
    width: 800px;
  }
</style>
