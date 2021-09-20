<template>
  <div id="app">
    <v-app-bar class="chat-room__header" app color="primary" dark>
      <info-box :avatar="user.avatar" :name="user.name"></info-box>
    </v-app-bar>
    <div class="chat-room">
      <div class="chat-room__body">
        <div class="chat-room__body__messages">
          <message-box :avatar="user.avatar" :message="message" />
        </div>
        <v-row class="chat-room__body__input">
          <v-col cols="9">
            <v-text-field
              v-model="messageInput"
              label=""
              placeholder="Type your message"
              @keyup.enter="sendMessage"
            />
          </v-col>
          <v-col>
            <div class="chat-room__body__input__send">
              <v-btn @click="sendMessage">Send</v-btn>
            </div>
          </v-col>
        </v-row>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
import { Message } from "@/models/Message";
import { User } from "@/models/User";
import InfoBox from "@/components/InfoBox.vue";
import MessageBox from "@/components/MessageBox.vue";

export default Vue.extend({
  name: "app",
  components: {
    InfoBox,
    MessageBox,
  },
  props: {},
  data: function() {
    return {
      title: "Chat Room",
      user: {
        id: 1,
        name: "Crys",
        avatar: "https://avatars3.githubusercontent.com/u/14785789?v=3&s=460",
      },
      message: {
        id: 1,
        content: "Chào bạn",
        timestamp: new Date().toISOString(),
      },
      messageInput: "",
    };
  },
  methods: {
    sendMessage(): void {
      console.log("send message");
    },
  }
});
</script>

<style lang="scss" scoped>

</style>
