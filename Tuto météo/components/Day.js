import { Text, ScrollView, View, Image } from "react-native"
import Style from "../Style"

function Day({day}){
    const days=["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]
    const date=new Date(day.dt*1000)
    const sunrise = new Date(day.sunrise*1000).getHours() + "h" + new Date(day.sunrise*1000).getMinutes()
    const sunset = new Date(day.sunset*1000).getHours() + "h" + new Date(day.sunset*1000).getMinutes()
    const id = day.weather[0].icon

    const url = '../assets/iconWeather/'.concat(id, '.png')

    function image(){
        switch (day.weather[0].icon) {
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

    return <View style={Style.day}>
                
                <View style={Style.dayitem}>
                    <Text style={Style.daytitle}>{days[date.getDay()]} </Text>
                    {image()}
                    <Text style={Style.dayTemp}>{Math.round(day.temp.day)}°</Text>
                </View>
                <View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/max.png')}/>
                        <Text>{Math.round(day.temp.max)}°</Text>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/min.png')}/>
                        <Text>{Math.round(day.temp.min)}°</Text>
                    </View>
                </View>
                <View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/vent.png')}/>
                        <Text>{Math.round(day.wind_speed*3.6)} km/h</Text>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/ressenti.png')}/>
                        <Text>{Math.round(day.feels_like.day)}°</Text>
                    </View>
                </View>
                <View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/pluie.png')}/>
                        <Text>{day.pop}%</Text>
                    </View> 
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/nuage.png')}/>
                        <Text>{day.clouds}%</Text>
                    </View>
                </View>
                    <View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/sunrise.png')}/>
                        <Text>{sunrise}</Text>
                    </View>
                    <View style={Style.dayitem}>
                        <Image style={Style.dayIcon} source={require('../assets/iconWeather/sunset.png')}/>
                        <Text>{sunset}</Text>
                    </View>
                </View>              
            </View>
}

export default Day