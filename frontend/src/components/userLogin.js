import React from 'react';
import { Link } from 'react-router-dom';
import  { Field, reduxForm } from 'redux-form';
import { connect } from 'react-redux';
import { login } from '../actions/index';


class LoginForm extends React.Component{
  renderError({ error, touched }) {
    if (touched && error) {
      return (
        <div className="ui error message">
          <div className="header">{error}</div>
        </div>
      );
    }
  }
  renderInput = ({ input, type="text", label, meta }) => {
    const className = `field ${meta.error && meta.touched ? 'error' : ''}`;
    return (
      <div className={className}>
        <label>{label}</label>
        <input {...input} type={type} autoComplete="on" />
        {this.renderError(meta)}
      </div>
    );
  };
  renderSignUpStatus(){
    const { signUpStatus } = this.props;
    if(!signUpStatus)
      return null;
    return(
      <div >
        {signUpStatus.message}
      </div>
    );
  }
  onSubmit = (formValues) => {
    this.props.login(formValues);
  }
  render(){
    return(
      <div >
        {this.renderSignUpStatus()}
        <div style={{width:'50%',height:'50%',alignContent:'centre',}}>
          <form 
            className="ui error form"
            onSubmit={this.props.handleSubmit(this.onSubmit)}
          >
            <Field 
              name="email"
              label="Email"
              component={this.renderInput}
            />
            <Field 
              name="password"
              label="Password"
              type="password"
              component={this.renderInput}
            />
            <button className="ui button" >Login</button>
            <Link className="ui button" to="/signup/">Sign up</Link>
          </form>
        </div>

      </div>
    );
  }
}

const validate = formValues => {
  const errors = {};
  const errorRequired = "This field is required";
  if (!formValues.email) {
    errors.email = errorRequired;
  }

  if (!formValues.password) {
    errors.password = errorRequired;

  }
  return errors;
}

const mapStateToProps = state => {
  return {signUpStatus:state.signUpStatus}
}

const LoginPage = reduxForm({
  form: 'loginForm',
  validate, 
})(LoginForm);

export default connect(mapStateToProps,{login})(LoginPage);