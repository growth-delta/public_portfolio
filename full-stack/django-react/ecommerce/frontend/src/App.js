import { Container } from 'react-bootstrap';

import Header from './components/Header';
import Footer from './components/Footer';
import Brand from './components/Brand';

function App() {
  return (
    <div>
      <Header />
      <main className='py-5'>
        <Container>
          <h1>WELCOME to <Brand/></h1>
        </Container>
      </main>
      <Footer />
    </div>
  );
}

export default App;
