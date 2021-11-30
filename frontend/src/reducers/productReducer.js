import {
  FETCH_PRODUCT, FETCH_PRODUCTS,
  FETCH_SKUS, SELECT_IMAGE,
  SELECT_SIZE
 } from '../actions/actionTypes';

const initialState = {
  products:[],
  productDetail:{
    detail:{},
    availableSkus:null,
    selectedImage:null,
    selectedSize:null
  }
}

export const productReducer = (state=initialState, action) => {
  const productDetail = state.productDetail;
  switch(action.type) {
    case FETCH_PRODUCTS:
      return {...state,products:action.payload["results"]};

    case FETCH_PRODUCT:
      productDetail["detail"] = action.payload;
      return {...state, productDetail};

    case SELECT_SIZE:
      productDetail["selectedSize"] = action.payload;
      return {...state, productDetail};

    case FETCH_SKUS:
      productDetail["availableSkus"] = action.payload;
      return {...state, productDetail};

    case SELECT_IMAGE:
      productDetail["selectedImage"] = action.payload;
      return {...state, productDetail};
      
    default:
      return state;
  }
}

export const productsPagesReducer = (state={}, action) => {
  switch(action.type) {
    case 'FETCH_PRODUCTS':
      return action.payload;
    default:
      return state;
  }
}
