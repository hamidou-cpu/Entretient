import { useState } from 'react'
import {TextInput, View, TouchableHighlight, ScrollView, Keyboard} from 'react-native'
import style from '../Style.js'
import { Ionicons } from '@expo/vector-icons';
import Result from './Result.js';
import { useBottomTabBarHeight } from '@react-navigation/bottom-tabs';


function Search() {
    const [city, onChangeCity] = useState(null)
    const [search, onChangeSearch] = useState(null)
    const [showResult, changeShowResult] = useState(false)

    function submit() {
        onChangeCity(search)
        changeShowResult(true)
    }

    const tabBarHeight = useBottomTabBarHeight();

    return (
        <View style={{paddingBottom:tabBarHeight+10}}>
            <View style={style.searchcontainer}>
                <View style={style.textinputcontainer}>
                    <TextInput
                        onChangeText={onChangeSearch}
                        value={search}
                        placeholder="Rechercher une ville"
                        style={style.textinput}
                        onSubmitEditing={() => {submit(search), onChangeSearch(''), Keyboard.dismiss()}}
                    />
                </View>
                <TouchableHighlight
                    activeOpacity={0.3}
                    style={style.button}
                    onPress={() => {submit(search), onChangeSearch(''), Keyboard.dismiss()}}
                    keyboardShouldPersistTaps='never'
                >
                    <Ionicons name="search-outline" size={25} color="white" style={{marginHorizontal:6}}/>
                </TouchableHighlight>
            </View>
            <ScrollView keyboardDismissMode='on-drag'>
                {showResult && <Result city={city}/>}
            </ScrollView>
        </View>
        
        
    )
}

export default Search