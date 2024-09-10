import React, { useState } from 'react';
import { View, TouchableOpacity, Text, StyleSheet, Dimensions } from 'react-native';
import axios from 'axios';

const screenWidth = Dimensions.get('window').width;

export default function LedControlScreen() {
  const [ledStatus, setLedStatus] = useState('');
  const [thresholdExceeded, setThresholdExceeded] = useState(false);

  const handlePress = async () => {
    try {
      const response = await axios.post('http://192.168.147.95/api/blink-led/');
      setLedStatus(response.data.message);
    } catch (error) {
      console.error('Error posting to Django:', error);
    }
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity
        onPress={handlePress}
        style={[styles.button, { backgroundColor: thresholdExceeded ? 'green' : '#763626' }]}
      >
        <Text style={styles.buttonText}>BLINK LED</Text>
      </TouchableOpacity>
      <Text style={styles.ledStatus}>{ledStatus}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFF2D7',
  },
  button: {
    width: screenWidth * 0.8,
    padding: 15,
    borderRadius: 150,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  ledStatus: {
    marginTop: 20,
    fontSize: 16,
    marginBottom:-40,
    marginLeft:40,
    color: 'black',
  },
});
