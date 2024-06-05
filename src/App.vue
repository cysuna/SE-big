<template>
    <div id="app">
      <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">Home</el-menu-item>
          <el-menu-item index="2">Questions</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </div>
  </template>
  
  <script>
  export default {
    name: 'App',
    data() {
      return {
        activeIndex: '1'
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        if (key === '1') {
          this.$router.push('/')
        } else if (key === '2') {
          this.$router.push('/questions')
        }
      }
    }
  }
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  