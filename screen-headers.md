# Descriptive headers

Screens should have descriptive headers, this helps users find specific content and orient themselves within your app. It is recommended to put distinguishing information at the beginning of your headers.

## WCAG

Relates to 2.4.6

## Android

On Android, headers created with [`TextView`](https://developer.android.com/reference/android/widget/TextView) can be changed with the [`setText`](https://developer.android.com/reference/android/widget/TextView#setText(java.lang.CharSequence)) method.

```kotlin
header.text = "Descriptive header"
ViewCompat.setAccessibilityHeading(header, true)
```

## iOS

On iOS, headers created with [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) can be changed with the [`text`](https://developer.apple.com/documentation/uikit/uilabel/1620538-text) property.

```swift
header.text = "Descriptive header"
header.accessibilityTraits = .header
```

## Flutter

In Flutter, headers created with `Text` can be changed with the unnamed [`data`](https://api.flutter.dev/flutter/widgets/Text/data.html) property.

```dart
Semantics(
  header: true,
  child: Text('Descriptive header')
);
```

## React Native

In React Native, headers created by using [`Text`](https://reactnative.dev/docs/text) can be changed by using a [`state hook`](https://reactjs.org/docs/hooks-state.html).

```jsx
<Text accessibilityRole="header">
    Descriptive header
</Text>
```

## Xamarin

In Xamarin, headers created by using [`Label`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label?view=xamarin-forms) can be changed with the [`Text`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.textproperty?view=xamarin-forms) property.

```xml
<Label 
    xct:SemanticEffect.HeadingLevel="1"
    Text="Descriptive header" />
```
