import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';
import {Route, NavLink, HashRouter} from 'react-router-dom';
import Home from './Home';
import Jokes from './Jokes';
import Data from './Data';
import About from './About';
import logo from './logo.svg';
import './Main.css';

class Main extends Component {
  render() {
	
    return (
	<HashRouter>
	<MuiThemeProvider>
	<div>
	  <AppBar title="ComAIdian" 
			  showMenuIconButton={false}
			  iconElementRight={
				  <div>
				    <NavLink to ="/">
						<FlatButton label="Home" /> 
					</NavLink>
					<NavLink to ="/jokes">
						<FlatButton label="Recommended Jokes" />
					</NavLink>
					<NavLink to ="/data">
						<FlatButton label="Data" />
					</NavLink>
					<NavLink to ="/about">					
						<FlatButton label="About Us" />
					</NavLink>
				  </div>
			  } />
	  <div>
		<Route exact path="/" component={Home}/>
        <Route path="/jokes" component={Jokes}/>
        <Route path="/data" component={Data}/>
		<Route path="/about" component={About}/>
	  </div>

	  <div className="bottom">
		<h3 className="bottom-align"> This application was built using React! </h3>
		<img src={logo} className="App-logo" alt="logo" />
      </div>
	</div>
	</MuiThemeProvider>
	</HashRouter>
    );
  }
}

export default Main;
