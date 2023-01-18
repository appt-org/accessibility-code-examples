# Linting

Linting is the process of running a tool which analyzes your code for potential errors. Generally, each problem detected by the tool is reported with a description message and a severity level. This allows you to quickly prioritize the critical improvements that need to be made. Everyone benefits from higher code quality, plus it improves the accuracy of assistive technologies.

## WCAG

Relates to 4.1.1

## Android

On Android you can use [`AndroidLint`](https://developer.android.com/studio/write/lint) to improve the quality of your code.

Check if you are using outdated code. In Android Studio you can check this by selecting the following menu options:

1. Kotlin
2. Migration
3. Usage of redundant or deprecated syntax or deprecated symbols

Avoid errors with automated testing. Follow the [UI-testing guide for Android](https://developer.android.com/training/testing/ui-testing).

```kotlin
/AndroidSDK/tools/lint /project
```

## iOS

On iOS you can use [`SwiftLint`](https://github.com/realm/SwiftLint) to improve the quality of your code.

Avoid errors with automated testing. On iOS you can use the [XCTest framework](https://www.hackingwithswift.com/articles/148/xcode-ui-testing-cheat-sheet).

```swift
swiftlint lint
```

## Flutter

Flutter ships with a built-in linter named [`flutter_lints`](https://docs.flutter.dev/release/breaking-changes/flutter-lints-package). Run `flutter analyze .` in the root of a project to return all usages of deprecated code.

If possible, always update Flutter to the newest version.

Avoid errors with automated testing. Follow the [How to test a Flutter App - Codelab](https://codelabs.developers.google.com/codelabs/flutter-app-testing#0) to get started.

```dart
flutter analyze .
```

## React Native

React Native ships a built-in linter named [`ESLint`](https://eslint.org/).

If possible, always update React Native to the newest version.

Avoid errors with automated testing. Follow the [Testing guide](https://reactnative.dev/docs/testing-overview) to get started.

```jsx
npx eslint "project/**"
```

## Xamarin

With Xamarin, you can can use a lint tool with `Xamarin.Android` projects. Set the property `AndroidLintEnabled` to true in your `.csproj`.

Unfortunately, there is no built-in lint tool for `Xamarin.iOS` projects.

```xml
<AndroidLintEnabled>true</AndroidLintEnabled>
```
