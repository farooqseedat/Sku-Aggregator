import React from 'react'
import { connect } from 'react-redux';
import  { Field, reduxForm } from 'redux-form'
import {createAccount} from '../actions/index';

class SignUpForm extends React.Component {
  
  renderError({ error, touched }) {
    if (touched && error) {
      return (
        <div className="ui error message">
          <div className="header">{error}</div>
        </div>
      );
    }
  }
  renderInput = ({ input, type, label, meta }) => {
    const className = `field ${meta.error && meta.touched ? 'error' : ''}`;
    return (
      <div className={className}>
        <label>{label}</label>
        <input {...input} type={type}autoComplete="on" />
        {this.renderError(meta)}
      </div>
    );
  };
  renderSignUpStatus(){
    const { signUpStatus } = this.props;
    if(!this.props.signUpStatus)
      return null;
    if(!signUpStatus.accountCreated)
      return(
        <div className="error">
          Error: 
          {Object.values(signUpStatus.message)}
        </div>
      )
  }

  onSubmit = formValues =>{
    this.props.createAccount(formValues);
  }
  render(){
    return (
      <div className="ui segment">
        {this.renderSignUpStatus}
      <form
        onSubmit={this.props.handleSubmit(this.onSubmit)}
        className="ui form error"
      >
        <div className="ui two column very relaxed grid">
          <div className="column">
            <div className="header">
              Address
            </div>
            <Field 
              name="profile.address"
              component={this.renderInput} 
              label="Address"/>
            <Field
              name="profile.zip"
              component={this.renderInput}
              label="Postal Code:"
            />
            <Field
              name="profile.city"
              component={this.renderInput}
              label="City:"
            />
            <Field
              name="profile.country"
              component={this.renderInput}
              label="Country"
            />
          </div>
          <div className="column">
            <div className="header">Basic-Info</div>
            <Field
              name="first_name"
              component={this.renderInput}
              label="First Name:*"
            />
            <Field
              name="last_name"
              component={this.renderInput}
              label="Last Name:*"
            />
            <Field
              name="email"
              component={this.renderInput}
              label="Email:*"
              type="email"
            />
            <Field
              name="profile.dob"
              component={this.renderInput}
              label="Date of Birth:*"
              type="date"
            />  

            <Field
              name="password"
              component={this.renderInput}
              label="Password:*"
              type="password"
            />
            <Field
              name="confirm_password"
              component={this.renderInput}
              label="Confirm Password:*"
              type="password"
            />
            <button className="ui button primary" style={{float:'right',flex:'right'}}>Sign Up</button>
          </div>
        </div>
      </form>
      <div style={{textAlign:"right",color:'red',marginTop:'10px'}}>
        <span>Fields with * are mandatory</span>
      </div>
        
      </div>
    );
  }
}

const validate = formValues => {
  const errors = {};
  const errorRequired = "This field is required";
  const errorLength = "Password is too short minimum is 6 characters";
  if (!formValues.first_name) {
    errors.first_name = errorRequired;
  }

  if (!formValues.last_name) {
    errors.last_name = errorRequired;
  }
  if (!formValues.email) {
    errors.email = errorRequired;
  }
  if (formValues.password &&formValues.password.length<6) {
    errors.password = errorLength;
  }
  if (formValues.confirm_password && formValues.confirm_password.length<6) {
    errors.confirm_password = errorLength;
  }
  if (
      formValues.password &&
      formValues.confirm_password &&
      formValues.confirm_password!==formValues.password
  )
  {
    errors.confirm_password="Password Must Match!";
  }

  return errors;
};


const SignUpPage = reduxForm({
  form: 'signUpForm',
  validate, 
})(SignUpForm);

const mapStateToProps = state => {
  return { signUpStatus: state.signUpStatus }
}
export default connect(mapStateToProps,{createAccount})(SignUpPage);