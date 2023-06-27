import { useState } from "react";

export default function Product() {


    const [selectedButton, setSelectedButton] = useState('small');
    const [zoomedImage, setZoomedImage] = useState('banner1.png')
    const [productQuantity, setProductQuantity] = useState(0)

    function handleButtonClick(event) {
    
        setSelectedButton(event.target.value);
    }

    function handleQuantityChange(event) {

        setProductQuantity(event.target.value)
    }

    function handleImageZoomClick(event) {

        setZoomedImage(event.target.src.replace('http://localhost:5173/', ''))
    }
  
    return (
        <>
            <div className="product-container">

                <div className="product-showcase">
                <div className="product-images">
                    <img src="banner1.png" onClick={handleImageZoomClick}/>
                    <img src="banner2.png" onClick={handleImageZoomClick}/>
                    <img src="banner3.png" onClick={handleImageZoomClick}/>
                    {/* <img src="" /> */}
                </div>
                {/* all the images */}
                <div className="product-image_zoomin">
                    <img src={zoomedImage} />
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
                                <thead>
                                    <tr>
                                        <td><b>Cloth: </b></td>
                                        <td>Cotton</td>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><b>Sizes Available: </b></td>
                                        <td>S, M, L and XL</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>


                        <div className="product-choice">
                            <div className="product-type">


                                <div className="product-size">
                                    <label htmlFor="type"><b>Type:</b> </label><br />
                                    <input checked={selectedButton === 'small'} onChange={handleButtonClick} type="radio" name="size" value='small'/>S
                                    <input checked={selectedButton === 'medium'} onChange={handleButtonClick} type="radio" name="size" value='medium'/>M
                                    <input checked={selectedButton === 'large'} onChange={handleButtonClick} type="radio" name="size" value='large'/>L
                                    <input checked={selectedButton === 'extraLarge'} onChange={handleButtonClick} type="radio" name="size" value='extraLarge'/>XL
                                </div>

                                <div className="quantity">
                                    <label htmlFor="quantity">Quantity: </label>

                                    <input type="number" name="quantity" id="quantity" min="0" max="3" onChange={handleQuantityChange}/>
                                </div>
                            </div>

                            <div className="purchase-btn">
                                <button className="buy-btn details_btn"> Buy Now {(productQuantity == 0)? '': '($' + productQuantity*15+ ')' } </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}