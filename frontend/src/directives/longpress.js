import Vue from "vue";

Vue.directive("longpress", {
  bind: function (el, binding, vnode) {
    let pressTimer;
    const press = () => {
      if (typeof binding.value !== "function") {
        console.error("longpress binding value must be a function");
        return;
      }
      if (binding.value) {
        binding.value(vnode.context);
      }
    };
    el.addEventListener("mousedown", () => {
      pressTimer = setTimeout(press, 500);
    });
    el.addEventListener("mouseleave", () => {
      clearTimeout(pressTimer);
    });
    el.addEventListener("mouseup", () => {
      clearTimeout(pressTimer);
    });
    // Touch devices
    el.addEventListener("touchstart", () => {
      pressTimer = setTimeout(press, 500);
    });
    el.addEventListener("touchend", () => {
      clearTimeout(pressTimer);
    });
    el.addEventListener("touchcancel", () => {
      clearTimeout(pressTimer);
    });
  },
});

Vue.directive("longpress-stop", {
  bind: function (el, binding, vnode) {
    const stop = () => {
      if (typeof binding.value !== "function") {
        console.error("longpress-stop binding value must be a function");
        return;
      }
      if (binding.value) {
        binding.value(vnode.context);
      }
    };
    el.addEventListener("mouseleave", stop);
    // Touch devices
    el.addEventListener("touchcancel", stop);
  },
});
