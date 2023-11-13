# Scale text - Android

On Android, you can use [Scale-independent Pixels](https://developer.android.com/guide/topics/resources/more-resources.html#Dimension) to scale text. This unit ensures that the user's preferences are taken into account when determining the font size. We recommend to define the [`textSize`](https://developer.android.com/reference/android/widget/TextView#attr_android:textSize) in your styles to make sure it's the same everywhere.

```xml
<style name="Widget.TextView">
    <item name="android:textSize">18sp</item>
</style>
```
