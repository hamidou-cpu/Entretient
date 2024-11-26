import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import About from './components/About';
import Search from './components/Search';
import { Ionicons } from '@expo/vector-icons';
import {StatusBar} from 'expo-status-bar'

const color = '#0066CC'

const Tab = createBottomTabNavigator();

export default function App() {
	return (
		<NavigationContainer>
			<StatusBar style="dark" />
			<Tab.Navigator
				screenOptions={{
					tabBarActiveTintColor: "white",
					tabBarInactiveTintColor: color,
					tabBarActiveBackgroundColor : color,
					tabBarInactiveBackgroundColor: "white"
				}}
			>
				<Tab.Screen 
					name="Météo" 
					component={Search} 
					options={{
						tabBarIcon: ({color, size}) => <Ionicons name="partly-sunny-outline" size={size} color={color}/>,
						tabBarShowLabel : false,
					}}
				/>
				<Tab.Screen
					name="À propos"
					component={About}
					options={{
						tabBarIcon: ({color, size}) => <Ionicons name="information-circle-outline" size={size} color={color} />,
						tabBarShowLabel : false
					}}
				/>
			</Tab.Navigator>
		</NavigationContainer>
	);
}