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
        <v-card class="message-box__content__message">
          <span>{{ content }}</span>
        </v-card>
      </div>
    </div>
    <div class="message-box__time">
      <span>{{ time }}</span>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";

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
    content: {
      type: Object,
    },
    time: {
      type: String,
    },
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

    .message-box__content__message {
      display: inline-block;
      background-color: rgb(15, 170, 218) !important;
      border-radius: 15px;
      padding: 2px 7px;
      color: white !important;
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
        .message-box__content__name {
          font-size: 10px;
        }
        .message-box__content__message {
          background-color: rgb(255, 255, 255) !important;
          color: black !important;
        }
      }
    }
  }
}
</style>
