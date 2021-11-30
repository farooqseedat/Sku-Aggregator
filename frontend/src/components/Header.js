import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

import { logOut } from '../actions/index';

class Header extends React.Component {
  renderLoginButton = () =>{
    const buttonText = this.props.isSignedIn? "Sign Out":"Sign In" ;
    return(
      <Link to={this.props.isSignedIn?'':'/login'}  
        className="ui red button"
        onClick={()=>this.onLogOut()}
      >
          {buttonText}
        </Link>
    );
  } 
  onLogOut = () => {
    this.props.logOut();
  }

  render(){ 
    const { isSignedIn ,userName } = this.props;
    const profileButton = <Link to="/profile" className="ui primary button">{userName}</Link>
    return (
      <div className="ui secondary pointing menu">
        <Link to="/" className="item">
          Products
        </Link>
        
        <div className="right menu">
          {isSignedIn?profileButton:null}
          {this.renderLoginButton()}
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isSignedIn: state.logInStatus? state.logInStatus.isSignedIn: false,
    userName: state.logInStatus? state.logInStatus.userName: null
  }
}
export default connect(mapStateToProps,{logOut})(Header);
