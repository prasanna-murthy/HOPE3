import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './src/screens/HomeScreen';
import SignupScreen from './src/screens/SignupScreen';
import LoginScreen from './src/screens/LoginScreen';
import MainScreen from './src/screens/MainScreen';
import LedControlScreen from './src/screens/LedControlScreen'; 
import VisualizeScreen from './src/screens/VisualizeScreen';
import FanControlScreen from './src/screens/FanControlScreen';
const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen 
          name="Home" 
          component={HomeScreen} 
          options={{ headerShown: false }} // Hide header
        />
        <Stack.Screen 
          name="Signup" 
          component={SignupScreen} 
          options={{ headerShown: false }} // Hide header
        />
        <Stack.Screen 
          name="Login" 
          component={LoginScreen} 
          options={{ headerShown: false }} // Hide header
        />
        <Stack.Screen 
          name="Main" 
          component={MainScreen} 
          options={{ headerShown: false }} // Hide header
        />
        <Stack.Screen 
          name="LedControlScreen" 
          component={LedControlScreen} 
          options={{ headerShown: false }} // Hide header
        />
        <Stack.Screen 
          name="VisualizeScreen" 
          component={VisualizeScreen} 
          options={{ headerShown: false }} // Hide header
        />
         <Stack.Screen name="FanControlScreen" 
         component={FanControlScreen}
         options={{ headerShown: false }}  />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

