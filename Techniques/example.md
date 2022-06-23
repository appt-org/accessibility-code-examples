# Add accessibility label

## Android

Add a label to all content without text.

On Android, you can use the [contentDescription](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) property.

```kotlin
element.contentDescription = "Description"
```

## iOS

On iOS, you can use the [accessibilityLabel](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) property to add a label.

```swift
element.accessibilityLabel = "Description"
```

## Flutter

With Flutter, a `label` or `attributedLabel` from the [Semantics](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget can be used. The  `label` is used by assistive technologies such as the screen reader. The `attributedLabel` can be used for more control over how it should be pronounced. For example by spelling out each character with [SpellOutStringAttribute](https://api.flutter.dev/flutter/dart-ui/SpellOutStringAttribute-class.html) or forcing another language with [LocaleStringAttribute](https://api.flutter.dev/flutter/dart-ui/LocaleStringAttribute-class.html).

```dart
Semantics(
  label: 'Appt',
  child: ListTile(...);
);
```

## React Native

In React Native you can add the [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) prop on almost any element. Depending on the element used you need to make it accessible first by adding the [`accessible`](https://reactnative.dev/docs/accessibility#accessible) prop.

```jsx
<Image
  source={require("exclamation-mark.png")}
  accessible
  accessibilityLabel="Warning!"
/>
```

## Xamarin

In Xamarin Forms you can add labels using the following property:

```xml
<Entry AutomationProperties.Name="Appt" />
```
