<template>
  <div class="reveal">
    <router-view />
  </div>
</template>

<script>
import "reveal.js/dist/reveal.css";
import "reveal.js/dist/theme/solarized.css";
import RevealHighlight from "reveal.js/plugin/highlight/highlight.js";
import RevealMarkdown from "reveal.js/plugin/markdown/markdown.js";
import RevealNotes from "reveal.js/plugin/notes/notes.js";
import Reveal from "reveal.js";
import "./css/monokai.css";
import img from "./images/vcgs.png";

export default {
  name: "App",
  mounted: function() {
    window.deck = new Reveal({});

    window.deck.initialize({
      slideNumber: true,
      plugins: [RevealMarkdown, RevealHighlight, RevealNotes],
      parallaxBackgroundImage: img,
      parallaxBackgroundPosition: "bottom left",
      parallaxBackgroundRepeat: "no-repeat"
    });
  }
};
</script>

<style>
.smallfont {
  font-size: 50% !important;
}
.med {
  font-size: 75% !important;
}

.al {
  text-align: left !important;
}
</style>
