# Descriptive labels

Screens should have descriptive labels, these help users recognize which purpose controls have.  It is recommended to put distinguishing information at the beginning of your labels.

## WCAG

Relates to 2.4.6

## Android

On Android, labels created with [`TextView`](https://developer.android.com/reference/android/widget/TextView) can be changed with the [`setText`](https://developer.android.com/reference/android/widget/TextView#setText(java.lang.CharSequence)) method.

```kotlin
label.text = "Descriptive label"
```

## iOS

On iOS, labels created with [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) can be changed with the [`text`](https://developer.apple.com/documentation/uikit/uilabel/1620538-text) property.

```swift
label.text = "Descriptive label"
```

## Flutter

In Flutter, labels created with `Text` can be changed with the unnamed [`data`](https://api.flutter.dev/flutter/widgets/Text/data.html) property.

```dart
Text('Descriptive label')
```

## React Native

In React Native, labels created by using [`Text`](https://reactnative.dev/docs/text) can be changed by using a [`state hook`](https://reactjs.org/docs/hooks-state.html).

```jsx
<Text>Descriptive label</Text>
```

## Xamarin

In Xamarin, labels created by using [`Label`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label?view=xamarin-forms) can be changed with the [`Text`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.textproperty?view=xamarin-forms) property.

```xml
<Label Text="Descriptive label" />
```
