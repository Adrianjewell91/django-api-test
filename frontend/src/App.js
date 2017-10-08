import React, { Component } from 'react';
import logo from './logo.svg';
import axios from "axios";

import './App.css';

class App extends Component {

  makeGet(ev) {
    ev.preventDefault();
    axios.get('http://127.0.0.1:8000/snippets/1')
    .then(res => {
      console.log(res.data)
    });
  }

  makePost(ev) {
    ev.preventDefault();
    axios.post('http://127.0.0.1:8000/snippets/', {
      owner: "guest",
      code: "Love me my love",
      title: "Not code"
    })
    .then(res => {
      console.log(res.data)
    });
  }


  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Translate Overflow</h1>
        </header>
        <p className="App-intro">
          <button type="button" onClick={this.makeGet}>Click Here to make a GET Request.</button>
          <button type="button" onClick={this.makePost}>Click Here to make a POST Request.</button>
        </p>
      </div>
    );
  }

}

export default App;
