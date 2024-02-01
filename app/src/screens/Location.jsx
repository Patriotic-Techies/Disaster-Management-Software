import React from 'react'
import { View, StyleSheet } from 'react-native'
import { WebView } from 'react-native-webview'

import useGlobal from '../core/global'

const LocationScreen = () => {
  const user = useGlobal(state => state.user)
  const latitude = 10.909119780582465
  const longitude = 76.97672426163373

  return (
    <View style={styles.container}>
      <WebView
        source={{
          html: `
            <iframe
              width="100%"
              height="100%"
              frameborder="0"
              scrolling="no"
              marginheight="0"
              marginwidth="0"
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3962.0479035690067!2d${longitude}!3d${latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x${longitude}%3A${latitude}!2sYour%20Location!5e0!3m2!1sen!2sus!4vYOUR_EMBEDDED_MAP_API_KEY"
              allowfullscreen
            ></iframe>
          `,
        }}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
})

export default LocationScreen