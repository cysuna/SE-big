<template>
  <div>
    <el-table :data="questions" style="width: 100%">
      <el-table-column prop="question_text" label="Question" width="400"></el-table-column>
      <el-table-column prop="question_type" label="Type" width="150"></el-table-column>
      <el-table-column prop="difficulty" label="Difficulty" width="100"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'Questions',
  data() {
    return {
      questions: []
    }
  },
  created() {
    this.fetchQuestions()
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await api.getQuestions()
        this.questions = response.data
      } catch (error) {
        console.error('Failed to fetch questions:', error)
      }
    }
  }
}
</script>
