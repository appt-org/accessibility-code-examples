# Localization - iOS

On iOS, you can set the locale of an app via the [`CFBundleDevelopmentRegion`](http://cfbundledevelopmentregion) property.  We suggest using `Base internationalization` to separate user-facing strings from `.storyboard` and `.xib files`. You can load a specific [`Bundle`](https://developer.apple.com/documentation/foundation/bundle) to load assets in the desired language.

For more information, see [Adding Support for Languages and Regions](https://developer.apple.com/documentation/xcode/adding-support-for-languages-and-regions).

```swift
extension String {
    func localized(_ language: String) -> String {
        guard let path = Bundle.main.path(forResource: language, ofType: "lproj"),
              let bundle = Bundle(path: path) else {
          return localized(Bundle.main)
        }
        return NSLocalizedString(self, tableName: nil, bundle: bundle, value: "", comment: "")
    }
}
```
