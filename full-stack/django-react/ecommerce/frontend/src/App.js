import { Container } from 'react-bootstrap';

import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div>
      <Header />
      <main className='py-5'>
        <Container>
          <h1>WELCOME</h1>
        </Container>
      </main>
      <Footer />
    </div>
  );
}

export default App;