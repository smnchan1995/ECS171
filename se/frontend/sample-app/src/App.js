import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
	<div>
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">eComedy</h1>
		  <h2>#1 Predictor Site for Users Seeking Jokes</h2>
        </header>
        <p className="App-intro">
          Enter your preferred joke genre, age, and major!
        </p>
		<form>
		  <label> Genre: <input type="text" name="genre" value="" /> </label>
		  <br />
		  <label> Age: <input type="text" name="age" value="" /> </label>
		  <br />
		  <label> Major: <input type="text" name="major" value="" /> </label>
		  <br />
		  <input type="submit" value="Submit" />
		</form>
	  </div>
	  <div className="bottom">
		<h3 className="bottom-align"> This application was built using React! </h3>
		<img src={logo} className="App-logo" alt="logo" />
      </div>
	</div>
    );
  }
}

export default App;
