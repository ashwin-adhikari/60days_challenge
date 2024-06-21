

function Items(){
    const item1 = "Burger";
    const item2 = "Pizza";

    return(
      <ul>
        <li>Fast Food</li>
        <li>{item1}</li>
        <li>{item2.toUpperCase()}</li>
      </ul>
    );
}

export default Items