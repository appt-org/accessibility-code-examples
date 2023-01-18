# Motion input

Provide an alternative way for actions activated by motion, to allow everyone to use the functionality. For example, for users with limited hand function, shaking is not always possible. Also make it possible to disable actions activated by motion. For example, for users with spasms, these actions could be triggered accidentally.

## WCAG

Relates to 2.5.4

## Android

On Android, the [`SensorManager`](https://developer.android.com/reference/android/hardware/SensorManager) can be used in combination with [`SensorEventListener`](https://developer.android.com/reference/android/hardware/SensorEventListener) to detect movement.

An event through sensors should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```kotlin
class SensorActivity : AppCompatActivity(), SensorEventListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        val sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_NORMAL)
    }

    override fun onSensorChanged(event: SensorEvent?) {
        // Add alternative
    }
}
```

## iOS

On iOS, it is common to use the [`motionEnded`](https://developer.apple.com/documentation/uikit/uiresponder/1621090-motionended) method to detect motion.

A motion event should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```swift
import UIKit

class MotionController: UIViewController {

    override var canBecomeFirstResponder: Bool{
        return true
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        becomeFirstResponder()
    }

    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        // Provide alternative
    }
}
```

## Flutter

With Flutter, packages like [`sensors_plus`](https://pub.dev/packages/sensors_plus) can be used to detect movement.

An event through sensors should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```dart
import 'package:sensors_plus/sensors_plus.dart';

accelerometerEvents.listen((AccelerometerEvent event) {
  // Provide alternative
});
```

## React Native

In React Native, packages like [`expo-sensors`](https://docs.expo.dev/versions/latest/sdk/sensors/) can be used to detect motion.

An event through sensors should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```jsx
import { Accelerometer } from 'expo-sensors';

export default function App() {
  const _subscribe = () => {
    setSubscription(
      Accelerometer.addListener(accelerometerData => {
        // Provide alternative
      })
    );
  };
}
```

## Xamarin

In Xamarin, the [`Accelerometer`](https://docs.microsoft.com/en-us/xamarin/essentials/accelerometer) class can be used to listen to changes in acceleration of the device in three-dimensional space.

An event through acceleration should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```csharp
Accelerometer.ReadingChanged += Accelerometer_ReadingChanged;

void Accelerometer_ReadingChanged(object sender, AccelerometerChangedEventArgs e)
{
    // Provide alternative
}
```
