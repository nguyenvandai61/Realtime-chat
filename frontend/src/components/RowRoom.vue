<template>
  <v-card class="row-room">
    <div class="col row-room__room-avatar">
      <room-avatar :user_avatars="room.user_avatars" />
    </div>
    <div class="col row-room__room-info">
      <div class="col row-room__room-title">
        <h3>{{ room.title }}</h3>
      </div>
      <div class="col row-room__last-message">
        <div class="col row-room__last-message__content">
          <p>{{ getLastMessage }}</p>
        </div>
        <div class="col row-room__last-message__time">
          <p>{{ room.last_message.created_at }}</p>
        </div>
      </div>
    </div>
    <div class="col row-room__room-status">
      <room-status
        :status="room.last_message.status"
        :seen_user_avatar="room.user_avatars[0].avatar"
        :is_notified="room.is_notified"
      />
    </div>
  </v-card>
</template>
<script>
import Vue from "vue";
import RoomAvatar from "./RowRoom/RoomAvatar.vue";
import RoomStatus from "./RowRoom/RoomStatus.vue";
export default Vue.extend({
  name: "RowRoom",
  components: {
    RoomAvatar,
    RoomStatus,
  },
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
  computed: {
    getLastMessage() {
      return (
        this.room.last_message.sender.first_name +
        ": " +
        this.room.last_message.message
      );
    },
  },
});
</script>
<style lang="scss" scoped>
.row-room {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  padding: 0.5rem;
  .col {
    flex: 1 1 auto;
    display: flex;
  }
  .row-room__room-info {
    flex: 1 1 auto;
    flex-direction: column;
  }
}
</style>
