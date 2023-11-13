# Scale text - React Native

React Native automatically scales text depending on the font size preferences of the user settings. In addition, all dimensions in React Native are unitless, and represent density-independent pixels.

Try to avoid using properties such as [`maxFontSizeMultiplier`](https://reactnative.dev/docs/text#maxfontsizemultiplier), [`allowFontScaling`](https://reactnative.dev/docs/text#allowfontscaling), [`adjustsFontSizeToFit`](https://reactnative.dev/docs/text#adjustsfontsizetofit) and [`numberOfLines`](https://reactnative.dev/docs/text#numberoflines). Using these properties may cause text to be unscalable or become inaccessible.

When inheriting a project you may find previous developers have disabled font-scaling with the following code: `Text.defaultProps.allowFontScaling = false;`. This is accessibility anti-pattern and should be rolled back.

The code example below shows how to have a scaling font size.

```jsx
<Text style={{ fontSize: 16 }}>
    Appt
</Text>
```
