<template>
  <div class="message-box">
    <div :class="`message-box__content ${is_guest ? 'guest' : ''}`">
      <div v-if="is_guest" class="message-box__content__user">
        <v-avatar size="40">
          <img :src="avatar" alt="" />
        </v-avatar>
      </div>
      <div class="message-box__content__right">
        <div v-if="is_guest" class="message-box__content__name">
          <span>{{ name }}</span>
        </div>
        <v-card
          class="message-box__content__message"
          v-longpress="handleLongPress"
          v-longpress-stop="handleLongPressStop"
        >
          <span>{{ content }}</span>
          <reaction-emotion :emotions="reaction_emotions"></reaction-emotion>
        </v-card>
        <reaction-emotion-picker
          v-show="is_show_emotion_picker"
          :emotion_picked="{}"
        ></reaction-emotion-picker>
      </div>
    </div>
    <div class="message-box__time">
      <span>{{ time }}</span>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
import ReactionEmotion from "./MessageBox/ReactionEmotion.vue";
import ReactionEmotionPicker from "./MessageBox/ReactionEmotionPicker.vue";
import "@/directives/longpress";

export default Vue.extend({
  name: "MessageBox",
  props: {
    is_guest: {
      type: Boolean,
    },
    name: {
      type: String,
    },
    avatar: {
      type: String,
    },
    content: {},
    time: {
      type: String,
    },
    reaction_emotions: {
      type: Object,
    },
  },
  components: {
    ReactionEmotion,
    ReactionEmotionPicker,
  },
  data() {
    return {
      is_show_emotion_picker: false,
    };
  },
  methods: {
    handleLongPress(): void {
      this.is_show_emotion_picker = true;
    },
    handleLongPressStop(): void {
      this.is_show_emotion_picker = false;
    }
  },
});
</script>
<style lang="scss" scoped>
.message-box {
  width: 100%;
  .message-box__content {
    padding: 5px;
    border-radius: 5px;
    margin-bottom: 5px;
    margin-left: 5px;
    float: right;
    position: relative;

    .message-box__content__message {
      display: inline-block;
      background-color: rgb(15, 170, 218) !important;
      border-radius: 15px;
      padding: 2px 7px;
      color: white !important;
    }
    .reaction-emotion-picker {
      position: absolute;
      top: -35px;
      right: 10px;
    }

    &.guest {
      @extend .message-box__content__user;
      @extend .message-box__content__message;
      float: left;
      .message-box__content__user {
        display: inline-block;
        margin-right: 10px;
        vertical-align: text-bottom;
      }
      .message-box__content__right {
        display: inline-block;
        position: relative;
        .message-box__content__name {
          font-size: 10px;
        }
        .message-box__content__message {
          background-color: rgb(255, 255, 255) !important;
          color: black !important;
          .reaction-emotion {
          }
        }
        .reaction-emotion-picker {
          position: absolute;
          top: -35px;
          left: 0px;
          right: auto;
        }
      }
    }
  }
}
</style>
