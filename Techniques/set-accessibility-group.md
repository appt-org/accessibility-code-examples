# Set accessibility group

It is easier and quicker for users of assistive technologies to interact with grouped elements. Grouping elements into a single control makes things clearer, simplifies interactions, and provides larger touch targets.

## Android

On Android you can group elements by using the `android:focusable` and `android:screenReaderFocusable` attributes. Sometimes you also need the . `android:importantForAccessibility` attribute. Don't for get to set a `contentDescription` for the group.

Keep in mind that `android:focusable` is not only used by assistive technologies, but also by other means of interaction.

```xml
<LinearLayout
    android:focusable="true"
    android:screenReaderFocusable="true"
    android:contentDescription="Appt group"  >
    <TextView
        android:focusable="false"
        android:importantForAccessibility="no"/>
    <ImageView
        android:focusable="false"
        android:importantForAccessibility="no"/>
</LinearLayout>
```

## iOS

On iOS, you can group elements by setting [`isAccessibilityElement`](https://developer.apple.com/documentation/objectivec/nsobject/1615141-isaccessibilityelement) to `true` on the parent element. Don't forget to set an [`accessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) for the group.

Sometimes it can be useful to also the [`shouldGroupAccessibilityChildren`](https://developer.apple.com/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren) property to group the accessibility elements that are children of the element, regardless of their positions on the screen.

```swift
group.isAccessibilityElement = true
group.shouldGroupAccessibilityChildren = true
group.accessibilityLabel = "Appt group"
```

## Flutter

On Flutter, there are multiple types of semantics to group accessibility elements. The [`excludeSemantics`](https://api.flutter.dev/flutter/widgets/Semantics/excludeSemantics.html) property can be used to override the semantics of all children. You can achieve similar behavior by using [`BlockSemantics`](https://api.flutter.dev/flutter/widgets/BlockSemantics-class.html).

```dart
Semantics(
  label: 'Appt group',
  excludeSemantics: true,
  child: Column(
        children: [
            Text('Appt'),
            Text('is a platform for accessibility')
        ]
    )
);
```

## React Native

In React Native, you can group elements together by using the [`accessible`](https://reactnative.dev/docs/accessibility#accessible) prop. An [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) should be set for grouped elements.

Note: by default, all touchable elements are accessible.

```jsx
<View accessible accessibilityLabel="Appt group">
  <Text>Appt</Text>
  <Text>is a platform for accessibility</Text>
</View>
```

## Xamarin

Xamarin Forms does not have built-in support to group accessibility elements.

```xml
Not available, contribute!
```
