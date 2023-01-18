# Input gestures

Gesture activated functionality should also be available without the use of gestures. Not everyone is able to make all gestures. For example, for users with limited mobility it might be difficult or impossible to make the 'pinch-to-zoom' gesture. You should provide buttons to zoom in and out as an alternative.

## WCAG

Relates to 2.5.1

## Android

On Android, the [`GestureDetector`](https://developer.android.com/reference/android/view/GestureDetector) and  [`OnGestureListener`](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener) objects are a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```kotlin
val scaleGestureDetector = ScaleGestureDetector(
    this,
    object : ScaleGestureDetector.SimpleOnScaleGestureListener() {
        override fun onScale(detector: ScaleGestureDetector): Boolean {
            // Provide alternative
            return super.onScale(detector)
        }
    }
)

view.setOnTouchListener { _, event ->
    scaleGestureDetector.onTouchEvent(event)
}
```

## iOS

On iOS, the [`UIGestureRecognizer`](https://developer.apple.com/documentation/uikit/uigesturerecognizer) and [`UIGestureRecognizerDelegate`](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate) objects are a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```swift
let gesture = UIPinchGestureRecognizer(
    target: self, 
    action: #selector(onPinch(_:))
)
addGestureRecognizer(gesture)

@objc private func onPinch(_ sender: UIPinchGestureRecognizer) {
    // Provide alternative
  }
}
```

## Flutter

In Flutter, the [`GestureDetector`](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html) class is a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```dart
double _baseScaleFactor = 1;
double _scaleFactor = 1;

GestureDetector(
  onScaleStart: (details) {
    _baseScaleFactor = _scaleFactor;
  },
  onScaleUpdate: (details) {
    setState(() {
      _scaleFactor = _baseScaleFactor * details.scale;
      // Provide alternative
    });
  },
  child: ...
  ),
);
```

## React Native

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

## Xamarin

With Xamarin, it is common to detect gestures using one of the recognizers defined in [`Xamarin Forms Gestures`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/gestures/).

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```csharp
var pinchGesture = new PinchGestureRecognizer();
pinchGesture.PinchUpdated += (sender, event) => {
  // Provide alternative
};
view.GestureRecognizers.Add(pinchGesture);
```
