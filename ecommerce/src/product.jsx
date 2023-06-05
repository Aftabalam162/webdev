
export default function Product() {

    return (
        <>
            <div className="product-showcase">
                <div className="product-images">
                    <img src="" />
                    <img src="" />
                    <img src="" />
                    <img src="" />
                </div>
                {/* all the images */}
                <div className="product-image_zoomin">

                </div>
                {/* main image div */}
            </div>

            <div className="description">
                <div className="product-title">

                </div>
                <div className="product-details">

                </div>
                <div className="product-spec">

                </div>
            </div>

            <div className="purchase-details">
                <div className="product-type">
                    <label htmlFor="type">Type</label>
                    <button name="type" type="radio" radioGroup="type">S</button>
                    <button name="type" type="radio" radioGroup="type">M</button>
                    <button name="type" type="radio" radioGroup="type">L</button>
                    <button name="type" type="radio" radioGroup="type">XL</button>
                </div>

                <div className="quantity">
                    <label htmlFor="quantity">Quantity</label>
                    <select name="quantity">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                </div>
            </div>
        </>
    )
}