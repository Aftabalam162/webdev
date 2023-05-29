import { Carousel } from './carousel'
import { Products } from './products'

export function Main() {
    return (
        <>
        <div className="main">
            <Carousel/>
            <div className="container">
              <Products />
              <Products />
              <Products />
              <Products />
              <Products />
            </div>
        </div>
        </>
    )

    function clickHandler() {
        const page = document.getElementsByClassName('main')[0];
        const navbarToggleButton = document.getElementsByClassName('navbar-toggler')[0];
        const navbarContent = document.getElementById('navbarSupportedContent');
        
        page.addEventListener('click',() => {
            navbarContent.classList.remove('show');
        })
    }
}