import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card } from 'react-bootstrap'
import Rating from '../components/Rating'
import Loader from '../components/Loader'
import Message from '../components/Message'
import { listProductDetails } from '../actions/productActions'
// import axios from 'axios'

function ProductScreen() {
    // const[product, setProduct]  = useState([])
    // const { id } = useParams();
  
    // useEffect(() => {
    //   async function fetchProduct(){
    //     const { data } = await axios.get(`/api/products/${id}`)
    //     setProduct(data)
    //   }
    //   fetchProduct()
    // }, [])
    // // const { id } = useParams();
    // // const product = products.find((p) => p._id === id);

    const { id } = useParams();
    const dispatch = useDispatch();
    const productDetails = useSelector(state => state.productDetails);
    const { loading, error, product } = productDetails;
  
    useEffect(() => {
        dispatch(listProductDetails(id))
    }, [dispatch, id]);

    return (
        <div>
            <h1 className='text-center'>{product.name}</h1>
            <Link to='/'><i className='fa-solid fa-circle-left text-secondary fa-3x'></i></Link>
            <br></br><br></br>
            {loading ? <Loader />: 
            error ? <Message variant='danger'>{error}</Message>:
            (
                <Row>
                    <Col md={6}>
                        <Image src={product.image} alt={product.name} fluid />
                    </Col>
                    <Col md={3}>
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <b>{product.name}</b>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Rating value={product.rating} text={`${product.numReviews} Reviews`} color={'#f8e825'} />
                            </ListGroup.Item>
                            <ListGroup.Item>
                                Price: <i className="fa-solid fa-dollar-sign"></i> {product.price}
                            </ListGroup.Item>
                            <ListGroup.Item>
                                {product.description}
                            </ListGroup.Item>
                        </ListGroup>
                    </Col>
                    <Col md={3}>
                        <Card>
                            <ListGroup variant='flush'>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Price: </Col>
                                        <Col><strong>${product.price}</strong></Col>
                                    </Row>
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>Status: </Col>
                                        <Col><strong>{product.countInStock > 0 ? 'In Stock' : 'Out of Stock'}</strong></Col>
                                    </Row>
                                    <br></br>
                                    <Row>
                                        <Button className='btn btn-success btn-block' disabled={product.countInStock === 0} type='button'>Add to Cart</Button>
                                    </Row>
                                </ListGroup.Item> 
                            </ListGroup>
                        </Card>  
                    </Col>
                </Row>
            )
            }
        </div>
    )
};

export default ProductScreen;