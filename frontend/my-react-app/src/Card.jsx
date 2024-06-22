import RestroPic from './assets/Burger.jpg'

function Card(){

    return(
        <div className="card">
            <img className="card-image" src="https://th.bing.com/th/id/OIP.0PAeTFUpPT5I4Z9lEl7RWwHaE7?rs=1&pid=ImgDetMain" alt="product"></img>
            <h2 className='card-title'>Product</h2>
            <p className='card-text'>This is a product</p>
        </div>
    );


}
export default Card