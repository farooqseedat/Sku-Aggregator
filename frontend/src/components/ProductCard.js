import React from 'react';
import { Link } from 'react-router-dom';
import './ProductCard.css';

const renderProductCard = ({product,link}) =>{
  const onMouseEnter = (e, product) => {
    e.currentTarget.src = product.image_urls[1]?product.image_urls[1]:e.currentTarget.src
  }

  const onMouseOut = (e, product) => {
    e.currentTarget.src = product.image_urls[0]?product.image_urls[0]:e.currentTarget.src
  }

  return (
    <div className="card border-0" >
      <div id="card-img-div">
      <img className="card-img center" src={product.image_urls[0]}
        onMouseEnter={e=>onMouseEnter(e,product)}  
        onMouseOut={e=>onMouseOut(e,product)}
       alt="product" />
       </div>
      <div className="card-body" >
        <Link className="btn stretched-link" to={link}  style={{fontSize:"14px"}}>
            {product.name}
        </Link>
        <p>
          {product.price}
        </p>
      </div>
    </div>
  );
}

export default renderProductCard;