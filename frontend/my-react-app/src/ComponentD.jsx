import { UserContext } from "./ComponentA";
import React, {useContext} from "react";

export default function ComponentD(){

    const user = useContext(UserContext)

    return(
        <div className="box">
            <h1>ComponentD</h1>
            <h2>{`Bye ${user}`}</h2>
        </div>
    );
}