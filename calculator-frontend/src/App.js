import { useState } from 'react';
import './App.css';

function App() {
  const [display, setDisplay] = useState('0');
  const [previousValue, setPreviousValue] = useState(null);
  const [operation, setOperation] = useState(null);
  const [newNumber, setNewNumber] = useState(true);

  const handleNumber = (num) => {
    if (newNumber) {
      setDisplay(String(num));
      setNewNumber(false);
    } else {
      setDisplay(prevDisplay => prevDisplay === '0' ? String(num) : prevDisplay + num);
    }
  };

  const handleOperation = async (op) => {
    const currentValue = parseFloat(display);

    if (previousValue === null) {
      setPreviousValue(currentValue);
      setDisplay(`${currentValue} ${op} `);
    } else if (operation) {
      try {
        const response = await fetch('http://localhost:5000/calculate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            num1: previousValue,
            num2: currentValue,
            operation: operation,
          }),
        });
        const data = await response.json();
        setPreviousValue(data.result);
        setDisplay(`${data.result} ${op} `);
      } catch (error) {
        setDisplay('Error');
        console.error(error);
      }
    }

    setOperation(op);
    setNewNumber(true);
  };

  const handleEquals = async () => {
    if (operation && previousValue !== null) {
      const currentValue = parseFloat(display.split(' ')[0] === '' ? display : display);
      const numToUse = isNaN(currentValue) ? parseFloat(display.split(' ').pop()) : currentValue;
      
      try {
        const response = await fetch('http://localhost:5000/calculate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            num1: previousValue,
            num2: numToUse,
            operation: operation,
          }),
        });
        const data = await response.json();
        setDisplay(String(data.result));
        setPreviousValue(null);
        setOperation(null);
        setNewNumber(true);
      } catch (error) {
        setDisplay('Error');
        console.error(error);
      }
    }
  };

  const handleClear = () => {
    setDisplay('0');
    setPreviousValue(null);
    setOperation(null);
    setNewNumber(true);
  };

  const handleDecimal = () => {
    if (newNumber) {
      setDisplay('0.');
      setNewNumber(false);
    } else if (!display.includes('.')) {
      setDisplay(prevDisplay => prevDisplay + '.');
    }
  };

  return (
    <div className="App">
      <div className="calculator">
        <h1>Calculator</h1>
        <div className="display">{display}</div>
        <div className="buttons">
          <button className="clear" onClick={handleClear}>C</button>
          <button onClick={() => handleOperation('/')}>/</button>
          <button onClick={() => handleOperation('*')}>×</button>
          <button onClick={() => handleOperation('-')}>−</button>

          <button onClick={() => handleNumber(7)}>7</button>
          <button onClick={() => handleNumber(8)}>8</button>
          <button onClick={() => handleNumber(9)}>9</button>
          <button onClick={() => handleOperation('+')}>+</button>

          <button onClick={() => handleNumber(4)}>4</button>
          <button onClick={() => handleNumber(5)}>5</button>
          <button onClick={() => handleNumber(6)}>6</button>
          <button className="empty"></button>

          <button onClick={() => handleNumber(1)}>1</button>
          <button onClick={() => handleNumber(2)}>2</button>
          <button onClick={() => handleNumber(3)}>3</button>
          <button className="empty"></button>

          <button className="zero" onClick={() => handleNumber(0)}>0</button>
          <button onClick={handleDecimal}>.</button>
          <button className="equals" onClick={handleEquals}>=</button>
        </div>
      </div>
    </div>
  );
}

export default App;
