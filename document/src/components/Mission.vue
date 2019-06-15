<template>
  <div class="mission">
    <header>
      <h2>{{mission.title}}</h2>
      <h3>{{mission.subtitle}}</h3>
    </header>
    <div class="mission-text" v-html="mission.text">
    </div>
    <div class="grandesLignes btn" >
      <div v-on:click="displayBasic = !displayBasic">
        <img  class="icone" src="/static/images/checklist2.png"/> Les grandes Lignes
      </div>
      <div v-if="displayBasic" class="wrapper">
        <ul>
          <li v-for="item in mission.basic">
            <span v-if="item.html" v-html="item.html"></span>
          </li>
        </ul>
      </div>
    </div>
    <div class="pasApas btn">
      <div v-on:click="displaySteps = !displaySteps">
        <img class="icone" src="/static/images/pas_a_pas.png"/> Le pas à pas
      </div>
      <div v-if="displaySteps" class="wrapper">
        <ul>
          <li v-for="item in mission.steps">
            <span v-if="item.html" v-html="item.html"></span>
            <span v-if="item.python">
              <pre v-highlightjs><code class="python">{{item.python}}</code></pre>
            </span>
          </li>
        </ul>
      </div>
    </div>
    <router-link v-if="last"
      :to="{ name: 'Mission', params: { index: 1 }}"
      tag="button" class="done">Retour au début</router-link>
    <router-link v-else
      :to="{ name: 'Mission', params: { index: missionIndex + 1 }}"
      tag="button" class="done">Mission accomplie</router-link>
  </div>
</template>

<script>
import missions from './missions.json'
export default {
  name: 'Mission',
  data () {
    let index = parseInt(this.$route.params.index) || 1
    if (index > missions.length) { index = 1 }
    return {
      missionIndex: index,
      last: index === missions.length,
      displayBasic: false,
      displaySteps: false,
      mission: missions[index - 1]
    }
  },
  watch: {
    '$route' (to, from) {
      let index = parseInt(to.params.index) || 1
      if (index > missions.length) { index = 1 }
      this.missionIndex = index
      this.last = index === missions.length
      this.displayBasic = false
      this.displaySteps = false
      this.mission = missions[index - 1]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.mission{
  margin:auto;
  width: 95%;
  max-width: 800px;
  box-shadow: 0 2px 2px #999;
  background-color:#e1f5fc;
  color:#444;
  padding-bottom: 20px;
}

.mission-text{
  padding-left: 30px;
  padding-right: 30px;
}

header {
  background-image:url('../images/mission.jpg');
  background-size:cover;
  min-height:200px;
  padding: 10px;
}
h2 {
  color: #f2704c;
}
h3 {
  max-width: 75%;
  color:white;
}

.icone {
  height: 42px;
  width:42px;
  border-right:1px solid #DDD;
  padding-right: 10px;
  padding-top: 5px;
  padding-bottom: 5px;
  padding-left: 5px;
  margin-right: 10px;
  vertical-align: middle;
}

.btn {
  display: inline-block;
  /*min-width: 45%;*/
  min-width: 95%;
  margin-top: 20px;
  margin-left: 20px;
  border: 1px solid #DDD;
  background-color: #EEE;
  border-radius: 7px;
}

.btn :hover {
  /*background: lightgray;*/
}

.wrapper {
  background-color:#FFF;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 100%;
}

ul {
  list-style: none;
  padding:0;

}

li {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
}
ul :nth-child(2n) {
  background-color: #EEE;
}

.marge {
  margin-left: 30px;
}

.mission button.done {
  display: block;
  background-color: #277c99;
  border-color: #277c99;
  color: #fff;
  font-weight: 400;
  text-align: center;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  margin: .75rem auto 0 auto;
  padding: .375rem .75rem;
  font-size: 0.75rem;
  line-height: 1.2;
  border-radius: .25rem;
  transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}
.mission button.done:hover {
  background-color: #076e84;
  border-color: #076e84;
}
</style>
