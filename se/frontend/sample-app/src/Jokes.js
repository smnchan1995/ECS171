import React, {Component} from 'react';
import './Main.css';

class Jokes extends Component {
	render() {
		return(
		<div className="App">
			<h2> Your Recommended Jokes </h2>
			<p>
			Base on your data, the following jokes from our database have been recommended to you.
			</p>
		</div>
		);
	}

}

export default Jokes;