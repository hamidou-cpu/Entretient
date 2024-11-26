import {Text, ActivityIndicator, Image, View} from 'react-native';
import Style from '../Style';
import axios from 'axios'
import { useEffect, useState } from 'react';
import { WEATHER_MAP_API_KEY } from "@env";
import Day from './Day';


function Result({city}) {
    const [meteo, setMeteo] = useState();   
    const[ville, setVille] = useState();
    const days=["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]

    useEffect(() => {
        axios.get(`http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=${WEATHER_MAP_API_KEY}`)
            .then((res)=>{
                setMeteo(null)
                if (res.data.length !== 0) {
                    setVille(res.data[0].local_names ? res.data[0].local_names.fr : res.data[0].name)
                    const lat = res.data[0].lat
                    const long = res.data[0].lon
                    axios.get(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&lang=fr&exclude=hourly,minutely&units=metric&appid=${WEATHER_MAP_API_KEY}`)
                    .then(res => {
                        setTimeout(() => setMeteo(res.data), 200)
                    })
                }
                else {
                    setTimeout(() => setMeteo(""), 1000)
                }
            })
    }, [city])

    function image(){
        switch (meteo.current.weather[0].icon) {
            case '01d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/01d.png')}/>
            }
            case '02d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/02d.png')}/>
            }
            case '03d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/03d.png')}/>
            }
            case '04d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/04d.png')}/>
            }
            case '09d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/09d.png')}/>
            }
            case '10d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/10d.png')}/>
            }
            case '11d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/11d.png')}/>
            }
            case '13d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/13d.png')}/>
            }
            case '50d':{
                return <Image style={Style.dayImage} source={require('../assets/iconWeather/50d.png')}/>
            }
            
        }
    }

    return (meteo == null ? 
        <ActivityIndicator style={{margin:5}} color="#0066CC" size="large"/>
        : meteo == "" ? <Text style={Style.city}>Ville non trouvée</Text> : 
            <View>
                <Text style={Style.city}>{ville}</Text>
                <View style={[Style.day, {backgroundColor:"#D0E8FF"}]}>
                    <View style={Style.dayitem}>
                        <Text style={Style.daytitle}>TODAY</Text>
                        <View style={Style.today}>
                            {image()}
                            <Text style={Style.dayTemp}>{Math.round(meteo.current.temp)}°</Text>
                        </View>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/vent.png')}/>
                        <Text>{Math.round(meteo.current.wind_speed*3.6)} km/h</Text>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/nuage.png')}/>
                        <Text>{meteo.current.clouds}%</Text>
                    </View>
                    <View style={Style.dayitem}> 
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/sunrise.png')}/>
                        <Text>{new Date(meteo.current.sunrise*1000).getHours() + "h" + new Date(meteo.current.sunrise*1000).getMinutes()}</Text>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/sunset.png')}/>
                        <Text>{new Date(meteo.current.sunset*1000).getHours() + "h" + new Date(meteo.current.sunset*1000).getMinutes()}</Text>
                    </View>
                </View>
                {Object.keys(meteo.daily).map((index) => <Day key={index} day={meteo.daily[index]}/>)}
            </View>
        )
}

export default Result