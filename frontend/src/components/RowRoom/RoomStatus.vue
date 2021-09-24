<template>
  <div class="room-status">
    <div class="room-status__icon" v-if="!is_notified">
      <v-icon> mdi-bell-off </v-icon>
    </div>
    <div class="room-status__icon" v-else-if="status === 'unseen'">
      <v-icon> mdi-checkbox-marked-circle </v-icon>
    </div>
    <div class="room-status__icon" v-else-if="status === 'seen'">
      <v-avatar size="20px">
        <img :src="seen_user_avatar" alt="" />
      </v-avatar>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "RoomStatus",
  props: {
    status: {
      type: String,
    },
    seen_user_avatar: {
      type: String,
    },
    is_notified: {
      type: Boolean,
    },
  },
});
</script>
