<template>
  <div class="home">
    <div class="home__header">
      <h1>Home</h1>
    </div>
    <div class="home__content">
      <div class="home__list-row-rooms">
        <row-room
          v-for="rowRoom in rooms"
          :room="rowRoom"
          :key="rowRoom.id"
        ></row-room>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import RowRoom from "@/components/RowRoom.vue";
import Vue from "vue";

export default Vue.extend({
  name: "Home",

  components: {
    RowRoom,
  },
  data() {
    return {
      rooms: [
        {
          id: 1,
          title: "Room 1",
          no_members: 2,
          user_avatars: [
            {
              id: 1,
              avatar:
                "https://avatars3.githubusercontent.com/u/14785789?v=3&s=460",
            },
            // {
            //   id: 2,
            //   avatar:
            //     "https://avatars3.githubusercontent.com/u/14785990?v=3&s=460",
            // },
          ],
          last_message: {
            sender: {
              id: 1,
              first_name: "Crys",
            },
            message: "Chào buổi sáng",
            created_at: "9h45",
            status: "seen",
          },
          is_notified: true,
        },

        {
          id: 2,
          title: "Room 2",
          no_members: 3,
          user_avatars: [
            {
              id: 1,
              avatar:
                "https://avatars3.githubusercontent.com/u/14785789?v=3&s=460",
            },
            {
              id: 2,
              avatar:
                "https://avatars3.githubusercontent.com/u/14785990?v=3&s=460",
            },
          ],
          last_message: {
            sender: {
              id: 1,
              first_name: "Crys",
            },
            message: "Chào buổi sáng",
            created_at: "9h45",
            status: "seen",
          },
          is_notified: false,
        },
      ],
    };
  },
});
</script>
<style lang="scss" scoped>
.home {
  .row-room {
    margin: auto 10px;
    margin-bottom: 20px;
    height: 70px;
  }
}
</style>
