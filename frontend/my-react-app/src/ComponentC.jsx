import ComponentD from "./ComponentD";
import { UserContext } from "./ComponentA";
import React, {useContext} from "react";
export default function ComponentC(){
    const user = useContext(UserContext)
    return(
        <div className="box">
            <h1>ComponentC</h1>
            <h2>{`${user} was here`}</h2>
            <ComponentD/>
        </div>
    );
}