<template>
  <div class="mission">
    <transition name="fade" >
      <div v-if="toast.visible" class="toast">{{toast.message}}</div>
    </transition>
    <header>
      <h2>{{mission.title}}</h2>
      <h3>{{mission.subtitle}}</h3>
    </header>
    <div class="mission-text" v-html="mission.text">
    </div>
    <div class="grandesLignes btn" v-if="mission.basic.length">
      <div v-on:click="displayBasic = !displayBasic">
        <img  class="icone" src="/static/images/checklist2.png"/> Les grandes lignes
      </div>
      <slide-up-down :active="displayBasic" :duration="500" class="wrapper">
        <ul>
          <li v-for="item in mission.basic">
            <span v-if="item.html" v-html="item.html"></span>
          </li>
        </ul>
      </slide-up-down>
    </div>
    <div class="pasApas btn" v-if="mission.steps.length">
      <div v-on:click="displaySteps = !displaySteps">
        <img class="icone" src="/static/images/pas_a_pas.png"/> Le pas à pas
      </div>
      <slide-up-down :active="displaySteps" :duration="500" class="wrapper">
        <ul>
          <li v-for="item in mission.steps">
            <span class="instruction" v-if="item.html" v-html="item.html"></span>
            <div class="python" v-if="item.python">
              <button v-if="displaySteps" type="button" class="copy-btn"
                title="Copier"
                v-clipboard:copy="item.python"
                v-clipboard:success="onClipCopy"
                v-clipboard:error="onClipError"><img src="/static/images/clipboard.png"/></button>
              <span>
                <pre v-highlightjs><code class="python">{{item.python}}</code></pre>
              </span>
            </div>
          </li>
        </ul>
      </slide-up-down>
    </div>
    <div class="question" v-if="mission.question">
      <span v-html="mission.question.statement"></span>
      <input type="text" v-model="response"/>
    </div>
    <nav>
      <router-link v-if="missionIndex > 1"
        :to="{ name: 'Mission', params: { index: missionIndex - 1 }}"
        tag="button" class="back">Retour</router-link>
      <router-link v-if="last && (solved || !mission.question)"
        :to="{ name: 'Mission', params: { index: 1 }}"
        tag="button" class="done">Retour au début</router-link>
      <router-link v-if="!last && (solved || !mission.question)"
        :to="{ name: 'Mission', params: { index: missionIndex + 1 }}"
        tag="button" class="done">Mission accomplie</router-link>
    </nav>
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
      response: null,
      solved: false,
      displayBasic: false,
      displaySteps: false,
      mission: missions[index - 1],
      toast: {
        visible: false,
        message: ''
      }
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
      this.response = ''
    },
    'response' (val, oldVal) {
      const reg = this.mission.question ? this.mission.question.response : null
      let re = new RegExp(reg)
      if (val) {
        this.solved = val.match(re) !== null
      } else {
        this.solved = false
      }
    }
  },
  methods: {
    onClipCopy: function (e) {
      this.toast.message = 'Copié: ' + e.text
      this.toast.visible = true
      setTimeout(() => { this.toast.visible = false }, 3000);
    },
    onClipError: function (e) {
      console.error('Failed to copy texts')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.toast {
  position: fixed;
  color: white;
  font-weight: bold;
  bottom: 10px;
  right: 10px;
  background: #4791ae;
  padding: 10px;
  width: 35%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  border-radius: 6px;
  font-size: 0.8rem;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .6s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

.mission {
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
  letter-spacing: .2rem;
  text-shadow: -1px  1px 2px #a8523a,
                1px  1px 2px #a8523a,
                1px -1px 0   #a8523a,
               -1px -1px 0   #a8523a;
}
h3 {
  color:white;
  text-shadow: -1px  1px 2px #555,
                1px  1px 2px #555,
                1px -1px 0   #555,
               -1px -1px 0   #555;
}

.grandesLignes > div:first-child, .pasApas > div:first-child {
  user-select: none;
  cursor: pointer;
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
  min-width: 95%;
  margin: 20px 20px 0 20px;
  border: 1px solid #DDD;
  background-color: #EEE;
  border-radius: 7px;
}

.wrapper {
  background-color:#FFF;
  width: 100%;
}

ul {
  list-style: none;
  padding: 8px;
  margin: 0;
}

li {
  padding-top: 4px;
  padding-bottom: 4px;
}
ul .instruction {
  background: white;
}
.python {
  position: relative;
}
.python pre {
  margin: 0;
  font-size: 0.7rem;
}
.copy-btn {
  position: absolute;
  z-index: 10;
  right: 4px;
  padding: 2px;
  margin-top: 4px;
  background-color: unset;
  opacity: 0.4;
  transition: opacity 300ms, border 300ms;
}
.copy-btn:hover {
  background-color: unset;
  border: 1px solid #777;
  opacity: 1;
}
.copy-btn img {
  width: 20px;
  height: 16px;
  margin-top: 2px;
}

.marge {
  margin-left: 30px;
}

.question {
  margin: 20px;
}

.question input[type="text"]{
  height: 30px;
  width: 200px;
  font-size: 0.9rem;
  border: none;
  border-bottom: 1px solid black;
  margin-left: 20px;
  padding: 0 8px;
  font-family: Verdana;
}

nav {
  display: flex;
}

button {
  display: inline-block;
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
  transition: color .15s ease-in-out,background-color .15s ease-in-out, border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

button:hover {
  background-color: #076e84;
  border-color: #076e84;
}

</style>
