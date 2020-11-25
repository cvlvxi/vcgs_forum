<template>
  <div class="slides">
    <!-- Intro -->
    <section>
      <h3>Clinical Bioinformatics Unit</h3>
    </section>
    <Slide1/>
    <Slide2/>
    <Slide10/>


    <section>
      <h3> What are you grateful for? </h3>
      <img src="./images/dz.jpg"/>
      <p class="medium"><em>
"Grateful for coffee takeaways still being sold at cafes, keeps the business running and gives me a boost of caffeine in the morning"
</em></p>
    </section>
    <Slide5/>
    <section>
      <h3> What are you grateful for? </h3>
      <img src="./images/ci.jpg"/><br/>
      <p class="medium"><em>"I'm grateful for being constantly intrigued and being able to endlessly learn new things whether it be in programming, stats, or biology...</em></p>
    </section>
    <Slide9/>
    <section>
      <h3> What are you grateful for? </h3>
      <img src="./images/mt.jpg"/><br/>
      <p class="medium"><em>"I suppose the increased work flexibility given the back problems I was having. <br/>
    I discovered + learned - how to play tennis in the local park without a court - and to play left handed!"</em></p>
    </section>
    <Slide4/>
    <section>
      <h3> What are you grateful for? </h3>
      <img src="./images/ss.jpg"/>
      <p class="medium"><em>"I am grateful that our team really responded well to moving remote - despite it being pretty tough for some of us, everyone held up and really kept up the work doing what needed to be done to keep things running"</em></p>
    </section>
    <Slide3/>
    <section>
      <h3> Good job all 🎉 </h3>
      <img src="https://media.giphy.com/media/11ISwbgCxEzMyY/giphy.gif"/>
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
    Slide10
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
