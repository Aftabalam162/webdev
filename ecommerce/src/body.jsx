import { Carousel } from './carousel'
import { Products } from './products'

const products = [
    {productName: 'Shirt', productImage: 'banner1.png', productDesc: 'This is the nicest shirt in town'},
    {productName: 'Watch', productImage: 'banner2.png', productDesc: 'This is the best watch in the country'},
 
]
// this should have been fetched from the database

const renderProducts = products.map((item) => { return (<Products productName={item.productName} productDesc={item.productDesc} productImgUrl={item.productImage} />)})


export function Main() {

    return (
        <>
        <div className="main">
            <Carousel/>
            <div className="container">
            { renderProducts }
            </div>
        </div>
        </>
    )
//productName, productImgUrl, productDesc

}