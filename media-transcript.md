# Transcript

Videos should contain a transcript to allow users to read what is shown in media, such as a video or podcast.

A basic transcript contains information needed to understand what is being said. This mostly benefits people who are deaf or hard of hearing, or have difficulty processing auditory information.

A descriptive transcript also contains visual information to understand what is being shown. This mostly benefits people who are blind or visually impaired.

## WCAG

Relates to 1.2.1, 1.2.3

## Android

On Android, you can use a [`TextView`](https://developer.android.com/reference/android/widget/TextView) to display written text. Don't forget to put it in a [ScrollView](https://developer.android.com/reference/android/widget/ScrollView), to make the text scrollable.

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Appt transcript" />
</ScrollView>
```

## iOS

On iOS, you can use [`UITextView`](https://developer.apple.com/documentation/uikit/uitextview) to present a transcript. A `UITextView` is scrollable by default. You can also choose to place one or more [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel)'s in a [`UIScrollView`](https://developer.apple.com/documentation/uikit/uiscrollview).

```swift
// Option 1
let transcript = UITextView()
transcript.text = "Appt transcript"

// Option 2
let transcript = UILabel()
transcript.text = "Appt transcript"

let view = UIView()
view.addSubview(transcript)

let scrollView = UIScrollView()
scrollView.addSubview(view)
```

## Flutter

With Flutter, you can use [`Text`](https://api.flutter.dev/flutter/widgets/Text-class.html) to display written text. Make sure to wrap the `Text` widget in a [`SingleChildScrollView`](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) and to set the overflow parameter to `TextOverflow.visible`. Also, the `softwrap` parameter needs to be set to true to prevent the text from overflowing outside its container.

```dart
SingleChildScrollView(
  child: Text(
    'Appt transcript',
    softWrap: true,
    overflow: TextOverflow.visible,
  ),
)
```

## React Native

In React Native, you can use [`Text`](https://reactnative.dev/docs/text) to display written text. Make sure to wrap the `Text` widget in a [`ScrollView`](https://reactnative.dev/docs/scrollview) to enable scrolling.

```jsx
<ScrollView>
    <Text>
        Appt transcript
    </Text>
</ScrollView>
```

## Xamarin

In Xamarin, you can use [`Label`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.label?view=xamarin-forms) to display written text. Make sure to wrap the `Label` widget in a [`ScrollView`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.scrollview?view=xamarin-forms) to enable scrolling.

```xml
<ScrollView>
    <Label x:name="transcript" Text="{Binding ApptTranscript}" />
</ScrollView>
```
