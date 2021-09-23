<template>
  <div class="reaction-emotion">
    <div class="reaction-emotion__emotions">
      <div
        v-for="emotion in emotions"
        :key="emotion.id"
        class="reaction-emotion__emotion"
      >
        <img :src="emotion.icon" alt="" />
        <div v-show="emotion.count > 1" class="reaction-emotion__count">
          {{ emotion.count }}
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: {
    // emotions: {
    //   type: Array,
    // },
  },
  data() {
    return {
      emotions: [
        {
          id: 1,
          icon: "https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",
          count: 1,
        },
        {
          id: 2,
          icon: "https://i.pinimg.com/originals/7d/a7/9d/7da79d025be28d28588f8bdc23c1456e.png",
          count: 2,
        },
      ],
    };
  },
});
</script>
<style lang="scss" scoped>
.reaction-emotion {
  display: flex;
  position: absolute;
  top: 10px;
  right: 3px;
  margin: 0.5rem;
  .reaction-emotion__emotions {
    display: flex;
    .reaction-emotion__emotion {
      display: flex;
      img {
        width: 20px;
      }
      .reaction-emotion__count {
        position: absolute;
        right: -5px;
        bottom: -10px;
        font-weight: 600;
        color: black;
      }
    }
  }
}
</style>
