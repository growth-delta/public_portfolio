import React from 'react'
import { Card } from 'react-bootstrap'
import Rating from './Rating'

function Product({ product }) {
  return (
    <Card className='my-3 p-3 rounded'>
        <Card.Body>

            <a href={`/product/${product._id}`}>
                <Card.Title as="div" className='link-dark'>
                    <strong>{product.name}</strong>
                </Card.Title>
            </a>
            
            <a href={`/product/${product._id}`}>
                <Card.Img src={product.image} height="175"/>
            </a>

            <Card.Text as="div">
                <div className='my-3'>
                    {/* {product.rating} /5 from {product.numReviews} reviews */}
                    <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'}/>
                </div>
            </Card.Text>

            <Card.Text as="h3">
                <div className='my-3'>
                    <i className="fa-solid fa-dollar-sign"></i>{product.price}
                </div>
            </Card.Text>

        </Card.Body>
    </Card>
  )
}

export default Product