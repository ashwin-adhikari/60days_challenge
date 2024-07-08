import React, { useState } from "react"

export default function MyComponent() {
    //  let[name, setName] = useState();//returns 2 value name and a setter function
    const [quantity, setQuantity] = useState(0);
    const [item, setItem] = useState('');
    const [payment, setPayment] = useState();

    function handleItem(e){
        setItem(e.target.value)
        

    }
    const incrementQuantity = () => {
        setQuantity(quantity + 1);//this is a default function
        setQuantity(q => q + 1);//this is a updater function

    }
    function handlePayment(e){
        setPayment(e.target.value);
    }


    return (
        <>
            <div className="order">
                <div className="add-item">
                <input value={item} onChange={handleItem} className="order-input"/>
                <button onChange={handleItem} className="add-to-cart">Add Item</button>
                <p>{item} is added to your order</p>
                </div>

                <div className="quantity">
                <p>Quantity: {quantity}</p>
                <button onClick={incrementQuantity}className="inc-quantity-button">Add to Cart</button> 
                </div>

                <div className="payment">
                <select value={payment} onChange={handlePayment} className="pay-option">
                    <option value=" ">Select an option</option>
                    <option value="Fonepay">Fonepay</option>
                    <option value="Online Banking">Online Banking</option>
                    <option value="Cash">Cash</option>
                </select>
                <p>Payment: {payment}</p>
                </div>


            </div> 
        </>
    );
}
