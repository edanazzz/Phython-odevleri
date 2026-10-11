# Kapsam (Scope) Notları

Dersteki örneklerde global, local ve nonlocal değişkenlerin nasıl çalıştığı gösterilmiştir. Değişkenin tanımlandığı yer, onun nereden erişilebileceğini belirler.

## UnboundLocalError Nedir?
Bir fonksiyonun içinde, dışarıda (globalde) tanımlanmış bir değişkene doğrudan yeni bir değer atamaya çalışırsak Python bunu önce "yerel (local) bir değişken" olarak kabul eder. Ancak bu değişkene bir değer atanmadan önce onu okumaya veya üzerinde işlem yapmaya kalkarsak program `UnboundLocalError` hatası verir.
