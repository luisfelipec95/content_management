<template>
  <div class="wrap">
    <div class="search">
      <input type="text" class="searchTerm" v-model="pattern" placeholder="What are you looking for?">
      <button @click="search" class="searchButton">
        <i class="fa fa-search"></i>
     </button>
   </div>
        <div v-for="content in contents">
          {{ content.name }}
        </div>
      
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  layout: "empty",
  head() {
    return {
      title: 'Content Management | Home',
      meta:[
        {
          hid: "description",
          name: 'description',
          content: 'Prueba técnica Nuevosmedios'
        }
        
      ],
      htmlAttrs: {
        lang: 'es'
      }
    }
  },
  data() {
    return {
      pattern: '',
      
    }
  },
  name: 'IndexPage',
  mounted: function() {
    this.$store.dispatch('contents/fetchContents');
  },
  methods: {
    search(){
      this.contents = this.pattern
    }
  },
  computed: {
    contents: {
      get() {
        return this.$store.getters['contents/getContents'];
      },
      set(pattern) {
        this.$store.commit("contents/filterContents", pattern);
      }
    }
  },
  
}
</script>
<style>
  @import url(https://fonts.googleapis.com/css?family=Open+Sans);

body{
  background: #f2f2f2;
  font-family: 'Open Sans', sans-serif;
}

.search {
  width: 100%;
  position: relative;
  display: flex;
}

.searchTerm {
  width: 100%;
  border: 3px solid #00B4CC;
  border-right: none;
  padding: 5px;
  height: 20px;
  border-radius: 5px 0 0 5px;
  outline: none;
  color: #9DBFAF;
}

.searchTerm:focus{
  color: #00B4CC;
}

.searchButton {
  width: 40px;
  height: 36px;
  border: 1px solid #00B4CC;
  background: #00B4CC;
  text-align: center;
  color: #fff;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  font-size: 20px;
}

/*Resize the wrap to see the search bar change!*/
.wrap{
  width: 30%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>