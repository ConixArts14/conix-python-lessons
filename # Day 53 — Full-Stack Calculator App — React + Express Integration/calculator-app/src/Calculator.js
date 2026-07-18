import './Calculator.css';

import React, { useState } from 'react';

function Calculator() {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [result, setResult] = useState('');

  const calculate = async (operation) => {
    const response = await fetch(`http://localhost:5000/${operation}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ a: Number(a), b: Number(b) })
    });
    const data = await response.json();
    setResult(data.result || data.error);
  };

return (
  <div className="calculator">
    <h2>Calculator</h2>
    <input type="number" value={a} onChange={e => setA(e.target.value)} placeholder="First number" />
    <input type="number" value={b} onChange={e => setB(e.target.value)} placeholder="Second number" />
    <div>
      <button onClick={() => calculate('add')}>Add</button>
      <button onClick={() => calculate('subtract')}>Subtract</button>
      <button onClick={() => calculate('multiply')}>Multiply</button>
      <button onClick={() => calculate('divide')}>Divide</button>
      <button onClick={() => calculate('power')}>Power</button>
      <button onClick={() => calculate('sqrt')}>Square Root</button>
    </div>
    <h3>Result: {result}</h3>
  </div>
);
}

export default Calculator;
