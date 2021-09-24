<template>
  <div class="room-avatar">
    <div
      class="room-avatar__one-user"
      v-if="user_avatars && user_avatars.length == 1"
    >
      <v-avatar class="first-avatar">
        <img :src="user_avatars[0].avatar" alt="avatar_0" />
      </v-avatar>
    </div>
    <div class="room-avatar__two-user" v-else>
      <v-avatar class="first-avatar">
        <img :src="user_avatars[0].avatar" alt="avatar_0" />
      </v-avatar>
      <v-avatar class="second-avatar">
        <img :src="user_avatars[1].avatar" alt="avatar_1" />
      </v-avatar>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "RoomAvatar",
  props: {
    user_avatars: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {};
  },
});
</script>
<style lang="scss" scoped>
.room-avatar {
  display: inline-flex;
  .room-avatar__one-user {
  }
  .room-avatar__two-user {
    margin-top: auto;
    position: relative;
    .second-avatar {
      justify-content: center;
      align-items: center;
      position: absolute;
      top: -15px;
      right: -15px;
      padding: 5px;
    }
  }
}
</style>
