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
    <section class='content-container'>
        <div class='content-nav'>
            <h2>Programación</h2>
            <nav class='content-nav-items'>
              <ul>
                <li><a href="*">Variables</a></li>
                <li><a href="*">Estructuras</a></li>
                <li><a href="*">Reactividad</a></li>
                <li><a href="*">Http Client</a></li>
                <li><a href="*">Dinámico</a></li>
                <li><a href="*">Akka</a></li>
                <li><a href="*" style="font-weight: bold;">Introduction to Java Structures</a></li>
              </ul>
            </nav>
        </div>
        <article>
            <h1>Introduction to Java Structures</h1>
            <div class='content-meta'>
              <ul>
                <li>Article ▪</li>
                <li>04/13/2022 ▪</li>
                <li>2 minutes to read ▪</li>
                <li>2 contributors</li>
              </ul>
              <span><i class="fa fa-eye" aria-hidden="true"></i>Visto</span>
            </div>
            <img src="~/assets/java.webp" class='content-banner'>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed venenatis eros ut dui pretium auctor. Morbi vel molestie nibh. Fusce non pharetra nulla. Quisque turpis justo, dictum ut tellus quis, ornare aliquet massa. Ut consequat sit amet massa sed auctor. Ut fermentum nibh nibh. Proin ornare a neque vel viverra. Vivamus consequat feugiat nunc, eget volutpat eros laoreet non. Donec faucibus ante magna, non consectetur erat volutpat eget. Phasellus aliquam sapien a nulla rutrum cursus. Sed sollicitudin venenatis tellus, vitae hendrerit lacus condimentum non.</p>
            <p>Curabitur velit magna, auctor in diam ut, aliquam tempor ex. Sed at felis sed lectus pulvinar ornare tempor et odio. Nam rutrum neque id tellus finibus iaculis. Cras pulvinar iaculis elit, congue pretium sapien. Donec vitae pretium turpis, pellentesque iaculis orci. Integer imperdiet purus id neque venenatis tristique. Phasellus at auctor quam. Quisque interdum turpis nec accumsan molestie. Vestibulum ut gravida nulla, sed bibendum justo. Suspendisse id ligula laoreet magna condimentum tincidunt. Integer auctor sit amet tortor eget finibus.</p>
            <p>Ut posuere leo dignissim, sollicitudin nibh vitae, varius nunc. Aenean efficitur tincidunt justo at fermentum. Curabitur consectetur nulla at mattis dignissim. In nibh est, viverra vel lacinia vel, sagittis aliquam odio. Ut vel lorem a quam interdum maximus. Donec eu quam pellentesque, molestie erat eget, pretium massa. In ultrices scelerisque arcu, eu pharetra libero ultricies eu. Etiam efficitur bibendum libero. Donec ac metus pulvinar, blandit ligula sed, vulputate lorem. Vivamus volutpat at mi id sollicitudin. Fusce congue arcu ac tempus rhoncus. Nulla egestas elit ac felis ultrices porttitor. Sed vitae dolor condimentum, vulputate arcu ac, tincidunt nisl. Ut eget ante massa.</p>
            <p>Phasellus eros justo, maximus quis rutrum et, pulvinar nec urna. Mauris ac rutrum ante. Nunc ac massa dui. Praesent pellentesque efficitur fermentum. Mauris nec rhoncus arcu, eu venenatis odio. Maecenas congue sapien condimentum felis bibendum efficitur. Aliquam et varius turpis. Integer pellentesque lorem erat, sit amet fringilla purus blandit non. Sed auctor orci quis lectus luctus sodales. Duis molestie malesuada commodo. Aliquam viverra blandit nulla ac dignissim. Donec consequat tellus sed faucibus ornare.</p>
            <p>Praesent rhoncus dui ut ipsum aliquet tempor. Etiam non malesuada ligula. Cras et sapien nec justo blandit tincidunt quis ac ex. Phasellus et mattis dolor, vel suscipit justo. Nunc a dictum risus. Integer sodales augue commodo, mattis massa a, venenatis neque. Etiam dictum mauris eget sapien fringilla, nec sollicitudin dui facilisis. Maecenas tristique, massa ac viverra bibendum, nibh felis porttitor justo, id venenatis neque dui sed lacus.</p>
            <div>
              <button>Previous</button>
              <button>Next</button>
            </div>
        </article>
    </section>
  </div>
</template>

<script>
  export default {
    layout: 'empty',
    computed: {
      category: { 
        get() { this.$store.getters['contents/getCategory']; },
        set(category) { this.$store.commit('contents/updateCategory', this.newCategory); }
      }
    },
    data() {
      return {
        newCategory: '',
      } 
    }
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

  .content-container {
      display: flex;
      .content-nav {
        width: 20vw;
        .content-nav-items {
          margin-left: 3vw;
          margin-top: 1vw;
          ul > li > a {
            text-decoration: none;
            color: #171717;
            word-wrap: break-word;
            cursor: pointer;
            &:hover {
              text-decoration: underline;
            }
          }
        }
      }
      article {
          margin: 0 2vw;
          padding: 0 10vw;
          h1{
            word-wrap: break-word;
            font-size: clamp(1.875rem,22.1052631579px + 1.6447368421vw,2.5rem);
          }
          .content-meta {
            display: flex;
            justify-content: space-between;
            font-size: .875rem;
            ul {
              display: flex;
              flex-wrap: wrap;
              list-style: none;
              padding: 0.125rem 0 0 0;
              font-size: .875rem;
              color: #505050;
              li {
                margin-right: 3px;
              }
            }
          }
          .content-banner {
            width: 100%;
            margin-top: 2%;
          }
          p {
            margin-top: 1rem;
            word-wrap: break-word;
            color: #171717;
          }
      }
  }

</style>