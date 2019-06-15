<template>
  <div id="app">
    <h1><span>TP  Python :</span> Où sont mes photos de Mayotte ?</h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300|Raleway&display=swap');

html, body{
  margin:0;
  padding: 0;
  background-color: #EEE;
  font-size: 20px;
  font-family: 'Raleway', sans-serif;
}

body{
  padding-bottom: 50px;
}

h1{
  font-size: 1.5em;
  text-align: center;
  color: #556;
  font-family: 'Roboto', sans-serif;
}

h1 > span{
  text-align: right
}

#app {

}
</style>
