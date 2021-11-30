import products from '../apis/products';
import users from '../apis/users';
import history from '../history';
import {
  FETCH_PRODUCT, FETCH_PRODUCTS,
  FETCH_SKUS, SELECT_IMAGE,
  SELECT_SIZE, SIGN_UP_SUCCESS,
  SIGN_UP_FAILURE, LOGIN_FAILURE,
  LOGIN_SUCCESS, LOGOUT_SUCCESS
 } from './actionTypes';

export const fetchProducts = params => dispatch => {
  products.get( '/products/',{params}).then(
  response=>dispatch({ type: FETCH_PRODUCTS , payload: response.data}));
}

export const fetchProduct = id => dispatch => {
  products.get(`/products/${id}`).then(
  response => dispatch({ type: FETCH_PRODUCT, payload: response.data}));
}

export const fetchAvailableSkus = skus =>{
  return {type:FETCH_SKUS, payload:skus};
}

export const selectSize =(size)=>{
  return {type:SELECT_SIZE, payload:size};
}

export const selectImage = imageUrl => {
  return {type:SELECT_IMAGE,payload:imageUrl};
}

export const createAccount = formValues =>  dispatch =>{
  users.post('/users/',{...formValues}).then( response=>{
    if(response.status===201)
    {
      dispatch({type:SIGN_UP_SUCCESS, payload:"Account Created Successfully"})
      history.push('/login');
    }
  }).catch(error=>dispatch({type:SIGN_UP_FAILURE, payload:error.response.data}));
}

export const login = formValues => dispatch =>{
  users.post('/users/login/',{...formValues})
  .then(response=>{
    if(response.status===200)
    {
      dispatch({type:LOGIN_SUCCESS, payload:response.data})
      history.push('/');
    } 
  }).catch(error=> {
    console.log(error)
    // dispatch({type:LOGIN_FAILURE, payload:error.response.data})
  });
}

export const logOut = () => {
  return ({type:LOGOUT_SUCCESS, payload:""})
}