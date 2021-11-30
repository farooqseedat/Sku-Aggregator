import React from 'react';
import { connect } from 'react-redux';
import { 
  fetchProduct,
  fetchAvailableSkus,
  selectSize,
  selectImage
} from '../actions';


class ProductDetail extends React.Component {
  componentDidMount()
  {
    this.props.fetchProduct(this.props.match.params.id);
    console.log("mount")
  }
  componentWillUnmount()
  {
    this.props.selectImage(null);
    console.log("unmount")
  }
  renderCategory(categories)
  {
    if(! categories)
      return null;
    return categories.map((category)=>{
      return(
      <React.Fragment key={category}>
        <a className="section" href="#">{category}</a>
        <div className="divider"> / </div>
      </React.Fragment>
      );
    })
  }

  renderPrice(product) {
    const price = parseFloat(product.price/100).toFixed(2);
    return(
      <div>{price} {product.currency}</div>
    )
  }
  renderDescription(descriptions) {
    if(!descriptions)
      return null;
    return descriptions.map((description)=>{
      return(<p key={description}>{description}</p>);
    })
  }
  onImageSelect(image_url)
  {
    this.props.selectImage(image_url);
  }
  renderThumbs(images)
  {
    if(!images)
      return null;
    return images.map((image)=>{
      return <img onClick={()=>this.onImageSelect(image)}key={image} src={image} alt="product"/>;
    })
  }
  
  onSizeSelect(size){
    const { selectSize, product } = this.props; 
    selectSize(size);
    const availableSkus = product.skus.filter((sku)=>sku.size===size);
    this.props.fetchAvailableSkus(availableSkus);
  }

  renderSizes(sizes,selected){
    return sizes.map((size)=>{
      return (
        <button 
          key={size}
          className={size===selected?'ui button primary':''} 
          onClick={()=>this.onSizeSelect(size)}>{size}
        </button>
      );
    })
  }
  renderVariants(){
    const {availableSkus}=this.props;
    if(!this.props.availableSkus)
      return null;
    return availableSkus.map((sku)=>{
      if(sku.color)
        return <button>{sku.color}</button>;
      else return null;
    });
  }
  renderSkus(skus){
    if(!skus)return null;
    
    const uniqueSizes = [...new Set(skus.map(sku=>sku.size))]
    return (<div>
      {this.renderSizes(uniqueSizes,this.props.selectedSize)}
      <div className="content">
        {this.renderVariants()}
      </div>
    </div>)

    
  }
  render(){
    const {product} = this.props;
    if(!product)
      return null;

    return (
      <div className="">
        <div className="ui breadcrumb">
        {this.renderCategory(product.category)}
        </div>
        <div className="ui segment">
        <div className="ui two column very relaxed grid">
          <div className="column">
            <img src={this.props.selectedImage?this.props.selectedImage:product.image_urls}
            style={{width:'100%',height:'500px' }}
            alt={product.name}
            />
            <div className="ui segment">
            <div className="ui small images">
              {this.renderThumbs(product.image_urls)}
            </div>
            </div>
          </div>
          <div className="column">
            <div className="ui medium header">
            {product.name}
            </div>
            <div className="ui large header">
            {this.renderPrice(product)}
            </div>
            <div className="ui small header">
              Description
            </div>
            {this.renderDescription(product.description)}
            <div>
              {this.renderSkus(product.skus)}
            </div>
          </div>          
        </div>
        
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { productDetail } = state.entities;
  return {
    product: productDetail.detail,
    availableSkus: productDetail.availableSkus,
    selectedSize: productDetail.selectedSize,
    selectedImage: productDetail.selectedImage,
  };
}

export default connect(
  mapStateToProps,
  {fetchProduct,fetchAvailableSkus, selectSize, selectImage})
  (ProductDetail);