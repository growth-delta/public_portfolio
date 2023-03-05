import React from 'react'
import { Navbar, Nav, Container, Row, Col } from 'react-bootstrap';
import logo from '../logo.png';
import Brand from './Brand.js'
import { LinkContainer } from 'react-router-bootstrap';

function Header() {
  return (
    <header>
      <div className='bg-warning'>
        <Row>
          <Col className='text-center py-3'>
            <h5>
              <i className="fa-solid fa-truck-fast"></i> FREE SHIPPING <i className="fa-solid fa-truck-fast"></i> OVER <i className="fa-solid fa-dollar-sign"></i><b>50</b>
            </h5>
          </Col>
        </Row>
      </div>
      <Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
        <Container>
          <LinkContainer to='/'>
            <Navbar.Brand>
              <h4><Brand/></h4>
            </Navbar.Brand>
          </LinkContainer>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav className="me-auto my-2 my-lg-0" style={{ maxHeight: '100px' }} navbarScroll>
            <LinkContainer to='/login'>
              <Nav.Link href="/login"><i className="fa-regular fa-user"></i> Login</Nav.Link>
            </LinkContainer>
            <LinkContainer to='/cart'>
              <Nav.Link href="/cart"><i className="fa-solid fa-cart-shopping"></i> Cart</Nav.Link>
            </LinkContainer>
            </Nav>
            <LinkContainer to='/'>
              <Navbar.Brand href="/">
                <img src={logo} width="45" className="d-inline-block align-top" alt="Logo"/>
              </Navbar.Brand>
            </LinkContainer>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header

