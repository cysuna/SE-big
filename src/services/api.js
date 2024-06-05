import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getQuestions() {
    return apiClient.get('/questions/')
  },
  // 其他API调用方法
}
