import { useState } from "react";

export default function Product() {


    const [selectedButton, setSelectedButton] = useState(null);
    
    function handleButtonClick(button) {
      setSelectedButton(button);
    }
      
  
    return (
        <>
            <div className="product-container">

                <div className="product-showcase">
                <div className="product-images">
                    <img src="banner1.png" />
                    <img src="banner2.png" />
                    <img src="banner3.png" />
                    {/* <img src="" /> */}
                </div>
                {/* all the images */}
                <div className="product-image_zoomin">
                    <img src="banner1.png" />
                </div>
                {/* main image div */}
                </div>

                <div className="product-box">
                    <div className="product-title">
                        <h1>Shirt</h1>
                    </div>
                    <div className="product-details">
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Natus, modi fugit! Debitis, ipsa, quo dolore quisquam illo nihil doloremque possimus harum deserunt ea sunt exercitationem atque voluptatem, a vero quia. Facilis rerum hic, amet quaerat perspiciatis corporis aut voluptas earum. Numquam suscipit explicabo corporis veritatis fuga illum quas magnam aut.
                    </div>
                    
                    <div className="purchase-details">

                        <div className="product-specification">
                            <table>
                                <tr>
                                    <td><b>Cloth: </b></td>
                                    <td>Cotton</td>
                                </tr>
                                <tr>
                                    <td><b>Sizes Available: </b></td>
                                    <td>S, M, L and XL</td>
                                </tr>
                            </table>
                        </div>


                        <div className="product-choice">
                            <div className="product-type">


                                <div className="product-size">
                                    <label htmlFor="type"><b>Type:</b> <b>{selectedButton}</b> </label><br />
                                    <button className={(selectedButton == 'S')? "active": ""} onClick={() => { handleButtonClick('S')}} type="radio" radioGroup="">S</button>
                                    <button className={(selectedButton == 'M')? "active": ""} onClick={() => { handleButtonClick('M')}} type="radio" radioGroup="type">M</button>
                                    <button className={(selectedButton == 'L')? "active": ""} onClick={() => { handleButtonClick('L')}} type="radio" radioGroup="type">L</button>
                                    <button className={(selectedButton == 'XL')? "active": ""} onClick={() => { handleButtonClick('XL')}} type="radio" radioGroup="type">XL</button>
                                </div>

                                <div className="quantity">
                                    <label htmlFor="quantity">Quantity: </label>
                                    <select name="quantity">
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                    </select>
                                </div>
                            </div>

                            <div className="purchase-btn">
                                <button className="buy-btn details_btn"> Buy Now </button>
                                <button className="add-cart-btn details_btn"> Add to cart </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}