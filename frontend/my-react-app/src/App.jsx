import Header from "./Header.jsx"
import Footer from "./Footer.jsx"
import Items from "./Items.jsx";
import Card from "./Card.jsx"; 
import Button from "./Button.jsx";
import Table from "./Table.jsx"; 
import UserGreeting from "./UserGreeting.jsx";
import List from "./List.jsx";
import MyComponent from "./MyComponent.jsx"
import ColorPicker from "./ColorPicker.jsx";
import ToDoList from "./ToDoList.jsx";
import ComponentA from "./ComponentA.jsx";
import Weather from "./FetchData.jsx";
function App() {

  return(
    <>
      {/* <Header/>
      <UserGreeting isLoggedIn={true} username="Ash"/>
      <Items/> */}
      {/* <MyComponent/> */}

      {/* <List/>
      <Card/>
      <Table capacity={4} isOccupied={true} location="north" />
      <Table capacity={2} isOccupied={false} location="South" />
      <Button/>
      <Footer/> */}
      {/* <ColorPicker/> */}
      {/* <ToDoList/> */}
      {/* <ComponentA/> */}
      <Weather/>
    </>


  );
 
}

export default App
