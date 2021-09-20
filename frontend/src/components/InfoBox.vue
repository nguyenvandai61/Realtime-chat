<template>
  <div class="info-box">
    <div class="info-box__avatar">
      <v-avatar>
        <img :src="avatar" alt="" />
      </v-avatar>
    </div>
    <div class="info-box__name">
      <span>{{ name }}</span>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "InfoBox",
  props: {
    avatar: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
});
</script>
<style lang="scss" scoped>
.info-box {
  display: inline-block;
  width: 200px;
  padding: 5px;
  background-color: #fff0;
  border-radius: 5px;
  margin-bottom: 5px;
  margin-left: 5px;
  .info-box__avatar {
    display: inline-block;
    margin-right: 15px;
  }
  .info-box__name {
    display: inline-block;
  }
}
</style>
