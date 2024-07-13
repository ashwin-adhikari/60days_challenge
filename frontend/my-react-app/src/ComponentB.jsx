import ComponentC from "./ComponentC";
import { UserContext } from "./ComponentA";
import React, {useContext} from "react";

export default function ComponentB(){
    const user = useContext(UserContext)
    return(
        <div className="box">
            <h1>ComponentB</h1>
            <h2>{`${user} used useContext hook instead of prop drilling`}</h2>
            <ComponentC/>
        </div>
    );
}