# Headings

Headings should be marked as `heading` in code, this helps user of assistive technologies to identify them. Heading text should also be descriptive, this helps users find specific content and orient themselves within your app. It is recommended to put distinguishing information at the beginning of your headings.

## Android

On Android, you can mark headings by using the [`ViewCompat.setAccessibilityHeading`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityHeading(android.view.View,%20boolean)) method.

If headings are created by using [`TextView`](https://developer.android.com/reference/android/widget/TextView), you can change the text with the [`setText`](https://developer.android.com/reference/android/widget/TextView#setText(java.lang.CharSequence)) method.

```kotlin
ViewCompat.setAccessibilityHeading(heading, true)
heading.text = "Descriptive heading"
```

## iOS

On iOS, you can mark headings by setting the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute to [`header`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620170-header).

If headings are created by using [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel), you can change the text with the [`text`](https://developer.apple.com/documentation/uikit/uilabel/1620538-text) property.

```swift
heading.accessibilityTraits = .header
heading.text = "Descriptive heading"
```

## Flutter

In Flutter, you can mark headings by using a [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget with [`header`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/header.html) set to `true`.

If headings are created by using `Text`, you can change text by using the [`data`](https://api.flutter.dev/flutter/widgets/Text/data.html) property.

```dart
Semantics(
  header: true,
  child: Text('Descriptive heading')
);
```

## React Native

In React Native, you can mark headings by setting the [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole) prop to `header`.

If headings are created by using [`Text`](https://reactnative.dev/docs/text), the text can be changed by using a [`state hook`](https://reactjs.org/docs/hooks-state.html).

```jsx
<Text accessibilityRole="header">
    Descriptive heading
</Text>
```

## Xamarin

In Xamarin, you can use the [`SemanticEffect`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Effects/Semantic/SemanticEffect.shared.cs) effect to mark headings by using the `HeadingLevel` property.

If headings are created by using [`Label`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label?view=xamarin-forms), the text can be changed with the [`Text`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.textproperty?view=xamarin-forms) property.

```xml
<Label 
    xct:SemanticEffect.HeadingLevel="1"
    Text="Descriptive heading" />
```
