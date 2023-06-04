import { Link } from 'react-router-dom'

export function Products({productName, productImgUrl, productDesc}) {
    return (
        <>
        <div className="card" >
            <div className="card-body">
                <img src={productImgUrl} />
                <h5 className="card-title">{productName}</h5>
                <p className="card-text">{productDesc}</p>
                <Link to={`${productName}`} className="btn btn-primary">Buy</Link>
          </div>
        </div>
        </>
    )
}