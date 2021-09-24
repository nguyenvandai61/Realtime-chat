<template>
  <div id="chat-room">
    <chat-room-header></chat-room-header>
    <div class="chat-room__body">
      <div class="chat-room__body__messages">
        <div
          class="chat-room__body__message"
          v-for="message in messages"
          :key="message.id"
        >
          <message-box
            :class="`chat-room__body__messages__message-box ${
              message.is_guest ? 'guest' : ''
            }`"
            :name="message.name"
            :is_guest="message.is_guest"
            :avatar="user.avatar"
            :content="message.content"
            :reaction_emotions="message.reaction_emotions"
          />
        </div>
      </div>
      <v-row class="chat-room__body__input">
        <div class="chat-room__body__input__text-field">
          <v-text-field
            v-model="messageInput"
            label=""
            autofocus
            placeholder="Type your message"
            @keyup.enter="sendMessage"
          />
        </div>
        <div class="chat-room__body__input__send">
          <v-btn @click="sendMessage">Send</v-btn>
        </div>
      </v-row>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
import { Message } from "@/models/Message";
import { User } from "@/models/User";
import InfoBox from "@/components/InfoBox.vue";
import MessageBox from "@/components/MessageBox.vue";
import ChatRoomHeader from "./components/ChatRoomHeader.vue";

export default Vue.extend({
  name: "app",
  components: {
    MessageBox,
    ChatRoomHeader,
  },
  props: {},
  data: function () {
    return {
      title: "Chat Room",
      user: {
        id: 1,
        name: "Crys",
        avatar: "https://avatars3.githubusercontent.com/u/14785789?v=3&s=460",
      },
      auth_user: {
        id: 2,
        name: "Dai",
        avatar: "https://avatars3.githubusercontent.com/u/14785790?v=3&s=460",
      },
      messages: [
        {
          id: 1,
          content: "Hello",
          is_guest: true,
          name: "Crys",
          user_id: 1,
        },
        {
          id: 2,
          content: "Chào bạn",
          is_guest: false,
          user_id: 2,
        },
        {
          id: 3,
          content: "Goodmorning",
          is_guest: true,
          name: "Crys",
          user_id: 1,
        },
      ],
      messageInput: "",
    };
  },
  methods: {
    sendMessage(): void {
      console.log("send message");
    },
  },
});
</script>

<style lang="scss" scoped>
.chat-room__body {
  background-color: rgb(215, 240, 231);
  display: block;
  position: relative;
  padding: 0px 10px 10px 10px;
  width: 100%;
  height: 100vh;
  .chat-room__body__messages {
    position: absolute;
    left: 0;
    bottom: 100px;
    width: 100%;
    .chat-room__body__message {
      .chat-room__body__messages__message-box {
        margin-bottom: 10px;
        float: right;
        &.guest {
          float: left;
        }
      }
    }
  }
  .chat-room__body__input {
    // margin: 3px;
    padding: 0px 8px;
    position: fixed;
    width: 100%;
    bottom: 0;
    background-color: white;
    .chat-room__body__input__text-field {
      flex-basis: 1;
      flex-grow: 1;
      margin-right: 15px;
    }
    .chat-room__body__input__send {
      display: flex;
      margin-left: 3px;
      justify-content: center;
      align-items: center;
    }
  }
}
</style>
