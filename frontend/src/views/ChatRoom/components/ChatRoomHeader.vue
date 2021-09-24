<template>
  <v-app-bar class="chat-room__header" app color="primary" dark>
    <v-btn icon>
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>
    <info-box :avatar="user.avatar" :name="user.name"></info-box>
    <v-spacer></v-spacer>
    <v-btn icon>
      <v-icon>call</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>camera</v-icon>
    </v-btn>
  </v-app-bar>
</template>
<script lang="ts">
import Vue from "vue";
import InfoBox from "@/components/InfoBox.vue";
export default Vue.extend({
  name: "ChatRoomHeader",
  components: {
    InfoBox,
  },
  data() {
    return {
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
    };
  },
});
</script>
<style lang="scss" scoped>
.chat-room__header {
  .v-btn {
    margin-left: 5px;
  }
}
</style>
