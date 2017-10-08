import React, { Component } from 'react';
import logo from './logo.svg';
import axios from "axios";

import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Translate Overflow</h1>
        </header>
        <p className="App-intro">
          <button type="button" onClick={this.makeGet}>Click Here to make a GET Request.</button>
        </p>
      </div>
    );
  }

  makeGet(ev) {
    ev.preventDefault();
    axios.get('/snippets')
         .then(res => {
            console.log(res.data)
         })
  }
}

export default App;
