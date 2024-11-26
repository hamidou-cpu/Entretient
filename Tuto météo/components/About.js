import React from "react"
import {View, Text, Linking} from 'react-native'
import Style from "../Style"

function About() {
    return (
        <View>
            <View style={Style.textcontainer}>
                <Text style={Style.text}>Ceci est une application test pour apprendre le React Native.</Text> 
                <Text style={Style.text}>Inspirée de la vidéo Youtube de Grafikart.fr : </Text>
                <Text style= {Style.textlink} onPress={() => Linking.openURL('https://www.youtube.com/embed/Y7rbJRjaYCY&t=2405s')}>Voir la vidéo</Text>
            </View>
            <View style={Style.textcontainer}>
                <Text style={Style.text}>Réalisée par Lucine Giraud en février 2022 </Text>
                <Text style= {Style.textlink} onPress={() => Linking.openURL('https://github.com/lucinegrd')}>Lien Github</Text>
            </View>
        </View>
    )
}


export default About