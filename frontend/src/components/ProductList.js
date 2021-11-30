import React from 'react';
import { Link } from 'react-router-dom';
import { Field, reduxForm } from 'redux-form';
import { connect } from 'react-redux';
import { fetchProducts } from '../actions';
import './ProductList.css';
import ProductCard from './ProductCard';


class ProductList extends React.Component {
  componentDidMount() {
    this.props.fetchProducts();
  }

  renderList() {
    const { products } = this.props;
    if (!products)
      return null;
    return this.props.products.map((product) => {
      return (
        <div key={product.id} className="">
          <ProductCard product={product} link={`/products/${product.id}`} />
        </div>
      );
    });
  }

  onClickNextPage(url) {
    const offset = (new URL(url)).searchParams.get('offset');
    this.props.fetchProducts({ offset });
  }

  onSearch = (formValues) => {
    this.props.fetchProducts(formValues);
  }

  renderInput = ({ input, type, id, className = "", placeholder = "", style }) => {
    return (
      <input {...input}
        key={id} type={type}
        className={className}
        placeholder={placeholder}
        style={style}
      />
    );
  };

  renderFilter() {
    return (
      <div className="container">
        <div className="row" />
        <div className="row" />
        <h4 className="title">Price Range</h4>
        <div className="row">
          <div className="col">
            <Field
              name="min_price"
              component={this.renderInput}
              type="number"
              placeholder="Min"
              style={{ width: "80px", height: "30px" }}
            />
            <div style={{ lineHeight: "30px", display: "inline" }}>-</div>
            <Field
              name="max_price"
              component={this.renderInput}
              type="number"
              placeholder="Max"
              style={{ width: "80px", height: "30px" }}
            />
          </div>
        </div>
        <h4 className="title">Gender</h4>
        <div className="row">
          <div className="col">
            <label className="">Men</label>
            <Field
              name="gender"
              component={this.renderInput}
              type="radio"
              value='Men'
            />
          </div>
          <div className="col">
            <label>Women</label>
            <Field
              name="gender"
              component={this.renderInput}
              type="radio"
              value='Women'
            />
          </div>
          <div className="col">
            <label>All</label>
            <Field
              name="gender"
              component={this.renderInput}
              type="radio"
              value=''
            />
          </div>
        </div>
        <div className="row" />
        <h4 className="title">Categories</h4>
        <div className="row">
          <div className="col">
            <label className="">Accessories</label>
            <Field
              name="categories"
              component={this.renderInput}
              type="radio"
              value="Accessories"
            />
          </div>
          <div className="col">
            <label>Footwear</label>
            <Field
              name="categories"
              component={this.renderInput}
              type="radio"
              value="Footwear"
            />
          </div>
          <div className="col">
            <label>All</label>
            <Field
              name="categories"
              component={this.renderInput}
              type="radio"
              value=""
            />
          </div>
        </div>
      </div>
    );
  }

  render() {
    return (
      <div className="container-fluid">
        <h3>{this.props.noOfProducts} results found</h3>

        <div className="row">
          <div className="container col-2">
            <form className="ui form" onSubmit={this.props.handleSubmit(this.onSearch)} >
              <div className="ui icon input">
                <Field name="search" component={this.renderInput} />
                <button className="ui red button" >Search</button>
              </div>
              {this.renderFilter()}
            </form>
          </div>
          <div className="container col-9">
            <div className="card-deck">
              {this.renderList()}
            </div>
          </div>
        </div>

        <ul className="pagination justify-content-center" >
          <li className={`page-item ${!this.props.prevPage ? 'disabled' : ''}`}>
            <Link className="page-link"
              onClick={() => this.onClickNextPage(this.props.prevPage)}
              to="/" >
              Previous
              </Link>
          </li>
          <li className={`page-item ${!this.props.nextPage ? 'disabled' : ''}`}>
            <Link className="page-link"
              onClick={() => this.onClickNextPage(this.props.nextPage)}
              to="/" >
              Next
              </Link>
          </li>
        </ul>
      </div>
    );

  }

}

const mapStateToProps = (state) => {
  return {
    products: state.entities.products,
    nextPage: state.paging.next,
    prevPage: state.paging.previous,
    noOfProducts: state.paging.count
  };
}
const Products = reduxForm({ form: 'searchForm' })(ProductList);

export default connect(mapStateToProps, { fetchProducts })(Products);