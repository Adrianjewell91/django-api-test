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
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          I just edited this thing.
          <button type="button" onClick={this.makeGet}>Click Here to make a GET Request.</button>
        </p>
      </div>
    );
  }

  makeGet(ev) {
    ev.preventDefault();
    axios.get('/snippets.json')
         .then(res => {
            console.log(res)
         })
        //  .then(response => {
        //    console.log(JSON.stringify(response));
        //  });
  }
}

export default App;
