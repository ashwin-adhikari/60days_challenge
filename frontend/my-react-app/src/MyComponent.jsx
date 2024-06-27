import React, {useState} from "react"

function Component(){
    let[name, setName] = useState();//returns 2 value name and a setter function
    const[quantity, setQuantity] = useState(0);

    const updateName = () => {
        setName("Pizza");
    }
    const incrementQuantity = () => {
        setQuantity(quantity + 1);
    }

    return(<div>


    <p>Quantity: {quantity}</p>
    <button onClick={incrementQuantity}>Add to Cart</button>
    
   

    </div> );

}
export default Component