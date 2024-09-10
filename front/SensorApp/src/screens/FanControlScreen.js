import React from 'react';
import { View, Button, Alert, StyleSheet, Dimensions, TouchableOpacity, Text } from 'react-native';
import axios from 'axios';

const screenWidth = Dimensions.get('window').width;

const ControlFanScreen = () => {
  // Function to control the fan
  const controlFan = (state) => {
    axios.post('http://198.168.147.95/api/control-fan/', {
      state: state,
    })
    .then((response) => {
      // Success handler
      Alert.alert('Success', response.data.status);
    })
    .catch((error) => {
      // Error handler
      console.error(error);
      Alert.alert('Error', 'Failed to control the fan.');
    });
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity
        onPress={() => controlFan('on')}
        style={[styles.button, { backgroundColor: '#4CAF50' }]} // Green for ON
      >
        <Text style={styles.buttonText}>TURN FAN ON</Text>
      </TouchableOpacity>

      <TouchableOpacity
        onPress={() => controlFan('off')}
        style={[styles.button, { backgroundColor: '#F44336', marginTop: 20 }]} // Red for OFF
      >
        <Text style={styles.buttonText}>TURN FAN OFF</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFF2D7', // Light green background
  },
  button: {
    width: screenWidth * 0.8,
    padding: 15,
    borderRadius: 150, // Rounded button
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default ControlFanScreen;
