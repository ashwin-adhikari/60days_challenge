import { useEffect, useState } from "react";

const BASE_URL = ` http://api.weatherapi.com/v1/current.json?key=04de50b2ab2a4ade9bc154816241707&q=Kathmandu`
const URL = ` http://api.weatherapi.com/v1/timezone.json?key=04de50b2ab2a4ade9bc154816241707&q=Kathmandu`

export default function Weather(){
    const [location, setLocation] = useState([])
    const [temp, setTemp] = useState(0)
    const [time, setTime] = useState("")


    useEffect(() => {
        const fetchlocation = async () => {
            const result = await fetch(URL)
            result.json().then(json => {
                setLocation(json.location.name +' ' +json.location.country) 
            })
        }
        fetchlocation()
    }, []);


    useEffect(() => {
        const fetchdata = async () => {
            const result = await fetch(BASE_URL)
            result.json().then(json => {
                setTemp(json.current.temp_c)  
            })
        }
        fetchdata()
    }, []);
    useEffect(() => {
        const fetchtime = async () => {
            const result = await fetch(URL)
            result.json().then(json => {
                setTime(json.location.localtime)
            })
        }
        fetchtime()
    }, []);

    return(<>
        <div className="location">Location: {location}</div>
        <div className="temperature">Current Temperature: {temp}°C</div>
        <div className="time">Current time: {time}</div>
        </>
    );
}