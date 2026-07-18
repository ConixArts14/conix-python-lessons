// Day 53 - Calculator App (Node.js Backend Setup)

const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;

// Middleware to parse JSON
app.use(express.json());

// Enable CORS
app.use(cors());

// Test route
app.get('/', (req, res) => {
  res.send('Calculator API is running...');
});

// Main calculate endpoint
app.post('/calculate', (req, res) => {
  const { num1, num2, operation } = req.body;

  if (num1 === undefined || num2 === undefined || !operation) {
    return res.status(400).json({ error: 'Missing parameters' });
  }

  let result;

  switch (operation) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      if (num2 === 0) {
        return res.json({ error: 'Division by zero not allowed' });
      }
      result = num1 / num2;
      break;
    default:
      return res.status(400).json({ error: 'Invalid operation' });
  }

  res.json({ result });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

// Legacy calculator routes (kept for compatibility)

app.post('/add', (req, res) => {
  const { a, b } = req.body;
  res.json({ result: a + b });
});

app.post('/subtract', (req, res) => {
  const { a, b } = req.body;
  res.json({ result: a - b });
});

app.post('/multiply', (req, res) => {
  const { a, b } = req.body;
  res.json({ result: a * b });
});

app.post('/divide', (req, res) => {
  const { a, b } = req.body;
  if (b === 0) {
    return res.json({ error: "Division by zero not allowed" });
  }
  res.json({ result: a / b });
});

app.post('/power', (req, res) => {
  const { a, b } = req.body;
  res.json({ result: Math.pow(a, b) });
});

app.post('/sqrt', (req, res) => {
  const { a } = req.body;
  if (a < 0) {
    return res.json({ error: "Cannot take square root of negative number" });
  }
  res.json({ result: Math.sqrt(a) });
});
