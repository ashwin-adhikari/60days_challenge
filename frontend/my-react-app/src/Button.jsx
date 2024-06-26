
function Button(){
    const styles = {
        backgroundColor: "hsl(200, 100%, 50%)",
        color: "aliceblue",
        padding: "10px 20px",
        borderRadius: "5px",
        border: "none",
        cursor: "pointer",
    }
    // const handleClick = () => console.log("Order Placed");//outputs the string in console
    // const handleClick = (e) => console.log(e);//outputs event that happened when clicking the button
    const handleClick = (e) => e.target.textContent = "Order Placed ✅";


    return(
        

        <button onClick={(e) => handleClick(e)} style={styles}>Order</button>
    );
}
export default Button