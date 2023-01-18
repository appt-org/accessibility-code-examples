# Accessibility order

Assistive technologies try to determine a logical accessibility order based on the placement and properties of the elements on the screen. In Left-to-Right languages, the order goes from top to bottom, from left to right. If this order is not optimal, you can override the accessibility order that assistive technologies follow.

## WCAG

Relates to 1.3.2, 2.1.1, 2.4.3

## Android

On Android, you can set the accessibility order in XML, or modify the accessibility order in code. You can use the [`android:accessibilityTraversalAfter`](https://developer.android.com/reference/android/view/View#attr_android:accessibilityTraversalAfter) and [`android:accessibilityTraversalBefore`](accessibilityTraversalBefore) properties in XML. Or you can use the [`setAccessibilityTraversalBefore`](https://developer.android.com/reference/android/view/View#setAccessibilityTraversalBefore(int)) and [`setAccessibilityTraversalAfter`](https://developer.android.com/reference/android/view/View#setAccessibilityTraversalAfter(int)) methods in code.

```xml
<TextView
    android:id="@+id/header" />
<RecyclerView
    android:id="@+id/list"
    android:accessibilityTraversalAfter="@id/description" />
<TextView
    android:id="@+id/description"
    android:accessibilityTraversalBefore="@id/header" />
```

```kotlin
header.setAccessibilityTraversalBefore(R.id.description)
list.setAccessibilityTraversalAfter(R.id.description)
```

## iOS

On iOS, you can use the [`accessibilityElements`](https://developer.apple.com/documentation/objectivec/nsobject/1615147-accessibilityelements) property to set the order for assistive technologies. Be careful using the `accessibilityElements` property, because any elements left out of the array cannot be reached with assistive technologies.

```swift
view.accessibilityElements = [header, description, list]
```

## Flutter

For sorting the focus order in Flutter apps, the `sortKey` parameter of [`Semantics`](https://api.flutter.dev/flutter/semantics/SemanticsProperties-class.html) is used.

This parameter uses a [`SemanticsSortKey`](https://api.flutter.dev/flutter/semantics/SemanticsSortKey-class.html) to sort the elements. The most common way to sort elements is the [`OrdinalSortKey`](https://api.flutter.dev/flutter/semantics/OrdinalSortKey-class.html), but you can also write your own implementation based on the `SemanticsSortKey` class.

The `OrdinalSortKey` needs an `order` as double and optionally a `name` as String. The elements are then sorted by name, with empty names handled first, and subsequently by `order`.

It is also possible to leave out the `sortKey`. In this case, Flutter will generate `OrdinalSortKey`'s based on a platform specific algorithm. This order is often the order you want, but make sure to verify the sequence by using an assistive technology such as the screen reader.

```dart
Widget focusOrderWidget(context) {
    return Scaffold(
        body: Center(
            child: Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                    Semantics(
                        sortKey: OrdinalSortKey(2.0),
                        child: Text("Second focus")
                    ),
                    Semantics(
                        sortKey: OrdinalSortKey(1.0),
                        child: Text("First focus")
                    )
                ],
            )
        )
    );
}
```

## React Native

React Native does not have support for changing the focus order. You can use the [`accessible`](https://reactnative.dev/docs/accessibility#accessible) prop to indicate that a view should be focusable. The child elements get grouped together.

More information about the lack of support for changing accessibility order can be found inside [Discussion 389](https://github.com/react-native-community/discussions-and-proposals/discussions/389) of the React Native Community.

```jsx
Not available, contribute!
```

## Xamarin

Xamarin Forms supports changing the accessibility order through the [`TabIndex`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.tabindex?view=xamarin-forms) property. The default value is 0. The lower the value, the higher the priority. For example, to reach the save button before reaching the cancel button, the cancel button's `TabIndex` needs to be higher than the save button.

```xml
<Label Text="Appt" />
<Button x:Name="cancelButton" TabIndex="20" />
<Button x:Name="saveButton" TabIndex="10"/>
```
