<template>
  <div class="slides">
    <!-- Intro -->
    <section :data-background-image="this.dnaImg">
      <h3>Clinical Bioinformatics Unit</h3>
      <table> 
      <tr>
        <td><p class="small">Dr. Simon Sadedin</p></td>
        <td><img src="./images/ss.jpg"/></td>
        <td><p class="small">Damien Zammit</p></td>
        <td><img src="./images/dz.jpg"/></td>
        </tr>
        <tr>
        <td><p class="small">Macgregor Todd</p></td>
        <td><img src="./images/mt.jpg"/></td>
        <td><p class="small">Christopher Ieng<br/>(me!)</p></td>
        <td><img src="./images/ci.jpg"/></td>
        </tr>
        </table>
    </section>
    <section>
      <h3> What do we actually do? </h3>
    </section>
    <section>
      <h3> CBU Operations </h3>
      <p class="small"> <em> Figure: CBU Team commiunicating via zoom</em></p>
      <table> 
      <tr>
        <td><p class="small">Dr. Simon Sadedin</p></td>
        <td><img width="230px" height="230px" src="https://media2.giphy.com/media/E6jscXfv3AkWQ/giphy.gif?cid=ecf05e47bdf76982a62adcd29b5159e3a415381766a9cf1c&rid=giphy.gif"/></td>
        <td><p class="small">Damien Zammit</p></td>
        <td><img width="240px" height="230px" src="https://media.giphy.com/media/vqJAJMr4klojK/giphy.gif"/></td>
        </tr>
        <tr>
        <td><p class="small">Macgregor Todd</p></td>
        <td><img width="230px" height="230px" src="https://media.giphy.com/media/13HBDT4QSTpveU/giphy.gif"/></td>
        <td><p class="small">Christopher Ieng<br/></p></td>
        <td><img width="230px" height="230px" src="https://media.giphy.com/media/unQ3IJU2RG7DO/giphy.gif"/></td>
        </tr>
        </table>
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
.small {
  font-size: 18px;
}
</style>
