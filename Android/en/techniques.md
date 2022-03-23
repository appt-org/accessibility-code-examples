# Important accessibility techniques for Android apps

This file contains important accessibility techniques for Android apps.

## Table of Contents <!-- omit in toc -->

- [1. Set accessibility label](#1-set-accessibility-label)
- [2. Set accessibility focus](#2-set-accessibility-focus)
- [3. Set accessibility visibility](#3-set-accessibility-visibility)
- [4. Group accessibility elements](#4-group-accessibility-elements)
- [5. Using AccessibilityNodeInfoCompat](#5-using-accessibilitynodeinfocompat)
  - [5.1. Mark accessibility button](#51-mark-accessibility-button)
  - [5.2. Mark accessibility heading](#52-mark-accessibility-heading)
  - [5.3. Add accessibility description](#53-add-accessibility-description)
  - [5.4. Set accessibility order](#54-set-accessibility-order)
- [6. Using AccessibilityManager](#6-using-accessibilitymanager)
  - [6.1. Announcing a message](#61-announcing-a-message)
  - [6.2. Interrupt assistive technology](#62-interrupt-assistive-technology)
  - [6.3. Check if screen reader is active](#63-check-if-screen-reader-is-active)
- [7. Toolbar accessibility](#7-toolbar-accessibility)
- [8. Keyboard accessibility](#8-keyboard-accessibility)
  - [8.1. Dashed border on focus](#81-dashed-border-on-focus)
  - [8.2. Color change on focus](#82-color-change-on-focus)
- [9. Spanned accessibility](#9-spanned-accessibility)
- [9.1 Split into paragraphs](#91-split-into-paragraphs)
  - [9.2. Determine attribute values](#92-determine-attribute-values)
    - [Detecting header style](#detecting-header-style)
    - [Detecting list style](#detecting-list-style)
    - [Detecting empty paragraphs](#detecting-empty-paragraphs)
  - [9.3 Create interface elements](#93-create-interface-elements)
- [Acknowledgements](#acknowledgements)

## 1. Set accessibility label

You can set a custom label which assistive technologies use by setting the `contentDescription` property.

```kotlin
fun label(view: View, label: CharSequence): View {
    view.contentDescription = label
    return view
}
```

## 2. Set accessibility focus

Sometimes you want to move the accessibility focus to a specific view. You can do so by sending a `TYPE_VIEW_FOCUSED` accessibility event. The view must be focusable for this event to take effect.

```kotlin
fun focus(view: View): View {
    view.isFocusable = true
    view.sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_FOCUSED)
    return view
}
```

## 3. Set accessibility visibility

Certain views are not important for assistive technologies, such as decorative images. You can hide a view for assistive technologies using the `isFocusable` and `importantForAccessibility` properties.

```kotlin
fun visible(view: View, visible: Boolean): View {
    view.isFocusable = false
    view.importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_NO
    return view
}
```

## 4. Group accessibility elements
In lists and other places, it often makes sense to group multiple elements together for users of assistive technologies. For example, let's say you have a list with items containing a date and title. You can group the date and title together by using the `android:focusable` and `android:contentDescription` attributes. From Android 9 (API 28), you can also use the `android:screenReaderFocusable` to set the focusable state only for screen reader users.

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/root"
    android:focusable="true"
    android:contentDescription="Date and title">

    <TextView
        android:id="@+id/date"
        android:text="01-01-2021"
        android:focusable="false"/>

    <TextView
        android:id="@+id/title"
        android:text="Title"
        android:focusable="false"/>
</LinearLayout>
```

## 5. Using AccessibilityNodeInfoCompat

The `AccessibilityNodeInfoCompat` is the entry point for many accessibility methods. It requires a couple of lines of code to access. This `accessibilityDelegate` method provides a callback for easier access.

```kotlin
fun accessibilityDelegate(view: View, callback: (host: View, info: AccessibilityNodeInfoCompat) -> Unit) {
    ViewCompat.setAccessibilityDelegate(view, object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)
            callback(host, info)
        }
    })
}
```

### 5.1. Mark accessibility button

Elements that act as button should be marked as buttons for assistive technologies. The best way to achieve this is to set the `className` property inside `AccessibilityNodeInfoCompat`. By setting the class name to `Button`, Android will automatically localize the description. For example, in English it's Button", in Dutch it's "Knop".

```kotlin
fun button(view: View, isButton: Boolean = true): View {
    accessibilityDelegate(view) { _, info ->
        info.className = if (isButton) {
            Button::class.java.name
        } else {
            this::class.java.name
        }
    }
    return view
}
```

### 5.2. Mark accessibility heading

Elements that act as heading should be marked as heading for assistive technologies. You can use the the `ViewCompat.setAccessibilityHeading(textView, true)` method. Or you can set the `isHeading` property of `AccessibilityNodeInfoCompat` to true.

```kotlin
fun heading(view: View, isHeading: Boolean = true): View {
    accessibilityDelegate(view) { _, info ->
        info.isHeading = isHeading
    }
    return view
}
```

### 5.3. Add accessibility description

When interactive elements behave differently than a user might expect, you can add an accessibility description. You can describe the action which will happen on the given [type of action](https://developer.android.com/reference/kotlin/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.AccessibilityActionCompat#properties).

```kotlin
fun description(view: View, type: Int, description: CharSequence): View {
    accessibilityDelegate(view) { _, info ->
        val action = AccessibilityNodeInfoCompat.AccessibilityActionCompat(type, description)
        info.addAction(action)
    }
    return view
}
```

### 5.4. Set accessibility order

You can use `setTraversalBefore()` and `setTraversalAfter()` methods to modify the accessibility order. This is how you can set the order of multiple views:

```kotlin
fun order(vararg views: View) {
    if (views.size < 2) {
        return
    }
    for (i in 0 until views.size-1) {
        accessibilityDelegate(views[i]) { _, info ->
            info.setTraversalBefore(views[i+1])
        }
    }
}
```

## 6. Using AccessibilityManager

The `AccessibilityManager` provides access to interact with the active assistive technology. You can retrieve an instance with a `Context` reference. This `accessibilityManager` method provides easier access and checks if any assistive technology is active.

```kotlin
fun accessibilityManager(context: Context?): AccessibilityManager? {
    if (context != null) {
        val manager = ContextCompat.getSystemService(context, AccessibilityManager::class.java)
        if (manager is AccessibilityManager && manager.isEnabled) {
            return manager
        }
    }
    return null
}
```

### 6.1. Announcing a message

You can announce a message by sending a `TYPE_ANNOUNCEMENT` event. The effect depends on the kind of assistive technology that is running. For example, with TalkBack, the provided message will be read aloud.

```kotlin
fun announce(context: Context?, message: String) {
    accessibilityManager(context)?.let { accessibilityManager ->
        val event = AccessibilityEvent.obtain(AccessibilityEventCompat.TYPE_ANNOUNCEMENT)
        event.text.add(message)

        accessibilityManager.sendAccessibilityEvent(event)
    }
}
```

### 6.2. Interrupt assistive technology

You can interrupt assistive technology by calling the `interrupt()` method. The effect depends on the kind of assistive technology that is running. For example, with TalkBack, any spoken announcements will be stopped.

```Kotlin
fun interrupt(context: Context?) {
    accessibilityManager(context)?.interrupt()
}
```

### 6.3. Check if screen reader is active

Sometimes it can be helpful to know if a screen reader is active. You can check this by retrieving a list of enabled accessibility services. Screen readers always have the `FEEDBACK_SPOKEN` flag set to true. In addition, screen reader have the `isTouchExplorationEnabled` property set to true. Combine these two to make sure a screen reader is active.

```kotlin
fun screenReaderActive(context: Context?): Boolean {
    accessibilityManager(context)?.let { accessibilityManager ->
        return@let accessibilityManager.isTouchExplorationEnabled &&
                   accessibilityManager.getEnabledAccessibilityServiceList(
                      AccessibilityServiceInfo.FEEDBACK_SPOKEN
                   ).isNotEmpty()
    }
    return false
}
```

## 7. Toolbar accessibility

By default, the title of the Toolbar is not marked as heading. Marking the title as heading helps users of assistive technologies to understand where they are in a screen. Menu items are not always marked as button. This also helps users of assistive technologies understand that they can execute an action on these items.

You can subclass `Toolbar` to automatically mark the title as heading and menu items as button.

```kotlin
class Toolbar @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = R.attr.toolbarStyle
) : androidx.appcompat.widget.Toolbar(context, attrs, defStyleAttr) {

    override fun setTitle(title: CharSequence?) {
        super.setTitle(title)

        // Mark title as heading
        children.filterIsInstance(AppCompatTextView::class.java)
                .firstOrNull()?.let { textView ->
            Accessibility.heading(textView, true)
        }
    }

    override fun inflateMenu(resId: Int) {
        super.inflateMenu(resId)

        // Mark menu items as button
        children.filterIsInstance(ActionMenuView::class.java)
                .firstOrNull()?.let { menu ->
            menu.children.forEach { view ->
                Accessibility.button(view, true)
            }
        }
    }
}
```

## 8. Keyboard accessibility

There is limited documentation on making an Android app fully keyboard accessible. One of the most important things is to let users know which element has focus. There are multiple ways to achieve this.

### 8.1. Dashed border on focus

One option is to show a dashed border around the focused element.

Create drawable selector `focus_selector.xml` in the `drawable` folder.

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@drawable/focus_border" android:state_focused="true" />
    <item android:drawable="@android:color/transparent"/>
</selector>
```

Create shape `focus_border.xml` in the `drawable` folder.

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">

    <stroke android:top="50dp"
        android:width="3dp"
        android:dashGap="3dp"
        android:dashWidth="3dp"
        android:color="@color/primary"/>

</shape>
```

By setting `android:background` to `@drawable/focus_border`, a dashed border is shown on focus.

### 8.2. Color change on focus
Create color selector `focus_color.xml` in the `color` folder.

```xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/primary" android:state_focused="true"/>
    <item android:color="@android:color/transparent"/>
</selector>
```

By setting `android:backgroundTint` to `@color/focus_color`, the background color changes on focus.

## 9. Spanned accessibility

It is often a requirement to markup text in a specific way. It can be tempting to write and parse HTML to achieve this. For example:

```html
Sentence with <strong>bold</strong> emphasis.

<h1>Important list</h1>
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
</ul>
```

You can initialize a `Spanned` with the HTML to create a String with the desired formatting.

**But there is a big accessibility problem: the markup is lost during the conversion.** The result is that the screen reader announces all text at once. One of the requirements from [WCAG 1.3.1](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html) is that assistive technologies should be able to access the information and relationships that are displayed visually.

This means that users need to be able to navigate the list items one by one, and the "Important list" heading should be marked up as heading.

To achieve this, each paragraph needs to consist of its own interface element. My recommendation is to populate a `RecyclerView` or `ScrollView` and avoid using HTML. But if this is not a viable option, you can follow three steps to improve the accessibility.

## 9.1 Split into paragraphs

By splitting text on the linebreak (`\n`) character you can create an array of paragraphs. By using the default substring method, you lose some of the attributes. You need to use the `subSequence()` method to keep the attributes.

```kotlin
fun Spanned.substring(start: Int, end: Int): Spanned {
    (subSequence(start, end) as? Spanned)?.let { substring ->
        return substring
    }
    return this
}
```

The `indexOf()` method can be used to determine the linebreaks. Combine this with the `substring` method to create a list of `Spanned` objects.

```kotlin
fun Spanned.separated(separator: String): List<Spanned> {
    val substrings = arrayListOf<Spanned>()

    var start = 0
    var index = indexOf(separator, start)

    while (index != -1) {
        substrings.add(substring(start, index))

        start = index + separator.length
        index = indexOf(separator, start)
    }

    substrings.add(substring(start, length))

    return substrings
}
```

### 9.2. Determine attribute values

We now have a list of `Spanned` objects, each representing a paragraph of text. To create the correct markup, it's important to detect headers, list items and empty paragraphs.

#### Detecting header style

The `getSpans()` method can be used to retrieve certain type of spans. A header is usually represented by a `RelativeSizeSpan`, which should have size change greater than zero. If a span uses a `Typeface.BOLD` for each character, it's usually a header.

```kotlin
val Spanned.isHeading: Boolean
    get() {
        return getSpans<StyleSpan>().any { span ->
            return span.style == Typeface.BOLD &&
                   getSpanStart(span) == 0 &&
                   getSpanEnd(span) == length
        } || getSpans<RelativeSizeSpan>().any { span ->
            return span.sizeChange > 0
        }
    }
```

#### Detecting list style

A list item is usually represented by a `BulletSpan`. If a span contains one or more of these, you can assume it is a list item.

```kotlin
val Spanned.isListItem: Boolean
    get() {
        return getSpans<BulletSpan>().isNotEmpty()
    }
```

#### Detecting empty paragraphs

If a paragraph only contains whitespace characters, it should be ignored by assistive technologies. Whitespace can be detected by using the `Spanned#isBlank()` method.

### 9.3 Create interface elements

Now that we have our paragraphs and are able to determine the attributes, it's time to create interface elements.

Create a subclass of `LinearLayout` named `HtmlTextViewWidget`. Add the `setHtmlText` method to set HTML text.

Create a subclass of `TextView` named `HtmlTextView`. Each HtmlTextView will display one paragraph of text. The most basic implementation only sets the `text` property.

Putting everything together:

```kotlin
fun setHtmlText(htmlText: String) {
    // Step 1: Parse the given String into a Spannable
    val spannable = getSpannableFromHtml(htmlText)

    // Step 2: Separate the Spannable on each linebreak
    val parts = spannable.separated("\n")

    // Step 3: Add a HtmlTextView for each part of the Spannable
    parts.forEachIndexed { index, part ->
        val textView = HtmlTextView(context)
        textView.text = part

        // Mark as heading?
        if (part.isHeading) {
            ViewCompat.setAccessibilityHeading(textView, true)
        }

        // Hide for assistive technologies?
        if (part.isBlank()) {
            textView.isFocusable = false
            textView.importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_NO
        }

        addView(textView)
    }
}
```

Depending on your styling requirements, you might need some more tweaks to make everything appear correctly.

Check out the full code here: [HtmlTextViewWidget.kt](https://github.com/minvws/nl-covid19-coronacheck-app-android/blob/main/design/src/main/java/nl/rijksoverheid/ctr/design/views/HtmlTextViewWidget.kt) and [HtmlTextView.kt](https://github.com/minvws/nl-covid19-coronacheck-app-android/blob/main/design/src/main/java/nl/rijksoverheid/ctr/design/views/HtmlTextView.kt).

## Acknowledgements

These code examples are based on:

- [appt-android](https://github.com/appt-nl/appt-android), licensed under [MIT](https://opensource.org/licenses/MIT)
- [nl-covid19-coronacheck-app-android](https://github.com/minvws/nl-covid19-coronacheck-app-android/commits?author=JJdeGroot), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)
- [nl-covid19-dbco-app-android](https://github.com/minvws/nl-covid19-dbco-app-android/commits?author=JJdeGroot), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)
- [nl-covid19-notification-app-android](https://github.com/minvws/nl-covid19-notification-app-android/commit/d8fb1167bd069304e42b0a50c6a983ce147cb7cd), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)
