# Screen title

Each screen should have a descriptive title, which helps users with identifying the screen.

## WCAG

Relates to 2.4.2

## Android

On Android, we recommend using a [`Toolbar`](https://developer.android.com/reference/androidx/appcompat/widget/Toolbar) with an appropriate [`title`](https://developer.android.com/reference/android/app/Activity.html#setTitle(java.lang.CharSequence)) on each screen.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.appt)

    val toolbar = findViewById(R.id.toolbar)
    setSupportActionBar(toolbar)
    title = "Appt homescreen"
}
```

## iOS

On iOS, we recommend using a [`UINavigationController`](https://developer.apple.com/documentation/uikit/uinavigationcontroller) with an appropriate [`title`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title) on each screen.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    title = "Appt homescreen"
}
```

## Flutter

In Flutter, we recommend using an [`AppBar`](https://api.flutter.dev/flutter/material/AppBar-class.html) with an appropriate [`title`](https://api.flutter.dev/flutter/material/AppBar/title.html) on each screen.

```dart
Scaffold(
  appBar: AppBar(
    title: const Text('Appt homescreen'),
  ),
  body: ...
);
```

## React Native

In React Native, we recommend using [React Navigation](https://reactnative.dev/docs/navigation) with an appropriate [`title`](https://reactnavigation.org/docs/headers#setting-the-header-title) on each screen.

```jsx
function StackScreen() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: 'Appt homescreen' }}
      />
    </Stack.Navigator>
  );
}
```

## Xamarin

With Xamarin Forms, we recommend setting an appropriate [`Title`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.page.title?view=xamarin-forms#xamarin-forms-page-title) for each [`ContentPage`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.contentpage?view=xamarin-forms).

```xml
<ContentPage
    x:Class="NewPage"
    xmlns="http://xamarin.com/schemas/2014/forms"
    xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
    Title="{Binding PageTitle}">
    <ContentView>
        ...
    </ContentView>
</ContentPage>
```

```csharp
public NewPage()
{
    SetBinding(Page.TitleProperty, new Binding("Appt homescreen")); 
}
```
