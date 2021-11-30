import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';
import { productReducer, productsPagesReducer } from './productReducer';
import { loginReducer, signUpReducer } from './userReducer';

export default combineReducers({
  entities: productReducer,
  paging: productsPagesReducer,
  form: formReducer,
  signUpStatus: signUpReducer,
  logInStatus: loginReducer,
})