<template>
  <div class="chat-room__body__messages__message">
    <v-card class="chat-room__body__messages__message__content">
      <div class="chat-room__body__messages__message__content__user">
        <v-avatar size="40">
          <img :src="avatar" alt="" />
        </v-avatar>
      </div>
      <div
        class="chat-room__body__messages__message__content__message white--text"
      >
        <span>{{ message.content }}</span>
      </div>
    </v-card>
    <div class="chat-room__body__messages__message__time">
      <span>{{ message.time }}</span>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "MessageBox",
  props: {
    avatar: {
      type: String,
      required: true,
    },
    message: {
      type: Object,
    },
  },
});
</script>
<style lang="scss" scoped>
.chat-room__body__messages__message__content {
  display: inline-block;
  background-color: rgb(15, 170, 218) !important;
  width: 200px;
  padding: 5px;
  border-radius: 5px;
  margin-bottom: 5px;
  margin-left: 5px;
  .chat-room__body__messages__message__content__user {
    display: inline-block;
    margin-right: 15px;
  }
  .chat-room__body__messages__message__content__message {
    display: inline-block;
  }
}
</style>
