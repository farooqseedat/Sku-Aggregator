import CryptoJS from 'crypto-js';
import {
  SIGN_UP_SUCCESS,SIGN_UP_FAILURE, 
  LOGIN_FAILURE, LOGIN_SUCCESS,
  LOGOUT_SUCCESS
 } from '../actions/actionTypes';
export const Key = 'ab^2fs4sv*avashd';

export const signUpReducer=(state=null, action) => {
  switch(action.type) {
    case SIGN_UP_SUCCESS:
      return {
        accountCreated:true,
        message:action.payload
      }
    case SIGN_UP_FAILURE:
      return {
        accountCreated:false,
        message:action.payload
      }
    default:
      return state;
  }
}

export const loginReducer = (state=null, action) => {
  switch (action.type) {
    case LOGIN_SUCCESS:
      localStorage.setItem("userRefreshToken", CryptoJS.AES.encrypt(action.payload.refresh, Key));
      localStorage.setItem("userAccessToken", CryptoJS.AES.encrypt(action.payload.access, Key));
      return { 
        isSignedIn:true,
        userName: action.payload.name 
      }
      case LOGIN_FAILURE:
      case LOGOUT_SUCCESS:
      return { 
        isSignedIn:false,
        userName: null 
      }
      default:
        return state;
  }
}
