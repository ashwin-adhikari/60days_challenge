import Header from "./Header.jsx"
import Footer from "./Footer.jsx"
import Items from "./Items.jsx";
import Card from "./Card.jsx"; 
import Button from "./Button.jsx";
import Table from "./Table.jsx"; 
import UserGreeting from "./UserGreeting.jsx";
function App() {

  return(
    <>
      <Header/>
      <UserGreeting isLoggedIn={true} username="Ash"/>
      <Items/>
      <Card/>
      <Table capacity={4} isOccupied={true} location="north" />
      <Table capacity={2} isOccupied={false} location="South" />
      <Button/>
      <Footer/>
    </>


  );
 
}

export default App
