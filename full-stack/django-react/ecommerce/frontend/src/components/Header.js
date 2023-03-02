import React from 'react'
import { Navbar, Nav, Container, Row } from 'react-bootstrap';
import logo from '../resources/logo.png';

function Header() {
  return (
    <header>
      <Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>

        <Container>
          <Navbar.Brand href="/">
            <img
            src={logo}
            width="45"
            height="45"
            className="d-inline-block align-top"
            alt="Big Commerce logo"
            />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="me-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll
            >
              <Nav.Link href="/login"> Login</Nav.Link>
              <Nav.Link href="/cart"><i class="fa-solid fa-cart-shopping"></i> Cart</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>

      </Navbar>
    </header>
  )
}

export default Header

