// import { createStore, combineReducers, applyMiddleware } from 'redux'
// import { configureStore } from '@reduxjs/toolkit';
// import thunk from 'redux-thunk'
// import { composeWithDevTools } from 'redux-devtools-extension'

// const reducer = combineReducers({})

// const initialState = {}

// const middleware = [thunk]

// const store = configureStore(reducer, initialState, composeWithDevTools(applyMiddleware(...middleware)))

// export default store
import { combineReducers } from 'redux'
import { configureStore } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
// import { composeWithDevTools } from 'redux-devtools-extension';
import { productListReducer, productDetailsReducer } from './reducers/productReducers';

const reducers = combineReducers({
  productList: productListReducer,
  productDetails: productDetailsReducer,
});

const initialState = {};

const middleware = [thunk];

const store = configureStore({
  reducer: reducers, // Add your reducers here
  preloadedState: initialState,
  middleware: middleware,
  devTools: true, // Enable Redux DevTools
});

export default store;

