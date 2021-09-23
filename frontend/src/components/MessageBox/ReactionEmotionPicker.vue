<template>
  <div class="reaction-emotion-picker">
    <v-card class="reaction-emotion-picker__icons">
      <div
        class="reaction-emotion-picker__icon"
        v-for="emotion in emotions"
        :key="emotion.id"
        @click="emotionClicked(emotion)"
      >
        <img :src="emotion.icon" :alt="emotion.name" />
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
      icon: String,
    },
  },
  data() {
    return {
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
});
</script>
<style lang="scss" scoped>
.reaction-emotion-picker {
  .reaction-emotion-picker__icons {
    border-radius: 25px;
    padding: 0px 5px;
    display: flex;
    .reaction-emotion-picker__icon {
      img {
        width: 30px;
        height: 30px;
        margin: 5px;
      }
    }
  }
}
</style>
