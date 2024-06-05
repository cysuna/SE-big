import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    axios.get('/api/questions/')
      .then(response => {
        setQuestions(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the questions!', error);
      });
  }, []);

  return (
    <div>
      <h1>Question List</h1>
      <ul>
        {questions.map(question => (
          <li key={question.id}>{question.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
