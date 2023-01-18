# Acessibility group

It is easier and quicker for users of assistive technologies to interact with grouped elements. Grouping elements into a single control makes things clearer, simplifies interactions, and provides larger touch targets.

## WCAG

Relates to 1.3.1

## Android

On Android you can group elements by using the [`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable) and [`android:screenReaderFocusable`](https://developer.android.com/reference/android/view/View#attr_android:screenReaderFocusable) attributes. Sometimes you also need the [`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility) attribute. Don't for get to set an [`android:contentDescription`](https://developer.android.com/reference/android/view/View#attr_android:contentDescription) for the group.

Keep in mind that [`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable) is not only used by assistive technologies, but also by other means of interaction.

```xml
<LinearLayout
    android:focusable="true"
    android:screenReaderFocusable="true"
    android:contentDescription="Appt group">

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

Note: all touchable elements are accessible by default.

```jsx
<View accessible accessibilityLabel="Appt group">
  <Text>Appt</Text>
  <Text>is a platform for accessibility</Text>
</View>
```

## Xamarin

Xamarin Forms does not have built-in support to group accessibility elements.

```csharp
Not available, contribute!
```
