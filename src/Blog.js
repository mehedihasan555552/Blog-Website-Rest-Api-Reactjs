import React, {useState, useEffect,Component} from 'react'
import './blog.css';
import axios from 'axios';



export default class Blog extends React.Component{

  state = {
    persons : []
  }

  componentDidMount(){
    axios.get(`http://127.0.0.1:8000/api/blogs/`)
    .then(res => {
      const persons = res.data;
      this.setState({persons})
    })
  }

  


  render(){
    return(
     

      <div>
    {this.state.persons.map(person => 
      
      
      <div className=" card1">
<div class="row no-gutters">
  <div class="col-md-4">
   
    <img class="card-img" src={person.image}/>
    
   
  </div>
  <div class="col-md-8">
    <div class="card-body">
    <h5 class="card-title"> {person.title}</h5>
      <p class="card-text"> {person.content}</p>
    <p class="card-text"><small class="text-muted">{person.created_at}</small></p>
    </div>
  </div>
</div>
</div>
      
      
      )}


</div>
     

      

    )
  }
}


