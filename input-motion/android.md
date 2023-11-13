# Motion input - Android

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
