# Motion input - Xamarin

In Xamarin, the [`Accelerometer`](https://docs.microsoft.com/en-us/xamarin/essentials/accelerometer) class can be used to listen to changes in acceleration of the device in three-dimensional space.

An event through acceleration should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```csharp
Accelerometer.ReadingChanged += Accelerometer_ReadingChanged;

void Accelerometer_ReadingChanged(object sender, AccelerometerChangedEventArgs e)
{
    // Provide alternative
}
```
