import React from 'react';
import ProductList from './ProductList';
import ProductDetail from './ProductDetail';
import UserSignUp from './UserSignUp';
import userLogin from './userLogin';
import { Router, Route, Switch } from 'react-router-dom';
import Header from './Header';
import history from '../history';

class App extends React.Component {
  render(){
      return (
          <div className="container-fluid">
            <Router history={history}>
              <div>
              <Header/>
              <Switch>
                <Route path="/signup/" exact component={UserSignUp}/>
                <Route path="/login/" exact component={userLogin}/>
                <Route path="/" exact component={ProductList}/>
                <Route path="/products/:id" exact component={ProductDetail}/>
              
              </Switch>
              </div>
            </Router>
          </div>
      );
  }
}

export default App;