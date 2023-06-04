import { useRouteError } from "react-router-dom";

export default function ErrorPage() {

    const error = useRouteError();
    console.error(error);

    return(
        <>
        <h1>OOPS! Looks like what you're searching for doesn't exist...</h1>
        </>
    )
}