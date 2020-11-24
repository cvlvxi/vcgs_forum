<template>
  <div class="slides">
    <!-- Intro -->
    <section>
      <h3>Clinical Bioinformatics Unit</h3>
    </section>
    <Slide1/>
    <Slide2/>
    <Slide3/>
    <Slide4/>
    <Slide5/>
    <Slide6/>
    <Slide7/>
    <Slide8/>
  </div>
</template>

<script>
import DeckMixin from "./DeckMixin";
import Slide1 from "./slides/Slide1"
import Slide2 from "./slides/Slide2"
import Slide3 from "./slides/Slide3"
import Slide4 from "./slides/Slide4"
import Slide5 from "./slides/Slide5"
import Slide6 from "./slides/Slide6"
import Slide7 from "./slides/Slide7"
import Slide8 from "./slides/Slide8"

export default {
  name: "App",
  mixins: [DeckMixin],
  components: {
    Slide1, 
    Slide2,
    Slide3,
    Slide4,
    Slide5,
    Slide6,
    Slide7,
    Slide8
  },
  data() {
    return {};
  }
};
</script>

<style>
.shadow {
  color: white;
  text-shadow: 2px 2px #000 !important;
}
.small {
  font-size: 18px;
}
</style>
