<template>
  <div class="slides">
    <!-- Intro -->
    <section>
      <h3>Clinical Bioinformatics Unit</h3>
    </section>
    <Slide1/>
    <Slide2/>
    <Slide3/>
    <Slide10/>
    <section>
      <img src="./images/dz.jpg"/>
      <h3> What are you grateful for? </h3>
      <p class="medium"><em>
"Grateful for coffee takeaways still being sold at cafes, keeps the business running and gives me a boost of caffeine in the morning"
</em></p>
    </section>
    <Slide5/>
    <section>
      <img src="./images/ci.jpg"/><br/>
      <h3> What are you grateful for? </h3>
    </section>
    <Slide11/>
    <Slide9/>
    <section>
      <img src="./images/mt.jpg"/><br/>
      <h3> What are you grateful for? </h3>
      <p class="medium"><em>"The increased work flexibility given the back problems I was having. <br/>
    I discovered how to play tennis in the local park without a court and to play left handed!"</em></p>
    </section>
    <Slide4/>
    <section>
      <img src="./images/ss.jpg"/>
      <h3> What are you grateful for? </h3>
      <p class="medium"><em>"I am grateful that our team really responded well to moving remote. <br/>Despite it being pretty tough for some of us, everyone held up and really kept up the work doing what needed to be done to keep things running"</em></p>
    </section>
    <section>
      <h3> Good job all 🎉 </h3>
      <img src="https://media.giphy.com/media/11ISwbgCxEzMyY/giphy.gif"/>
      <h3> Let's get through this together! </h3>
    </section>
  </div>
</template>

<script>
import DeckMixin from "./DeckMixin";
import Slide1 from "./slides/Slide1"
import Slide2 from "./slides/Slide2"
import Slide3 from "./slides/Slide3"
import Slide4 from "./slides/Slide4"
import Slide5 from "./slides/Slide5"
import Slide9 from "./slides/Slide9"
import Slide10 from "./slides/Slide10"
import Slide11 from "./slides/Slide11"

export default {
  name: "App",
  mixins: [DeckMixin],
  components: {
    Slide1, 
    Slide2,
    Slide3,
    Slide4,
    Slide5,
    Slide9,
    Slide10,
    Slide11
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
.medium {
  font-size: 25px;
}
</style>
