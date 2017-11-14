import React, {Component} from 'react';
import {
  Table,
  TableBody,
  TableHeader,
  TableHeaderColumn,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import './Main.css';

class About extends Component {
	render() {
	  return (
	  <div className="App">
	    <h2> About the Blue Team </h2>
		
		<p>
		This application was brought to you by:
		</p>
		
		<Table>
		<TableHeader displaySelectAll={false} >
		  <TableRow>
			<TableHeaderColumn>Project Management</TableHeaderColumn>
			<TableHeaderColumn>Software Engineering</TableHeaderColumn>
			<TableHeaderColumn>Machine Learning and Algorithms</TableHeaderColumn>
			<TableHeaderColumn>UI/UX and Visualization</TableHeaderColumn>
			<TableHeaderColumn>Quality Assurance</TableHeaderColumn>		
		  </TableRow>
		</TableHeader>
		<TableBody displayRowCheckbox={false}>
		  <TableRow>
			<TableRowColumn style={{paddingLeft: 85}}>
				<li>Naomi Okiddy</li>
				<li>Rishi Subramanian</li>
				<li>Hyoung-yoon Kim</li>
				<li>Dillon Carlos</li>
				<li>Aidan Daniels-Soles</li>		
			</TableRowColumn>
			<TableRowColumn style={{paddingLeft: 80}}>
				<li>Daniel Perano</li>
				<li>Andrew van Tonningen</li>
				<li>Domnall Hegarty </li>
				<li>Michelle Tang</li>
				<li>Eric Ai</li>
				<li>Hasith Rajakarunanayake</li>
				<li>Simon Chan</li>
				<li>Edward Xu</li>
				<li>Faiyz Rahman</li>
				<li>Daniel Wang</li>
				<li>Jennifer Wong</li>		
			</TableRowColumn>
			<TableRowColumn style={{paddingLeft: 90}}>
				<li>Chirag Kashyap</li>
				<li>Jonathan Ngo</li>
				<li>Kush Patel</li>
				<li>Dominic Yang</li>
				<li>Sarah Dang</li>
				<li>Andy Tran</li>
				<li>Christine Tech</li>
				<li>Yash Bhartia</li>
				<li>Aakaash Kapoor </li>
				<li>Isaac Kim</li>
				<li>Haofei Chen</li>
				<li>Ehsan Fanaian</li>		
			</TableRowColumn>
			<TableRowColumn style={{paddingLeft: 60}}>
				<li>Tsz Chi Leung</li>
				<li>Dat Nguyen</li>
				<li>hao lin</li>
				<li>Gunther Schuler</li>
				<li>Jian Yuan</li>
				<li>Yiru Sun</li>
				<li>Gabriel Yin</li>		
			</TableRowColumn>
			<TableRowColumn style={{paddingLeft: 40}}>
				<li>Nathan Telles</li>
				<li>Andrei Blebea</li>
				<li>Alvis Leung</li>		
			</TableRowColumn>
		  </TableRow>
		</TableBody>
	  </Table>
		
	  </div>
	  );
	}
}

export default About;