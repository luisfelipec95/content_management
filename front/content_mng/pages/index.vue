<template>
  <div id='home-container'>
    <div class='home-header'>
      <h1 class='home-header-title-medium'>Nuevos Medios</h1>
      <h1 class='home-header-title-small'>NM</h1>
      <div>
        <input class='search-bar' type='search' v-model="pattern" placeholder='¿Qué deseas aprender?'>
        <i class="fa fa-search" aria-hidden="true" @click="search"></i>
      </div>
    </div>
    <section class='popl-section'>
      <div class='popl-cour-crsl-container'>
        <div class='popl-cour-crsl'>
          <img src='~/assets/cripto.jpg' class='popl-cour-crsl-img'>
          <img src='~/assets/cripto.jpg' class='popl-cour-crsl-img'>
          <img src='~/assets/cripto.jpg' class='popl-cour-crsl-img'>
          <img src='~/assets/cripto.jpg' class='popl-cour-crsl-img'>
        </div>
      </div>
      <div class="popl-cour-crsl-inds">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>
    </section>
    <div class='ctgs-container'>
      <div class='ctgs-header'>
        <h2>Categorías</h2>
      </div>
      <div class='ctgs-crsl-container'>
        <div class='ctgs-crsl'>
          <div class='ctgs-item' v-for="content in contents">
            <a href='/content' @click="updateCategory">{{ content.name }}</a>
          </div>
        </div>
        <button class='ctgs-acts ctgs-acts-previous' :style="{visibility: isPreviousVisible ? 'visible' : 'hidden'}">
          <i class="fa fa-chevron-left" aria-hidden="true"></i>
        </button>
        <button class='ctgs-acts ctgs-acts-next' :style="{visibility: isNextVisible ? 'visible' : 'hidden'}">
          <i class="fa fa-chevron-right" aria-hidden="true"></i>
        </button>
      </div>
    </div>  
  </div>
</template>

<script>
export default {
  layout: "empty",
  data() {
    return {
      pattern: '',
      isPreviousVisible: true,
      isNextVisible: true,
    }
  },
  name: 'IndexPage',
  mounted: function() {
    this.$store.dispatch('contents/fetchContents');
  },
  methods: {
    search(){ this.contents = this.pattern },
    updateCategory(e) { this.$store.commit('contents/updateCategory', e) }
  },
  computed: {
    contents: {
      get() { return this.$store.getters['contents/getContents']; },
      set(pattern) { this.$store.commit("contents/filterContents", pattern); }
    }
  },
}
</script>

<style lang='scss'>
  @import url(https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap);

  $mg-main-palette-c1: #0056d2;
  $mg-main-palette-c2: #fff;
  $mg-main-palette-c3: #4B4848;
  $mg-main-palette-c4: #636363;

  $small-screen: 450px;
  $medium-screen: 800px;
  $crsl-speed: 10s;

  #home-container {
    display: flex;
    flex-direction: column;
    font-family: 'Montserrat', 'Helevtica', sans-serif;
    .home-header {
      display: flex;
      padding-bottom: 10px; 
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(0,0,0,.12);
      h1 {
        color: $mg-main-palette-c1;
        margin: 0 20px 0 0;
      }
    }
  }

  .home-header-title-medium {
    @media screen and (max-width: $small-screen) {
      display: none;
    }
    @media screen and (min-width: $medium-screen) {
      display: block;
    }
  }
  .home-header-title-small {
    @media screen and (max-width: $small-screen) {
      display: block;
    }
    @media screen and (min-width: $medium-screen) {
      display: none;
    }
  }

  .search-bar {
    border: 0;
    height: 100%;
    padding: 10px 20px;
    background: white;
    border: 1px solid $mg-main-palette-c4;
    border-radius: 3px;
    transition: all 0.4s ease;
    &:focus {
      border: 1px solid $mg-main-palette-c1;
      outline: none;
    }
    @media screen and (max-width: $small-screen) {
      width: 65vw;
    }
    @media screen and (min-width: $medium-screen) {
      width: 50vw;
    }
  }

  .fa-search {
    position: relative;
    cursor: pointer;
    @media screen and (max-width: $small-screen) {
      left: -10%;
    }
    @media screen and (min-width: $medium-screen) {
      left: -6%;
    }
  }

  @keyframes crsl-scroll {
	  0% { transform: translateX(0); }
	  100% { transform: translateX(-50%); }
  }

  .popl-section {
    width: 100%;
    flex-direction: column;
    .popl-cour-crsl-container {
      height: 40vh;
      overflow: hidden;
      .popl-cour-crsl {
        position: relative;
        display: flex;
        height: inherit;
        width: inherit;
        animation: crsl-scroll $crsl-speed linear infinite;
        display: flex;
        width: 200%;
        .popl-cour-crsl-img {
          height: inherit;
          width: 1166px;
        }
      }
    }
    .popl-cour-crsl-inds {
      margin: 10px 0;
      text-align: center;
      span {
        display: inline-block;
        background-color: #d1d7dc;
        width: 30px;
        height: 4px;
        border-radius: 2px;
        opacity: .8;
        cursor: pointer;
        margin: 3px;
        &:active {
          opacity: 1;
          background-color: $mg-main-palette-c1;
        }
      }
    }
  }

  .ctgs-header {
    display: flex;
    justify-content: center;
    margin: 20px 0 20px 0;
    padding: 0 5%;
  }

  .ctgs-crsl-container {
    position: relative;
  }
  .ctgs-crsl {
    display: grid;
    align-items: center;
    justify-items: center;
    width: 100%;
    max-width: 99%;
    height: 18vh;
    grid-template-rows: repeat(2,1fr);
    grid-gap: 0.8rem;
    grid-auto-flow: column;
    overflow-x: hidden;
    padding: 0 5%;
    @media screen and (max-width: $small-screen) {
      grid-auto-columns: calc((102% - (2 - 1) * 0.8rem)/2);
    }
    @media screen and (min-width: $medium-screen) {
      grid-auto-columns: calc((100% - (3 - 1) * 0.8rem)/3);
    }
    .ctgs-item {
      height: 100%;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      border: 1px solid #d1d7dc;
      cursor: pointer;
      &:hover{
        background-color: #f7f9fa;
      }
      a{
        color: #1c1d1f;
        text-decoration: none;
        font-weight: bold;
        line-height: 1.2;
        letter-spacing: -.02rem;
      }
    }
  }

  .ctgs-acts {
    position: absolute;
    top: 2rem;
    padding: 0 1rem;
    width: 3rem;
    height: 3em;
    border-radius: 50%;
    background-color: $mg-main-palette-c1;
    i {
      color: $mg-main-palette-c2;
      font-size: 1.5em;
    }
    &:hover {
      	background-color: #{$mg-main-palette-c1}E6;
    }
  }

  .ctgs-acts-previous {
    left: calc(4.5% - (3 - 1) * 0.8rem);
    i {
      right: 2px;
      position: relative;
    }
  }
  .ctgs-acts-next {
    right: calc(5.5% - (3 - 1) * 0.8rem);
  }

</style>