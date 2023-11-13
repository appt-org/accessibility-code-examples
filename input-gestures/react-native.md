# Input gestures - React Native

In React Native, the [`Gesture Responder System`](https://reactnative.dev/docs/gesture-responder-system) is a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```jsx
import { PinchGestureHandler, State } from 'react-native-gesture-handler'

const PinchableView = () => {
  scale = new Animated.Value(1)

  onPinchEvent = Animated.event([{
    nativeEvent: { scale: this.scale }
  }], {
      useNativeDriver: true
  })

  
  onPinchStateChange = event => {
    if (event.nativeEvent.oldState === State.ACTIVE) {
        // Provide alternative
        Animated.spring(this.scale, {
            toValue: 1,
            useNativeDriver: true
        }).start()
    }
  }

  return (
    <PinchGestureHandler
        onGestureEvent={this.onPinchEvent}
        onHandlerStateChange={this.onPinchStateChange}>
        <View style={{
            transform: [{ scale: this.scale }] 
        }} />
    </PinchGestureHandler>
  )
}
```
