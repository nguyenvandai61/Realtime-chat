<template>
  <div class="reaction-emotion-picker">
    <v-card class="reaction-emotion-picker__icons">
      <div
        class="reaction-emotion-picker__icon"
        v-for="(emotion, index) in emotions"
        :key="emotion.id"
        @click="() => emotionClicked(index)"
      >
        <img :src="emotion.icon" :alt="emotion.name" />
        <span v-if="emotion_picked.id == emotion.id" class="dot"></span>
      </div>
    </v-card>
  </div>
</template>
<script>
import Vue from "vue";
export default Vue.extend({
  name: "ReactionEmotionPicker",
  props: {
    emotion_picked: {
      id: Number,
    },
  },
  data() {
    return {
      // emotion_picked: {
      //   id: 1,
      // },
      emotions: [
        {
          id: 1,
          icon: "https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",
        },
        {
          id: 2,
          icon: "https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",
        },
        {
          id: 3,
          icon: "https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",
        },
      ],
    };
  },
  methods: {
    emotionClicked(index) {
      this.emotion_picked = this.emotions[index];
      this.$emit("emotion-picked-off", this.emotion_picked);
    }
  }
});
</script>
<style lang="scss" scoped>
.reaction-emotion-picker {
  .reaction-emotion-picker__icons {
    border-radius: 25px;
    padding: 0px 5px;
    display: flex;
    .reaction-emotion-picker__icon {
      position: relative;
      img {
        width: 30px;
        height: 30px;
        margin: 5px;
      }
      .dot {
        position: absolute;
        bottom: 0px;
        left: 14px;
        height: 10px;
        width: 10px;
        background-color: rgb(15, 170, 218);
        border-radius: 50%;
        display: inline-block;
      }
    }
  }
}
</style>
