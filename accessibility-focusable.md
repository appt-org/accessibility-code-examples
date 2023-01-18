# Accessibility focusable

An element should indicate whether it should be focusable by assistive technologies or not. You can help users of assistive technologies by choosing which elements they can interact with. By keep unnecessary elements out of the accessibility tree, the user experience is improved.

## WCAG

Relates to 1.1.1

## Android

On Android, you can use the [`setImportantForAccessibility`](https://developer.android.com/reference/android/view/View#setImportantForAccessibility(int)) method to set whether assistive technologies can focus on an element. You can also set this property directly in XML by using the [`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility) property.

```kotlin
view.importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_NO
```

```xml
<View
  android:importantForAccessibility="no" />
```

## iOS

On iOS, you can use the [`isAccessibilityElement`](https://developer.apple.com/documentation/objectivec/nsobject/1615141-isaccessibilityelement) property to indicate whether assistive technologies can focus on an element.

```swift
element.isAccessibilityElement = false
```

## Flutter

On Flutter, the [`focusable`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/focusable.html) property of [`SemanticsProperties`](https://api.flutter.dev/flutter/semantics/SemanticsProperties-class.html) can be used to indicate whether assistive technologies can focus on an element.

```dart
Semantics(
  focusable: false,
  child: Widget();
);
```

## React Native

In React Native, the [`accessible`](https://reactnative.dev/docs/accessibility#accessible) property indicates whether assistive technologies can focus on an element.

```jsx
<View accessible />
```

## Xamarin

In Xamarin, the [`IsInAccessibleTree`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesisinaccessibletree) property indicates whether assistive technologies can focus on an element.

```xml
<Image 
  AutomationProperties.IsInAccessibleTree="False" />
```
