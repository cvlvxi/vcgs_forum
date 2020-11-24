<template>
  <div class="slides">
    <!-- Intro -->
    <section :data-background-image="this.dnaImg">
      <h3 class="shadow">Clinical Bioinformatics Overview</h3>
      <p class="shadow">Christopher Ieng</p>
    </section>
    <section>
      HERE IS SOME TEXT
      <iframe
        width="100%"
        height="800"
        frameborder="0"
        src="https://observablehq.com/embed/@cvlvxi/brushable-scatterplot?cell=viewof+selection"
      ></iframe>
    </section>
    <section>
      HERE IS SOME MORE TEXDT
      <iframe
        width="100%"
        height="681"
        frameborder="0"
        src="https://observablehq.com/embed/@d3/bar-chart-race?cell=chart"
      ></iframe>
    </section>
  </div>
</template>

<script>
import DeckMixin from "./DeckMixin";

export default {
  name: "App",
  mixins: [DeckMixin],
  components: {},
  data() {
    return {};
  }
};
</script>

<style scoped>
.shadow {
  color: white;
  text-shadow: 2px 2px #000 !important;
}
</style>
